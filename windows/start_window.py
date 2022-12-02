import main as m
from widgets.text_frame import Text_frame
import widgets.keyboard as k
from arduino.arduino_control import *



#######################################################################################
def code_check():
    arduino("activeGame=0")
    arduino("activeMachine=0")
    # resizing the background to fit the display
    metalic_background_logo = m.pygame.transform.scale(
        m.metal_plate_museumlogo, (m.WIDTH * 0.5, m.HEIGHT)
    )

    metalic_background__info_board = m.pygame.transform.scale(
        m.metal_plate_infoboard, (m.WIDTH * 0.5, m.HEIGHT)
    )

    # resizing a single screw to later use by the backgrounds
    single_screw = m.pygame.transform.scale(
        m.single_screw, (m.WIDTH * 0.025, m.WIDTH * 0.025)
    )

    # deviding the welcoming message to 2 separate phrases
    welcome_text_1 = Text_frame(
        None,
        None,
        None,
        "Welkom bij de",
        m.white_color,
        m.MagdaClean_font_70,
        m.WIDTH * 0.215 + 10,
        m.HEIGHT * 0.39,
    )
    welcome_text_2 = Text_frame(
        None,
        None,
        None,
        "Escape Game van",
        m.white_color,
        m.MagdaClean_font_70,
        m.WIDTH * 0.255,
        m.HEIGHT * 0.46,
    )

    # deviding the code-insertion instruction message to 3 separate phrases
    instruction_1 = Text_frame(
        None,
        None,
        None,
        "Voer de code in die je bij de ",
        m.black_color,
        m.MagdaClean_font_30,
        m.WIDTH * 0.75,
        m.HEIGHT * 0.2,
    )
    instruction_2 = Text_frame(
        None,
        None,
        None,
        "balie hebt gekregen om het spel ",
        m.black_color,
        m.MagdaClean_font_30,
        m.WIDTH * 0.75,
        m.HEIGHT * 0.24,
    )
    instruction_3 = Text_frame(
        None,
        None,
        None,
        "te starten.",
        m.black_color,
        m.MagdaClean_font_30,
        m.WIDTH * 0.75,
        m.HEIGHT * 0.28,
    )
    # deviding the incorrect-code  warning message to deviding
    incorrect_code_message_1 = Text_frame(
        None,
        None,
        None,
        "De code is onjuist. Ga naar de ",
        m.red_color,
        m.MagdaClean_font_30,
        m.WIDTH * 0.75,
        m.HEIGHT * 0.2,
    )
    incorrect_code_message_2 = Text_frame(
        None,
        None,
        None,
        "balie om je aan te melden voor ",
        m.red_color,
        m.MagdaClean_font_30,
        m.WIDTH * 0.75,
        m.HEIGHT * 0.24,
    )
    incorrect_code_message_3 = Text_frame(
        None,
        None,
        None,
        "de Escape Game ",
        m.red_color,
        m.MagdaClean_font_30,
        m.WIDTH * 0.75,
        m.HEIGHT * 0.28,
    )

    # keyboard
    keyboard = k.Keyboard(m.WIDTH * 0.68, m.HEIGHT * 0.52)
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0
    incorrect_code = False
    display_background = True
    button_pushed = True

    # play the music in an infinite loop
    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # displaying the background images
        if display_background:
            m.SCREEN.blit(metalic_background_logo, (0, 0))
            # displaying the screws
            # top left, left part
            m.SCREEN.blit(single_screw, (m.WIDTH * 0.025, m.HEIGHT * 0.05))
            # top right, left part
            m.SCREEN.blit(
                single_screw,
                (m.WIDTH * 0.5 - (m.WIDTH * 0.001) - (m.WIDTH * 0.05), m.HEIGHT * 0.05),
            )
            # bottom left, left part
            m.SCREEN.blit(
                single_screw, (m.WIDTH * 0.025, (m.HEIGHT - (m.HEIGHT * 0.1)))
            )
            # bottom right, left part
            m.SCREEN.blit(
                single_screw,
                (
                    m.WIDTH * 0.5 - (m.WIDTH * 0.001) - (m.WIDTH * 0.05),
                    m.HEIGHT - (m.HEIGHT * 0.1),
                ),
            )
            # displaying the welcoming message
            welcome_text_1.display()
            welcome_text_2.display()

            display_background = False

        if button_pushed:
            # displaying the right background
            m.SCREEN.blit(metalic_background__info_board, (m.WIDTH * 0.5, 0))

            # displaying the screws

            # top left, right part
            m.SCREEN.blit(
                single_screw, (m.WIDTH * 0.5 + (m.WIDTH * 0.025), m.HEIGHT * 0.05)
            )
            # top right, right part
            m.SCREEN.blit(
                single_screw,
                (m.WIDTH - (m.WIDTH * 0.001) - (m.WIDTH * 0.05), m.HEIGHT * 0.05),
            )
            # bottom left, right part
            m.SCREEN.blit(
                single_screw,
                (m.WIDTH * 0.5 + (m.WIDTH * 0.025), (m.HEIGHT - (m.HEIGHT * 0.1))),
            )
            # bottom right, right part
            m.SCREEN.blit(
                single_screw,
                (
                    m.WIDTH - (m.WIDTH * 0.001) - (m.WIDTH * 0.05),
                    (m.HEIGHT - (m.HEIGHT * 0.1)),
                )
            )

            # displaying the keyboard
            keyboard.display()

            # displaying the warning in case of incorrect code insertion
            if not incorrect_code:
                instruction_1.display()
                instruction_2.display()
                instruction_3.display()
            else:
                incorrect_code_message_1.display()
                incorrect_code_message_2.display()
                incorrect_code_message_3.display()
            
            button_pushed = False

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

        # resize the clicked button
        if timer >= int(m.button_resizing_delay / 3):

            # to the next window (if the code was correct)
            if pressed_button == 10:
                if code == m.start_code:
                    m.start_game_robot_voice_correct_code.play()
                    return
                else:
                    incorrect_code = True
                    m.start_game_robot_voice_incorrect_code.play()
                    
            else:
                # to stop robot's sound by new code insertion
                m.start_game_robot_voice_incorrect_code.stop()

                m.click_sound.play()
            code = keyboard.keyboard_button_pressed(pressed_button, code)

            # reset
            keyboard.resize_buttons()
            button_pressed = False
            pressed_button = 99
            timer = 0
            button_pushed = True

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            # or the escape button on the keyboard
            if event.type == m.pygame.QUIT or (
                event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE
            ):
                m.pygame.quit()

            if event.type == m.pygame.MOUSEBUTTONDOWN:

                pressed_button = keyboard.pressed_button()

                if pressed_button in range(0, 12):
                    button_pressed = True
                    button_pushed = True

        # the window should be updated after each while-loop
        m.pygame.display.update()


######################################################################################################


def corret_code():

    # resizinf the background image to fit the hole display
    black_background = m.pygame.transform.scale(
        m.black_screen_background, (m.WIDTH, m.HEIGHT)
    )

    # scaling the message to appear once a correct code insertion occur
    info_text = Text_frame(
        None,
        None,
        None,
        "De code is … JUIST!",
        m.green_color,
        m.MagdaClean_font_50,
        m.WIDTH * 0.45,
        m.HEIGHT * 0.32,
    )

    # resizinf the gear image for later use as animation
    green_gear_1 = m.pygame.transform.scale(
        m.green_gear_1, (m.WIDTH * 0.05, m.WIDTH * 0.05)
    )
    green_gear_2 = m.pygame.transform.scale(
        m.green_gear_2, (m.WIDTH * 0.05, m.WIDTH * 0.05)
    )
    green_gear_3 = m.pygame.transform.scale(
        m.green_gear_3, (m.WIDTH * 0.05, m.WIDTH * 0.05)
    )
    green_gear_4 = m.pygame.transform.scale(
        m.green_gear_4, (m.WIDTH * 0.05, m.WIDTH * 0.05)
    )

    green_gear_teller = 1
    delay = 0
    animation = 100
    start_time = m.pygame.time.get_ticks()

    while True:
        # to go to next screen after 3 seconds
        if  m.pygame.time.get_ticks() >= start_time + m.correct_code_animation_delay:
                return

        # animating the gears 
        if green_gear_teller == 1 and delay >= animation:
            m.SCREEN.blit(black_background, (0, 0))
            info_text.display()
            m.SCREEN.blit(green_gear_1, (m.WIDTH * 0.4, m.HEIGHT * 0.5))
            m.SCREEN.blit(green_gear_1, (m.WIDTH * 0.46, m.HEIGHT * 0.5))
            m.SCREEN.blit(green_gear_1, (m.WIDTH * 0.43, m.HEIGHT * 0.43))
            m.SCREEN.blit(green_gear_1, (m.WIDTH * 0.49, m.HEIGHT * 0.43))
            green_gear_teller +=1 
            delay = 0
        elif green_gear_teller == 2 and delay >= animation:
            m.SCREEN.blit(black_background, (0, 0))
            info_text.display()
            m.SCREEN.blit(green_gear_2, (m.WIDTH * 0.4, m.HEIGHT * 0.5))
            m.SCREEN.blit(green_gear_2, (m.WIDTH * 0.46, m.HEIGHT * 0.5))
            m.SCREEN.blit(green_gear_2, (m.WIDTH * 0.43, m.HEIGHT * 0.43))
            m.SCREEN.blit(green_gear_2, (m.WIDTH * 0.49, m.HEIGHT * 0.43))
            green_gear_teller +=1
            delay = 0
        elif green_gear_teller == 3 and delay >= animation:
            m.SCREEN.blit(black_background, (0, 0))
            info_text.display()
            m.SCREEN.blit(green_gear_3, (m.WIDTH * 0.4, m.HEIGHT * 0.5))
            m.SCREEN.blit(green_gear_3, (m.WIDTH * 0.46, m.HEIGHT * 0.5))
            m.SCREEN.blit(green_gear_3, (m.WIDTH * 0.43, m.HEIGHT * 0.43))
            m.SCREEN.blit(green_gear_3, (m.WIDTH * 0.49, m.HEIGHT * 0.43))
            green_gear_teller +=1
            delay = 0
        elif green_gear_teller == 4 and delay >= animation:
            m.SCREEN.blit(black_background, (0, 0))
            info_text.display()
            m.SCREEN.blit(green_gear_4, (m.WIDTH * 0.4, m.HEIGHT * 0.5))
            m.SCREEN.blit(green_gear_4, (m.WIDTH * 0.46, m.HEIGHT * 0.5))
            m.SCREEN.blit(green_gear_4, (m.WIDTH * 0.43, m.HEIGHT * 0.43))
            m.SCREEN.blit(green_gear_4, (m.WIDTH * 0.49, m.HEIGHT * 0.43))
            green_gear_teller = 1
            delay = 0

        delay += 1

        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            # or the escape button on the keyboard
            if event.type == m.pygame.QUIT or (
                event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE
            ):
                m.pygame.quit()

            if event.type == m.pygame.MOUSEBUTTONDOWN:
                return

        # the window should be updated after each while-loop
        m.pygame.display.update()


######################################################################################################


def start_window():

    m.TOTAL_PLAY_TIME = 0
    code_check()
    corret_code()
