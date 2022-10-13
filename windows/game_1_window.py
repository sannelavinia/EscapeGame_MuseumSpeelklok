import imp
from tkinter.messagebox import NO
import pygame
import main as m
import widgets.keyboard as k
from widgets.massage_box import Massage_box
from widgets.code_frame import Text_frame
import widgets.button as b


#######################################################################################
def game_1_window():

    # massage = Massage_box(m.message, 400, 300,
    #                       m.game_1_explanation, m.black_color, 100, 300)
    title = Text_frame(None, "Spel 1", m.black_color,
                       m.speelklok_website_font, m.WIDTH/2, (m.HIGHT/2)-255)

    instruction_box = pygame.transform.scale(m.instruction_box, (500, 400))

    instruction_box = Text_frame(instruction_box, "", m.black_color,
                                 m.code_font, m.WIDTH/3, m.HIGHT*3/5)

    instruction_title = Text_frame(None, "Instructies", m.black_color,
                                   m.code_font, 500, 300)

    # logo_button = b.Button(m.ms_logo, m.ms_logo,
    #                        m.ms_logo, m.WIDTH-75, m.HIGHT-25)

    # background music
    m.pygame.mixer.music.load("Assets/sounds/game_1.wav")
    m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    keyboard = k.Keyboard(m.WIDTH*2/3, 300)  # the input keyboard
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0  # used for animating the buttons

    play_time = 0

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(m.background_gears, (0, 0))
        m.SCREEN.blit(m.yellowbar, (0, 30))     # display yellow title bar
        title.display()
        instruction_box.display()
        instruction_title.display()
        # massage.display()
        keyboard.display()
        # logo_button.display()

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
            keyboard.text_frame.change_input_text(code, m.white_color)
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
