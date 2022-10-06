import main as m
import widgets.keyboard as k


#######################################################################################
def game_4_window():

    # background music
    m.pygame.mixer.music.load("Assets/sounds/game_4.wav")
    m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    keyboard = k.Keyboard(1100, 300)  # the input keyboard
    keyboard_x = 1100
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0  # used for animating the buttons

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(m.background_game_4, (0, 0))
        if(keyboard_x < 1100):
            keyboard_x += 2
            keyboard.move_to(keyboard_x, 300)
        keyboard.display()

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

        # resize the clicked button
        if timer >= m.button_resizing_delay:
            # to the next window (if the code was correct)
            if pressed_button == 10:
                if code == m.game_4_code:
                    m.correct_answer_sound.play()
                    return
                else:
                    m.wrong_answer_sound.play()
            else:
                m.click_sound.play()
            code = m.keyboard_button_pressed(pressed_button, code)
            keyboard.text_frame.change_input_text(code)
            # reset
            keyboard.resize_buttons()
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

        # the window should be updated after each while-loop
        m.pygame.display.update()
