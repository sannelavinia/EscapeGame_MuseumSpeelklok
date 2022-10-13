import pygame
import main as m
import widgets.keyboard as k
from widgets.massage_box import Massage_box
from widgets.code_frame import Text_frame
import widgets.button as b


#######################################################################################
def game_4_window():

    # massage = Massage_box(m.message, 400, 300,
    #                       m.game_1_explanation, m.black_color, 100, 300)
    title = Text_frame(None, "Spel 4", m.black_color,
                       m.speelklok_website_font, m.WIDTH/2, (m.HIGHT/2)-255)

    instruction_box = pygame.transform.scale(m.instruction_box, (500, 400))

    instruction_box = Text_frame(instruction_box, "", m.black_color,
                                 m.code_font, m.WIDTH/3, m.HIGHT*3/5)

    instruction_title = Text_frame(None, "Instructies", m.black_color,
                                   m.code_font, 500, 300)

    logo_button = b.Button(m.ms_logo, m.ms_logo,
                           m.ms_logo, m.WIDTH-70, m.HIGHT-27)

    tip_button = b.Button(m.tip_button, m.tip_button,
                          m.tip_button_small, 40, m.HIGHT-40)

    tip_message_box = pygame.transform.scale(m.tip_message_box, (100, 200))
    tip_message_box = Text_frame(
        tip_message_box, "", m.black_color, m.main_font, 100, m.HIGHT - 120)

    tip_message = Text_frame(None, "hint!", m.black_color,
                             m.main_font, 150, m.HIGHT - 130)

    # background music
    m.pygame.mixer.music.load("Assets/sounds/game_4.wav")
    m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    keyboard = k.Keyboard(m.WIDTH*2/3, 300)  # the input keyboard
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0  # used for animating the buttons
    start_display_tip_icon = False
    start_display_tip_message = False
    logo_button_pressed = False
    restart_timer = 0

    start_time = m.pygame.time.get_ticks()
    time_difference = 0
    previous_second = 0
    play_time = Text_frame(None, m.from_millisecond_to_clock(
        m.TOTAL_PLAY_TIME + time_difference), m.green_color, m.code_font, m.WIDTH/8, (m.HIGHT/2)-260)

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        if restart_timer >= 300:
            return 1

        time_difference = m.pygame.time.get_ticks()-start_time

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(m.background_gears, (0, 0))
        m.SCREEN.blit(m.yellowbar, (0, 30))     # display yellow title bar
        play_time.display()
        title.display()
        instruction_box.display()
        instruction_title.display()
        # massage.display()
        keyboard.display()
        logo_button.display()

        if start_display_tip_icon:
            tip_button.display()
        if start_display_tip_message:
            tip_message_box.display()
            tip_message.display()

        # tik-sound every second
        if int((time_difference / 1000) % 60) != previous_second:
            previous_second = int((time_difference / 1000) % 60)
            m.clock_tik.play()

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

        # logo button functionality
        if logo_button_pressed and logo_button.mouse_on_button():
            restart_timer += 1
        else:
            logo_button_pressed = False
            restart_timer = 0

        # resize the clicked button
        if timer >= m.button_resizing_delay:
            # to the next window (if the code was correct)
            if pressed_button == 10:
                if code == m.game_1_code:
                    m.correct_answer_sound.play()
                    return
                else:
                    m.wrong_answer_sound.play()
            else:
                m.click_sound.play()
            code = keyboard.keyboard_button_pressed(pressed_button, code)
            keyboard.text_frame.change_input_text(code, m.white_color)
            # reset
            keyboard.resize_buttons()
            tip_button.restore_normal_size()
            button_pressed = False
            pressed_button = 99
            timer = 0

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.QUIT:
                m.pygame.quit()

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN:
                pressed_button = keyboard.pressed_button()

                if pressed_button in range(0, 12):
                    button_pressed = True
                if tip_button.mouse_on_button() and start_display_tip_icon:
                    tip_button.display_click_animation()
                    button_pressed = True
                    start_display_tip_message = True
                if logo_button.mouse_on_button():
                    logo_button_pressed = True

        if time_difference < m.game_1_normal_time:
            play_time.change_input_text(m.from_millisecond_to_clock(
                m.TOTAL_PLAY_TIME + time_difference), m.green_color)
        else:
            play_time.change_input_text(m.from_millisecond_to_clock(
                m.TOTAL_PLAY_TIME + time_difference), m.red_color)
            start_display_tip_icon = True

        # the window should be updated after each while-loop
        m.pygame.display.update()
