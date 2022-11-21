import main as m
import widgets.keyboard as k


def admin_mode():
    keyboard = k.Keyboard((m.WIDTH/2)-(m.button_width),
                          (m.HEIGHT/2)-(m.button_width))
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0  # used for animating the buttons

    while True:

        m.SCREEN.fill(m.black_color)
        keyboard.display()

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

        # resize the clicked button
        if timer >= m.button_resizing_delay:

            # to the next window (if the code was correct)
            if pressed_button == 10:
                if code == m.admin_code:
                    m.correct_answer_sound.play()
                    return
                else:
                    m.wrong_answer_sound.play()
            else:
                m.click_sound.play()
            code = keyboard.keyboard_button_pressed(pressed_button, code)

            # reset
            keyboard.resize_buttons()
            button_pressed = False
            pressed_button = 99
            timer = 0

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
        # the window should be updated after each while-loop
        m.pygame.display.update()
