import main as m
import widgets.keyboard as k
import widgets.text_frame as t
import widgets.button as b
import widgets.instruction_box as i


#######################################################################################
def push_button_to_start(game_number):

    # resizing the images
    metal_plate_empty = m.pygame.transform.scale(
        m.metal_plate_empty, (m.WIDTH/2, m.HEIGHT))
    single_screw = m.pygame.transform.scale(
        m.single_screw, (m.WIDTH/20, m.WIDTH/20))

    # text variables
    text_line_1 = t.Text_frame(
        None, None, None, "Klik op de knop om", m.black_color, m.code_font, m.WIDTH/4, (m.HEIGHT/2)-50)
    text_line_2 = t.Text_frame(
        None, None, None, f"spel {game_number} ", m.white_color, m.code_font, m.WIDTH/4, m.HEIGHT/2)
    text_line_3 = t.Text_frame(
        None, None, None, "te starten", m.black_color, m.code_font, m.WIDTH/4, (m.HEIGHT/2)+50)
    text_button_start = t.Text_frame(
        None, None, None, "START", m.white_color, m.code_font, m.WIDTH*3/4, m.HEIGHT/2)

    # start button
    green_start_button = b.Button(m.green_start_button, m.green_start_button,
                                  m.green_start_button_pushed, m.WIDTH*3/4, m.HEIGHT/2, m.WIDTH/4, m.WIDTH/4)

    button_pressed = False
    timer = 0  # used for animating the buttons

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(metal_plate_empty, (0, 0))
        m.SCREEN.blit(metal_plate_empty, (m.WIDTH/2, 0))

        # display the screws
        m.SCREEN.blit(single_screw, (m.WIDTH/40, m.HEIGHT/20))
        m.SCREEN.blit(single_screw, (m.WIDTH/2-(m.WIDTH/40) -
                      (m.WIDTH/20), m.HEIGHT/20))
        m.SCREEN.blit(single_screw, (m.WIDTH/2+(m.WIDTH/40), m.HEIGHT/20))
        m.SCREEN.blit(single_screw, (m.WIDTH-(m.WIDTH/40) -
                      (m.WIDTH/20), m.HEIGHT/20))
        m.SCREEN.blit(single_screw, (m.WIDTH/40, m.HEIGHT-(m.HEIGHT/20) -
                      (m.WIDTH/20)))
        m.SCREEN.blit(single_screw, (m.WIDTH/2-(m.WIDTH/40) -
                      (m.WIDTH/20), m.HEIGHT-(m.HEIGHT/20) -
                      (m.WIDTH/20)))
        m.SCREEN.blit(single_screw, (m.WIDTH/2+(m.WIDTH/40), m.HEIGHT-(m.HEIGHT/20) -
                      (m.WIDTH/20)))
        m.SCREEN.blit(single_screw, (m.WIDTH-(m.WIDTH/40) -
                      (m.WIDTH/20), m.HEIGHT-(m.HEIGHT/20) -
                      (m.WIDTH/20)))

        # display the text
        text_line_1.display()
        text_line_2.display()
        text_line_3.display()

        # display the button
        green_start_button.display()
        text_button_start.display()

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

        # resize the clicked button
        if timer >= m.button_resizing_delay:
            return

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            # or the escape button on the keyboard
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.quit()

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN:

                if green_start_button.mouse_on_button():
                    green_start_button.display_click_animation()
                    button_pressed = True

        # the window should be updated after each while-loop
        m.pygame.display.update()


#######################################################################################
def game_started(game_number, game_instructions):

    # resizing the images
    background_games_template = m.pygame.transform.scale(
        m.background_games_template, (m.WIDTH, m.HEIGHT))

    title = t.Text_frame(None, None, None, f"SPEL {game_number}", m.white_color,
                         m.speelklok_website_font, m.WIDTH*5/8, m.HEIGHT/11)

    instruction_title = t.Text_frame(None, None, None, "Instructies", m.green_color,
                                     m.code_font, 500, 250)
    instruction_box = i.Instruction_Box(
        m.instruction_screen_games, (m.WIDTH*4/6)+36, (m.HEIGHT/2)+30, game_instructions, m.green_color, 0, (m.HEIGHT/6)+18)

    logo_button = b.Button(m.museum_logo_grey, m.museum_logo_grey,
                           m.museum_logo_grey, m.WIDTH-(m.WIDTH/6.7), m.HEIGHT-(m.HEIGHT/12.55), m.WIDTH/6.75, m.HEIGHT/12.5)

    tip_button = b.Button(m.tip_button_grey, m.tip_button,
                          m.tip_button_pushed, (m.HEIGHT/8)+10, (m.HEIGHT-m.HEIGHT/8)-10, m.HEIGHT/4, m.HEIGHT/4)

    # tip_message_box = t(
    #     m.tip_message_box, 100, 200, "", m.black_color, m.main_font, 100, m.HEIGHT - 120)

    # tip_message = t(None, None, None, "hint!", m.black_color,
    #                          m.main_font, 150, m.HEIGHT - 130)

    # # background music
    # m.pygame.mixer.music.load("Assets/sounds/game_1.wav")
    # m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    keyboard = k.Keyboard(m.WIDTH - 350, 350)  # the input keyboard
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0  # used for animating the buttons
    start_display_tip_icon = False
    tip_button_to_yellow = False
    start_display_tip_message = False
    logo_button_pressed = False
    restart_timer = 0

    start_time = m.pygame.time.get_ticks()
    time_difference = 0
    previous_second = int((m.TOTAL_PLAY_TIME / 1000) % 60)
    play_time_as_text = t.Text_frame(None, None, None, m.from_millisecond_to_clock(
        m.TOTAL_PLAY_TIME), m.green_color, m.code_font, m.WIDTH/9, m.HEIGHT/11)

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        if restart_timer >= 30:
            return 1

        time_difference = m.pygame.time.get_ticks()-start_time
        play_time = m.TOTAL_PLAY_TIME + time_difference
        play_time_seconds = int((play_time / 1000) % 60)

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(background_games_template, (0, 0))

        play_time_as_text.display()
        title.display()
        instruction_box.display()
        instruction_title.display()
        keyboard.display()
        tip_button.display()
        logo_button.display()

        # if start_display_tip_icon:

        # if start_display_tip_message:
        #     tip_message_box.display()
        #     tip_message.display()

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

            # reset
            keyboard.resize_buttons()
            if tip_button_to_yellow:
                tip_button.restore_normal_size()
            button_pressed = False
            pressed_button = 99
            timer = 0

            # to the next window (if the code was correct)
            if pressed_button == 10:
                if code == m.game_1_code:
                    m.correct_answer_sound.play()
                    m.TOTAL_PLAY_TIME += time_difference
                    return
                else:
                    m.wrong_answer_sound.play()
            else:
                m.click_sound.play()
            code = keyboard.keyboard_button_pressed(pressed_button, code)

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            # or the escape button on the keyboard
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.quit()

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN:
                pressed_button = keyboard.pressed_button()

                if pressed_button in range(0, 12):
                    button_pressed = True
                if tip_button.mouse_on_button() and start_display_tip_icon:
                    tip_button.display_click_animation()
                    button_pressed = True
                    # start_display_tip_message = True
                if logo_button.mouse_on_button():
                    logo_button_pressed = True

        if time_difference <= m.game_normal_time:
            play_time_as_text.change_input_text(m.from_millisecond_to_clock(
                play_time), m.green_color)
        else:
            play_time_as_text.change_input_text(m.from_millisecond_to_clock(
                play_time), m.red_color)
            start_display_tip_icon = True

            # to display the yellow tip image ( instead of the grey one )
            if not tip_button_to_yellow:
                tip_button_to_yellow = True
                tip_button.restore_normal_size()

        # the window should be updated after each while-loop
        m.pygame.display.update()


#######################################################################################
def games_window(game_number, game_instructions):

    # reset
    if game_number == 1:
        m.TOTAL_PLAY_TIME = 0

    push_button_to_start(game_number)
    return game_started(game_number, game_instructions)
