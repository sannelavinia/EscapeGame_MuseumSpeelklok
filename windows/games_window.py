import main as m
import widgets.keyboard as k
import widgets.text_frame as t
import widgets.button as b
import widgets.instruction_box as i
import windows.start_window as sw


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
        "Gefeliciteerd! Je hebt alle",
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
def game_started(game_number, game_instructions, game_code):

    # resizing the images
    background_games_template = m.pygame.transform.scale(
        m.background_games_template, (m.WIDTH, m.HEIGHT)
    )

    timer_bachground = m.pygame.transform.scale(m.black_screen_background, (390, 200))

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
        (m.WIDTH * 4 / 6) + 36,
        (m.HEIGHT / 2) + 30,
        game_instructions,
        m.green_color,
        0,
        (m.HEIGHT / 6) + 18,
        m.MagdaClean_font_30,
        40,
        60,
        50,
    )

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

    tip_message = i.Instruction_Box(
        m.instruction_screen_games,
        (m.WIDTH * 4 / 6) + 36,
        (m.HEIGHT / 2) + 30,
        m.text_2,
        m.green_color,
        0,
        (m.HEIGHT / 6) + 18,
        m.MagdaClean_font_30,
        40,
        60,
        50,
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

    # for speeding up
    displayed = False
    button_pushed = True
    tip_message_1_displayed = False
    tip_message_2_displayed = False
    tip_button_displayed = 0

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        if restart_timer >= 30:
            return 1

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
        if button_pushed or tip_button_displayed == 1:
            keyboard.display()
            tip_button.display()
            button_pushed = False
            if tip_button_displayed == 1:
                tip_button_displayed = 2

        # display the timer
        m.SCREEN.blit(timer_bachground, (0, 0))
        play_time_as_text.display()

        # display the tip message
        if display_tip_message_1:
            tip_message.display()
            display_tip_message_1 = False
            tip_message_1_displayed = True
        if display_tip_message_2:
            # here display the second tip
            m.correct_answer_sound.play()
            tip_message_2_displayed = True
            display_tip_message_2 = False

        # tik-sound every second
        if play_time_seconds != previous_second:
            previous_second = play_time_seconds
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
        if timer >= int(m.button_resizing_delay / 3):

            if pressed_button != 12:
                # to the next window (if the code was correct)
                if pressed_button == 10:
                    if code == game_code:
                        m.correct_answer_sound.play()
                        m.TOTAL_PLAY_TIME += time_difference
                        sw.corret_code()
                        return
                    else:
                        code = keyboard.keyboard_button_pressed(
                            pressed_button, code, m.red_color
                        )
                        m.wrong_answer_sound.play()
                else:
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
                button_pushed = True

                if pressed_button in range(0, 12):
                    button_pressed = True

                if tip_button.mouse_on_button() and start_display_tip_icon:
                    tip_button.display_click_animation()
                    button_pressed = True
                    pressed_button = 12
                    if tip_message_1_displayed:
                        if tip_message_2_displayed:
                            displayed = False
                            tip_message_1_displayed = False
                            tip_message_2_displayed = False
                        else:
                            display_tip_message_2 = True
                    else:
                        display_tip_message_1 = True

                if logo_button.mouse_on_button():
                    logo_button_pressed = True

        if time_difference <= m.game_normal_time:
            play_time_as_text.change_input_text(
                m.from_millisecond_to_clock(play_time), m.green_color
            )
        else:
            play_time_as_text.change_input_text(
                m.from_millisecond_to_clock(play_time), m.red_color
            )
            if tip_button_displayed == 0:
                tip_button_displayed = 1
                start_display_tip_icon = True

                # # to display the yellow tip image ( instead of the grey one )
                # if not tip_button_to_yellow:
                tip_button_to_yellow = True
                tip_button.restore_normal_size()

        # the window should be updated after each while-loop
        m.pygame.display.update()


#######################################################################################
def games_window(game_number, game_instructions, game_code):

    push_button_to_start(game_number)
    if game_number != 6:
        return game_started(game_number, game_instructions, game_code)
    else:
        return_value = game_started(game_number, game_instructions, game_code)
        if return_value != 1:
            push_button_to_start(game_number + 1)
        return return_value
