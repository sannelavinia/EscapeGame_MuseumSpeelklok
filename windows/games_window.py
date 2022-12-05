import main as m
import widgets.keyboard as k
import widgets.text_frame as t
import widgets.button as b
import widgets.instruction_box as i
import windows.start_window as sw
from arduino.arduino_control import *

#######################################################################################
def push_button_to_start(game_number):

    # resizing the images
    metal_plate_empty = m.pygame.transform.scale(
        m.metal_plate_empty, (m.WIDTH / 2, m.HEIGHT)
    )
    single_screw = m.pygame.transform.scale(
        m.single_screw, (m.WIDTH * 0.025, m.WIDTH * 0.025)
    )
    rings_for_gears_with_gears = m.pygame.transform.scale(
        m.rings_for_gears_with_gears, (m.WIDTH * 0.35, m.HEIGHT * 0.23)
    )

    # text variables
    text_0 = t.Text_frame(
        None,
        None,
        None,
        "Druk op start om het spel",
        m.black_color,
        m.MagdaClean_font_50,
        m.WIDTH / 4,
        (m.HEIGHT / 2) - 60,
    )
    text_1 = t.Text_frame(
        None,
        None,
        None,
        "te beginnen. De tijd zal",
        m.black_color,
        m.MagdaClean_font_50,
        m.WIDTH / 4,
        m.HEIGHT / 2,
    )
    text_2 = t.Text_frame(
        None,
        None,
        None,
        "dan ook meteen gaan lopen!",
        m.black_color,
        m.MagdaClean_font_50,
        m.WIDTH / 4,
        (m.HEIGHT / 2) + 60,
    )
    text_3 = t.Text_frame(
        None,
        None,
        None,
        "Dus … GO!!!! ",
        m.black_color,
        m.MagdaClean_font_50,
        m.WIDTH / 4,
        (m.HEIGHT / 2) + 120,
    )
    # ( Na spel 6! )
    text_4 = t.Text_frame(
        None,
        None,
        None,
        "Gefeliciteerd! Jullie hebben alle",
        m.black_color,
        m.MagdaClean_font_50,
        m.WIDTH / 4,
        m.HEIGHT * 0.24,
    )
    text_5 = t.Text_frame(
        None,
        None,
        None,
        "6 tandwielen",
        m.white_color,
        m.MagdaClean_font_50,
        m.WIDTH * 0.17,
        m.HEIGHT * 0.3,
    )
    text_6 = t.Text_frame(
        None,
        None,
        None,
        "verzameld.",
        m.black_color,
        m.MagdaClean_font_50,
        m.WIDTH * 0.35,
        m.HEIGHT * 0.3,
    )
    text_7 = t.Text_frame(
        None,
        None,
        None,
        "Klik op de knop om de",
        m.black_color,
        m.MagdaClean_font_50,
        m.WIDTH * 0.25,
        m.HEIGHT * 0.36,
    )
    text_8 = t.Text_frame(
        None,
        None,
        None,
        "eindmontage",
        m.white_color,
        m.MagdaClean_font_50,
        m.WIDTH * 0.18,
        m.HEIGHT * 0.42,
    )
    text_9 = t.Text_frame(
        None,
        None,
        None,
        "te starten",
        m.black_color,
        m.MagdaClean_font_50,
        m.WIDTH * 0.35,
        m.HEIGHT * 0.42,
    )

    text_button_start = t.Text_frame(
        None,
        None,
        None,
        "START",
        m.white_color,
        m.MagdaClean_font_70,
        m.WIDTH * 3 / 4,
        m.HEIGHT / 2,
    )

    # start button
    green_start_button = b.Button(
        m.green_start_button,
        m.green_start_button,
        m.green_start_button_pushed,
        m.WIDTH * 3 / 4,
        m.HEIGHT / 2,
        m.WIDTH / 4,
        m.WIDTH / 4,
    )

    # for speeding up
    displayed = False
    button_pushed = True
    button_pressed = False
    timer = 0  # used for animating the buttons

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:
        m.game_1_to_6_robot_voice_correct_code.stop()


        if not displayed:
            # display the background image ( it should be the fisrt image to display,
            # so that the other objects will be displayed ontop of it )
            m.SCREEN.blit(metal_plate_empty, (0, 0))
            m.SCREEN.blit(metal_plate_empty, (m.WIDTH / 2, 0))

            # display the screws
            # top left, left part
            m.SCREEN.blit(single_screw, (m.WIDTH * 0.025, m.HEIGHT * 0.05))
            # top right, left part
            m.SCREEN.blit(
                single_screw,
                (m.WIDTH * 0.5 - (m.WIDTH * 0.001) - (m.WIDTH * 0.05), m.HEIGHT * 0.05),
            )
            # top left, right part
            m.SCREEN.blit(
                single_screw, (m.WIDTH * 0.5 + (m.WIDTH * 0.025), m.HEIGHT * 0.05)
            )
            # top right, right part
            m.SCREEN.blit(
                single_screw,
                (m.WIDTH - (m.WIDTH * 0.001) - (m.WIDTH * 0.05), m.HEIGHT * 0.05),
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
                ),
            )

            # display the text
            if game_number <= 6:
                text_0.display()
                text_1.display()
                text_2.display()
                text_3.display()
            # ( Na spel 6! )
            else:
                text_4.display()
                text_5.display()
                text_6.display()
                text_7.display()
                text_8.display()
                text_9.display()
                m.SCREEN.blit(
                    rings_for_gears_with_gears, (m.WIDTH * 0.08, m.HEIGHT * 0.6)
                )
            displayed = True

        if button_pushed:
            # display the button
            green_start_button.display()
            text_button_start.display()
            button_pushed = False

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

        # resize the clicked button
        if timer >= m.button_resizing_delay:
            m.correct_answer_sound.play()
            button_pushed = True
            return

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            # or the escape button on the keyboard
            if event.type == m.pygame.QUIT or (
                event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE
            ):
                m.pygame.quit()

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN:

                if green_start_button.mouse_on_button():
                    green_start_button.display_click_animation()
                    button_pressed = True
                    button_pushed = True

        # the window should be updated after each while-loop
        m.pygame.display.update()


#######################################################################################
def game_started(
    game_number,
    game_instructions,
    game_code,
    game_tip_1=None,
    game_tip_2=None,
    game_tip_1_image=None,
    game_tip_2_image=None,
    game_tip_3_image=None,
    game_tip_4_image=None,
):
        
    arduino("activeMachine=2&" + "activeGame=" + str(game_number) + "\n")

    # resizing the images
    background_games_template = m.pygame.transform.scale(
        m.background_games_template, (m.WIDTH, m.HEIGHT)
    )

    rings_for_gears = m.pygame.transform.scale(
        m.rings_for_gears, (m.WIDTH / 3, m.HEIGHT / 6.5)
    )

    red_gear = m.pygame.transform.scale(m.red_gear, (m.WIDTH * 0.07, m.WIDTH * 0.07))
    orange_gear = m.pygame.transform.scale(
        m.orange_gear, (m.WIDTH * 0.07, m.WIDTH * 0.07)
    )
    yellow_gear = m.pygame.transform.scale(
        m.yellow_gear, (m.WIDTH * 0.07, m.WIDTH * 0.07)
    )
    green_gear = m.pygame.transform.scale(
        m.green_gear, (m.WIDTH * 0.07, m.WIDTH * 0.07)
    )
    blue_gear = m.pygame.transform.scale(m.blue_gear, (m.WIDTH * 0.07, m.WIDTH * 0.07))

    timer_bachground = m.pygame.transform.scale(m.black_screen_background, (390, 198))

    if game_tip_1_image != None:
        tip_image_1 = m.pygame.transform.scale(
            game_tip_1_image, (615, (m.HEIGHT / 2) - 50)
        )

    if game_tip_2_image != None:
        tip_image_2 = m.pygame.transform.scale(
            game_tip_2_image, (615, (m.HEIGHT / 2) - 50)
        )

    if game_tip_3_image != None:
        tip_image_3 = m.pygame.transform.scale(
            game_tip_3_image, (922, (m.HEIGHT / 2) - 50)
        )

    if game_tip_4_image != None:
        if game_tip_3_image != None:
            tip_image_4 = m.pygame.transform.scale(
                game_tip_4_image, (308, (m.HEIGHT / 2) - 50)
            )
        else:
            tip_image_4 = m.pygame.transform.scale(
                game_tip_4_image, (1230, (m.HEIGHT / 2) - 50)
            )

    # texts
    title = t.Text_frame(
        None,
        None,
        None,
        f"SPEL {game_number}",
        m.white_color,
        m.MagdaClean_font_70,
        m.WIDTH * 12 / 20,
        m.HEIGHT / 11,
    )

    instruction_title = t.Text_frame(
        None, None, None, "Instructies", m.green_color, m.MagdaClean_font_50, 600, 300
    )

    instruction_box = i.Instruction_Box(
        m.instruction_screen_games,
        1320,
        (m.HEIGHT / 2) + 36,
        game_instructions,
        m.green_color,
        3,
        (m.HEIGHT / 6) + 23,
        m.MagdaClean_font_30,
        40,
        60,
        50,
    )

    if game_tip_1 != None:
        tip_message_1 = i.Instruction_Box(
            m.instruction_screen_games,
            1316,
            (m.HEIGHT / 2) + 30,
            game_tip_1,
            m.green_color,
            0,
            (m.HEIGHT / 6) + 18,
            m.MagdaClean_font_30,
            40,
            60,
            50,
        )

    if game_tip_2 != None:
        tip_message_2 = i.Instruction_Box(
            m.instruction_screen_games,
            1316,
            (m.HEIGHT / 2) + 30,
            game_tip_2,
            m.green_color,
            0,
            (m.HEIGHT / 6) + 18,
            m.MagdaClean_font_30,
            40,
            60,
            50,
        )

    # buttons
    logo_button = b.Button(
        m.museum_logo_grey,
        m.museum_logo_grey,
        m.museum_logo_grey,
        m.WIDTH - (m.WIDTH / 6.7),
        m.HEIGHT - (m.HEIGHT / 12.55),
        m.WIDTH / 6.75,
        m.HEIGHT / 12.5,
    )

    tip_button = b.Button(
        m.tip_button_grey,
        m.tip_button,
        m.tip_button_pushed,
        (m.HEIGHT / 8) + 10,
        (m.HEIGHT - m.HEIGHT / 8) - 10,
        m.HEIGHT / 4,
        m.HEIGHT / 4,
    )

    # # background music
    # m.pygame.mixer.music.load("Assets/sounds/game_1.wav")
    # m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    keyboard = k.Keyboard(m.WIDTH - 450, 430)  # the input keyboard
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0  # used for animating the buttons
    start_display_tip_icon = False
    tip_button_to_yellow = False
    display_tip_message_1 = False
    display_tip_message_2 = False
    logo_button_pressed = False
    restart_timer = 0
    start_time = m.pygame.time.get_ticks()
    time_difference = 0
    previous_second = int((m.TOTAL_PLAY_TIME / 1000) % 60)
    play_time_as_text = t.Text_frame(
        None,
        None,
        None,
        m.from_millisecond_to_clock(m.TOTAL_PLAY_TIME),
        m.green_color,
        m.Quantico_font_50,
        m.WIDTH / 9,
        m.HEIGHT / 11,
    )

    tip_time = t.Text_frame(
        None,
        None,
        None,
        m.from_millisecond_to_clock(m.game_tip_1_time, True),
        m.black_color,
        m.Quantico_font_50,
        (m.HEIGHT / 8) + 10,
        (m.HEIGHT - m.HEIGHT / 8) - 10,
    )

    # for speeding up
    displayed = False
    button_pushed = True
    tip_message_1_displayed = False
    tip_message_2_displayed = False
    reset_tip_button = True

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        if restart_timer >= m.restart_time_logo_pressed:
            if m.admin_mode() == 1:
                return 1

            # reset for dispaly
            displayed = False
            button_pushed = True
            tip_message_1_displayed = False
            tip_message_2_displayed = False
            reset_tip_button = True

        time_difference = m.pygame.time.get_ticks() - start_time
        play_time = m.TOTAL_PLAY_TIME + time_difference
        play_time_seconds = int((play_time / 1000) % 60)


        if not displayed:
            # display the background image ( it should be the fisrt image to display,
            # so that the other objects will be displayed ontop of it )
            m.SCREEN.blit(background_games_template, (0, 0))
            title.display()
            instruction_box.display()
            instruction_title.display()
            logo_button.display()
            if game_number >= 2:
                m.SCREEN.blit(red_gear, (m.WIDTH * 0.2295, m.HEIGHT * 0.794))
            if game_number >= 3:
                m.SCREEN.blit(orange_gear, (m.WIDTH * 0.293, m.HEIGHT * 0.858))
            if game_number >= 4:
                m.SCREEN.blit(yellow_gear, (m.WIDTH * 0.358, m.HEIGHT * 0.793))
            if game_number >= 5:
                m.SCREEN.blit(green_gear, (m.WIDTH * 0.43, m.HEIGHT * 0.761))
            if game_number >= 6:
                m.SCREEN.blit(blue_gear, (m.WIDTH * 0.4715, m.HEIGHT * 0.866))
            m.SCREEN.blit(rings_for_gears, (m.WIDTH / 4, m.HEIGHT * 16 / 20))

            displayed = True

        # redisplay the pushed button
        if button_pushed:
            keyboard.display()
            tip_button.display()
            if time_difference < m.game_tip_2_time:
                tip_time.display()
            button_pushed = False

        # display the timer
        m.SCREEN.blit(timer_bachground, (0, 0))
        play_time_as_text.display()

        # tik-sound every second
        if play_time_seconds != previous_second:
            # dispaly tip button with timer on it
            if time_difference < m.game_tip_2_time:
                tip_button.display()
                tip_time.display()
            elif reset_tip_button:
                tip_button.display()
                reset_tip_button = False
            previous_second = play_time_seconds
            m.clock_tik.play()

        # display the tip message
        if display_tip_message_1 and time_difference >= m.game_tip_1_time:
            if game_tip_1 != None:
                tip_message_1.display()
            if game_tip_1_image != None:
                m.SCREEN.blit(tip_image_1, (44, 240))
            if game_tip_2_image != None:
                m.SCREEN.blit(tip_image_2, (659, 240))
            display_tip_message_1 = False
            tip_message_1_displayed = True

        if display_tip_message_2 and time_difference >= m.game_tip_2_time:
            if game_tip_2 != None:
                tip_message_2.display()
            if game_tip_3_image != None:
                m.SCREEN.blit(tip_image_3, (44, 240))
                m.SCREEN.blit(tip_image_4, (966, 240))
            elif game_tip_4_image != None:
                m.SCREEN.blit(tip_image_4, (44, 240))
            tip_message_2_displayed = True
            display_tip_message_2 = False

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
        if timer >= int(m.button_resizing_delay / 3):

            if pressed_button != 12:
                # to the next window (if the code was correct)
                if pressed_button == 10:
                    if code == game_code:
                        m.game_1_to_6_robot_voice_correct_code.play()
                        m.TOTAL_PLAY_TIME += time_difference
                        sw.corret_code()
                        
                        return
                    else:
                        if game_number == 1:        
                            m.game_1_robot_voice_incorrect_code.play()
                        elif game_number == 2:
                            m.game_2_robot_voice_incorrect_code.play()
                        elif game_number == 3:
                            m.game_3_robot_voice_incorrect_code.play()
                        elif game_number == 4:
                            m.game_4_robot_voice_incorrect_code.play()
                        elif game_number == 5:
                            m.game_5_robot_voice_incorrect_code.play() 
                        elif game_number == 6:
                            m.game_6_robot_voice_incorrect_code.play()
                        code = keyboard.keyboard_button_pressed(
                            pressed_button, code, m.red_color
                        )
                        
                        # incorrect_code(game_number)
         
                else:
                    if game_number == 1:        
                        m.game_1_robot_voice_incorrect_code.stop()
                    elif game_number == 2:
                        m.game_2_robot_voice_incorrect_code.stop()
                    elif game_number == 3:
                        m.game_3_robot_voice_incorrect_code.stop()
                    elif game_number == 4:
                        m.game_4_robot_voice_incorrect_code.stop()
                    elif game_number == 5:
                        m.game_5_robot_voice_incorrect_code.stop() 
                    elif game_number == 6:
                        m.game_6_robot_voice_incorrect_code.stop()
                    m.click_sound.play()
                    code = keyboard.keyboard_button_pressed(pressed_button, code)
            else:
                m.click_sound.play()

            # reset
            keyboard.resize_buttons()
            if tip_button_to_yellow:
                tip_button.restore_normal_size()
            button_pressed = False
            button_pushed = True
            pressed_button = 99
            timer = 0

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            # or the escape button on the keyboard
            if event.type == m.pygame.QUIT or (
                event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE
            ):
                m.pygame.quit()

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN:
                pressed_button = keyboard.pressed_button()

                # pressing a keyboard button
                if pressed_button in range(0, 12):
                    button_pressed = True
                    button_pushed = True

                # pressing the tip button
                if tip_button.mouse_on_button() and start_display_tip_icon:
                    tip_button.display_click_animation()
                    button_pressed = True
                    button_pushed = True
                    pressed_button = 12
                    if tip_message_1_displayed:
                        if (
                            not tip_message_2_displayed
                            and time_difference >= m.game_tip_2_time
                        ):
                            display_tip_message_2 = True
                        else:
                            displayed = False
                            tip_message_1_displayed = False
                            tip_message_2_displayed = False
                    else:
                        display_tip_message_1 = True

                # pressing the logo button
                if logo_button.mouse_on_button():
                    logo_button_pressed = True

        # display the timer in green color
        if time_difference <= m.game_normal_time:
            play_time_as_text.change_input_text(
                m.from_millisecond_to_clock(play_time), m.green_color
            )
        else:  # display the timer in red color
            play_time_as_text.change_input_text(
                m.from_millisecond_to_clock(play_time), m.red_color
            )

        # display the tip button timer
        if time_difference <= m.game_tip_1_time:
            tip_time.change_input_text(
                m.from_millisecond_to_clock((m.game_tip_1_time) - time_difference, True)
            )
        elif time_difference <= m.game_tip_2_time:
            tip_time.change_input_text(
                m.from_millisecond_to_clock((m.game_tip_2_time) - time_difference, True)
            )

        # to display the yellow tip image ( instead of the grey one )
        if time_difference >= m.game_tip_1_time:
            start_display_tip_icon = True
            if not tip_button_to_yellow:
                tip_button_to_yellow = True
                tip_button.restore_normal_size()

        # the window should be updated after each while-loop
        m.pygame.display.update()


#######################################################################################

# def incorrect_code(game_number):

#     # resizinf the background image to fit the hole display
#     black_background = m.pygame.transform.scale(
#         m.black_screen_background, (m.WIDTH, m.HEIGHT)
#     )

#     # scaling the message to appear once a correct code insertion occur
#     info_text = m.Text_frame(
#         None,
#         None,
#         None,
#         "De code is … ONJUIST!",
#         m.red_color,
#         m.MagdaClean_font_50,
#         m.WIDTH * 0.45,
#         m.HEIGHT * 0.32,
#     )

#     # resizinf the gear image for later use as animation
#     red_gear_1 = m.pygame.transform.scale(
#         m.red_gear_1, (m.WIDTH * 0.05, m.WIDTH * 0.05)
#     )
#     red_gear_2 = m.pygame.transform.scale(
#         m.red_gear_2, (m.WIDTH * 0.05, m.WIDTH * 0.05)
#     )
#     red_gear_3 = m.pygame.transform.scale(
#         m.red_gear_3, (m.WIDTH * 0.05, m.WIDTH * 0.05)
#     )
#     red_gear_4 = m.pygame.transform.scale(
#         m.red_gear_4, (m.WIDTH * 0.05, m.WIDTH * 0.05)
#     )

#     red_gear_teller = 1
#     delay = 0
#     animation = 100
#     start_time = m.pygame.time.get_ticks()

#     while True:
#         # to go to next screen after 3 seconds
#         if  m.pygame.time.get_ticks() >= start_time + m.incorrect_code_animation_delay:
#             return

#         if game_number == 1:        
#             m.game_1_robot_voice_incorrect_code.play()
#         elif game_number == 2:
#             m.game_2_robot_voice_incorrect_code.play()
#         elif game_number == 3:
#             m.game_3_robot_voice_incorrect_code.play()
#         elif game_number == 4:
#             m.game_4_robot_voice_incorrect_code.play()
#         elif game_number == 5:
#             m.game_5_robot_voice_incorrect_code.play() 
#         elif game_number == 6:
#             m.game_6_robot_voice_incorrect_code.play()

#         # animating the gears 
#         if red_gear_teller == 1 and delay >= animation:
#             m.SCREEN.blit(black_background, (0, 0))
#             info_text.display() 
#             m.SCREEN.blit(red_gear_1, (m.WIDTH * 0.4, m.HEIGHT * 0.5))
#             m.SCREEN.blit(red_gear_1, (m.WIDTH * 0.46, m.HEIGHT * 0.5))
#             m.SCREEN.blit(red_gear_1, (m.WIDTH * 0.43, m.HEIGHT * 0.43))
#             m.SCREEN.blit(red_gear_1, (m.WIDTH * 0.49, m.HEIGHT * 0.43))
#             red_gear_teller +=1 
#             delay = 0
#         elif red_gear_teller == 2 and delay >= animation:
#             m.SCREEN.blit(black_background, (0, 0))
#             info_text.display()
#             m.SCREEN.blit(red_gear_2, (m.WIDTH * 0.4, m.HEIGHT * 0.5))
#             m.SCREEN.blit(red_gear_2, (m.WIDTH * 0.46, m.HEIGHT * 0.5))
#             m.SCREEN.blit(red_gear_2, (m.WIDTH * 0.43, m.HEIGHT * 0.43))
#             m.SCREEN.blit(red_gear_2, (m.WIDTH * 0.49, m.HEIGHT * 0.43))
#             red_gear_teller +=1
#             delay = 0
#         elif red_gear_teller == 3 and delay >= animation:
#             m.SCREEN.blit(black_background, (0, 0))
#             info_text.display()
#             m.SCREEN.blit(red_gear_3, (m.WIDTH * 0.4, m.HEIGHT * 0.5))
#             m.SCREEN.blit(red_gear_3, (m.WIDTH * 0.46, m.HEIGHT * 0.5))
#             m.SCREEN.blit(red_gear_3, (m.WIDTH * 0.43, m.HEIGHT * 0.43))
#             m.SCREEN.blit(red_gear_3, (m.WIDTH * 0.49, m.HEIGHT * 0.43))
#             red_gear_teller +=1
#             delay = 0
#         elif red_gear_teller == 4 and delay >= animation:
#             m.SCREEN.blit(black_background, (0, 0))
#             info_text.display()
#             m.SCREEN.blit(red_gear_4, (m.WIDTH * 0.4, m.HEIGHT * 0.5))
#             m.SCREEN.blit(red_gear_4, (m.WIDTH * 0.46, m.HEIGHT * 0.5))
#             m.SCREEN.blit(red_gear_4, (m.WIDTH * 0.43, m.HEIGHT * 0.43))
#             m.SCREEN.blit(red_gear_4, (m.WIDTH * 0.49, m.HEIGHT * 0.43))
#             red_gear_teller = 1
#             delay = 0

#         delay += 1

#         for event in m.pygame.event.get():

#             # when pressing the close button "X" at the top-right of the game-window
#             # or the escape button on the keyboard
#             if event.type == m.pygame.QUIT or (
#                 event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE
#             ):
#                 m.pygame.quit()

#             if event.type == m.pygame.MOUSEBUTTONDOWN:
#                 return

#         # the window should be updated after each while-loop
#         m.pygame.display.update()

###########################################################################################
def games_window(
    game_number,
    game_instructions,
    game_code,
    game_tip_1=None,
    game_tip_2=None,
    game_tip_1_image=None,
    game_tip_2_image=None,
    game_tip_3_image=None,
    game_tip_4_image=None,
):


    push_button_to_start(game_number)
    if game_number != 6:
        return game_started(
            game_number,
            game_instructions,
            game_code,
            game_tip_1,
            game_tip_2,
            game_tip_1_image,
            game_tip_2_image,
            game_tip_3_image,
            game_tip_4_image,
        )
    else:
        return_value = game_started(
            game_number,
            game_instructions,
            game_code,
            game_tip_1,
            game_tip_2,
            game_tip_1_image,
            game_tip_2_image,
            game_tip_3_image,
            game_tip_4_image,
        )
        if return_value != 1:
            push_button_to_start(game_number + 1)
        return return_value
