import pygame
import main as m
import widgets.keyboard as k
from widgets.massage_box import Massage_box


#######################################################################################
def game_1_window():

    # text, message_box = m.render_text(m.text_2, m.black_color, 400, 300)

    massage = Massage_box(m.message, 400, 300,
                          m.game_1_explanation, m.black_color, 100, 300)

    # background music
    m.pygame.mixer.music.load("Assets/sounds/game_1.wav")
    m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    keyboard = k.Keyboard(600, 300)  # the input keyboard
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0  # used for animating the buttons

    play_time = 0

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(m.background_game_1, (0, 0))
        massage.display()
        keyboard.display()

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

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

        play_time = pygame.time.get_ticks()

        # the window should be updated after each while-loop
        m.pygame.display.update()
