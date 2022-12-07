import main as m
import widgets.keyboard as k
import widgets.text_frame as t
import widgets.button as b
import widgets.quit_game as q

def admin_mode():

    # resizing the images
    background = m.pygame.transform.scale(
        m.black_screen_background, (m.WIDTH, m.HEIGHT)
    )

    # instructions displayed on the screen
    instruction_message_1 = t.Text_frame(
        None,
        None,
        None,
        "Dit scherm is alleen bedoeld voor het personeel in het museum..!!!",
        m.red_color,
        m.MagdaClean_font_50,
        m.WIDTH / 2,
        150,
    )
    instruction_message_2 = t.Text_frame(
        None,
        None,
        None,
        "U kunt teruggaan naar het spel door op TERUG te klikken",
        m.green_color,
        m.MagdaClean_font_50,
        m.WIDTH / 2,
        200,
    )
    instruction_message_3 = t.Text_frame(
        None,
        None,
        None,
        "De tijd blijft lopen! .. Snel TERUG!!",
        m.green_color,
        m.MagdaClean_font_50,
        m.WIDTH / 2,
        250,
    )

    # back button
    back_button = b.Button(
        m.green_start_button,
        m.green_start_button,
        m.green_start_button_pushed,
        m.WIDTH * 3 / 4,
        (m.HEIGHT / 2) + 100,
        m.WIDTH / 4,
        m.WIDTH / 4,
    )
    text_back_button = t.Text_frame(
        None,
        None,
        None,
        "TERUG",
        m.white_color,
        m.MagdaClean_font_70,
        m.WIDTH * 3 / 4,
        (m.HEIGHT / 2) + 100,
    )

    keyboard = k.Keyboard(m.WIDTH / 4, m.HEIGHT / 2)
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0  # used for animating the buttons

    # for speeding up
    button_pushed = True

    while True:

        if button_pushed:
            m.SCREEN.blit(background, (0, 0))
            instruction_message_1.display()
            instruction_message_2.display()
            instruction_message_3.display()
            keyboard.display()
            back_button.display()
            text_back_button.display()
            button_pushed = False

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

        # resize the clicked button
        if timer >= m.button_resizing_delay:

            # to the next window (if the code was correct)
            if pressed_button == 10:
                if code == m.admin_code:
                    m.correct_answer_sound.play()
                    return 1
                else:
                    code = keyboard.keyboard_button_pressed(
                        pressed_button, code, m.red_color
                    )
                    m.wrong_answer_sound.play()
            elif pressed_button == 12:
                return
            else:
                m.click_sound.play()
                code = keyboard.keyboard_button_pressed(pressed_button, code)

            # reset
            keyboard.resize_buttons()
            back_button.restore_normal_size()
            button_pressed = False
            button_pushed = True
            pressed_button = 99
            timer = 0

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            q.quit_game(event)

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN:
                pressed_button = keyboard.pressed_button()

                if pressed_button in range(0, 12):
                    button_pressed = True
                    button_pushed = True

                if back_button.mouse_on_button():
                    back_button.display_click_animation()
                    pressed_button = 12
                    button_pressed = True
                    button_pushed = True

        # the window should be updated after each while-loop
        m.pygame.display.update()
