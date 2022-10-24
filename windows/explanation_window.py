import pygame
import main as m
from widgets.instruction_box import Instruction_Box
import widgets.button as b

#######################################################################################


def explanation_window():

    message = Instruction_Box(m.instruction_box, 1000,
                              450, m.text_2, m.black_color, 200, 175)

    # background music
    # m.intro_sound.play()
    # m.pygame.mixer.music.load("Assets/sounds/start.wav")
    # m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(m.background_gears, (0, 0))
        message.display()

        # display yellow title bar
        m.SCREEN.blit(m.yellowbar, (0, 30))
        title1 = m.speelklok_website_font.render(
            'Spelregels', True, m.black_color)
        text_rect_title1 = title1.get_rect(
            center=(m.WIDTH/2, (m.HEIGHT/2)-255))
        m.SCREEN.blit(title1, text_rect_title1)

        # display logo
        m.SCREEN.blit(m.ms_logo, (1400-130, 700-46))

        # display button
        vbutton = b.Button(m.button_verder, m.button_verder,
                           m.button_verder_small, m.WIDTH//2, (m.HEIGHT//2)+225)
        vbutton.display()
        if vbutton.pressed_button() == True:
            vbutton.display_click_animation()
            vbutton.display()
            m.click_sound.play()
            pygame.time.delay(250)
            return

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.QUIT:
                m.pygame.quit()

            # when pressing a mouse button
            # if event.type == m.pygame.MOUSEBUTTONDOWN:
            #     m.correct_answer_sound.play()
                # return

        # the window should be updated after each while-loop
        m.pygame.display.update()
