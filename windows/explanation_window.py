import pygame
import main as m
from widgets.instruction_box import Instruction_Box
from widgets.button import Button
import widgets.button as b

#######################################################################################
# Might be useful to load this image in main.py instead of here
transparent_box = pygame.image.load("Assets/images/HD_transparent_picture.png")
transparent_box = pygame.transform.scale(transparent_box, (0, 0))


def explanation_window():
    message = Instruction_Box(transparent_box, 1000,
                              450, m.text_2, m.green_color, m.WIDTH/9500, m.HEIGHT/12, m.Consolas_font_30)

    # create title object that will be displayed on the screen
    title = m.Consolas_font_70.render('Speluitleg', True, m.green_color)

    start_button = Button(m.small_green_button, m.small_green_button,
                          m.small_green_button, m.WIDTH / 1.2, m.HEIGHT / 1.07, 50, 50)
    start_text = m.Consolas_font_30.render('Begin', True, m.green_color)

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        black_screen_background = pygame.transform.scale(
            m.black_screen_background, (m.WIDTH, m.HEIGHT))
        m.SCREEN.blit(black_screen_background, (0, 0))

        # This should be a button eventually
        m.SCREEN.blit(m.museum_logo_grey, (m.WIDTH/1.17, m.HEIGHT/1.10))
        m.SCREEN.blit(title, (m.WIDTH/35, m.HEIGHT/50))

        message.display()

        start_button.display()
        m.SCREEN.blit(start_text, (m.WIDTH/1.3, m.HEIGHT/1.08))

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.quit()

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN and start_button.mouse_on_button():
                m.correct_answer_sound.play()
                return

        # the window should be updated after each while-loop
        m.pygame.display.update()
