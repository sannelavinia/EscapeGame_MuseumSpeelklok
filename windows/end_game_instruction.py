import main as m
from constants import *
import pygame
from widgets.button import Button
import widgets.button as b
import widgets.text_frame as t
import widgets.quit_game as q
from arduino.arduino_control import *
from widgets.instruction_box import Instruction_Box

#######################################################################################

def end_game_instruction():
    arduino("activeMachine=3&activeGame=0\n")

    explanation_text = Instruction_Box(m.transparent_box, 1000,
                              450, m.end_game_instruction_text, m.green_color, m.WIDTH/18, m.HEIGHT/15, m.MagdaClean_font_50)
   
    # create title object that will be displayed on the screen
    title = m.MagdaClean_font_70.render("Eindspel" , True, m.green_color)


    start_button = Button(m.small_green_button, m.small_green_button,
                          m.small_green_button, m.WIDTH / 1.2, m.HEIGHT / 1.07, 50, 50)
    start_text = m.MagdaClean_font_30.render('Start', True, m.green_color)

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        black_screen_background = pygame.transform.scale(
            m.black_screen_background, (m.WIDTH, m.HEIGHT))
        m.SCREEN.blit(black_screen_background, (0, 0))

        # This should be a button eventually
        m.SCREEN.blit(m.museum_logo_grey, (m.WIDTH/1.17, m.HEIGHT/1.10))
        # m.SCREEN.blit(title, (m.WIDTH/2, m.HEIGHT/2))

        # message.display()

        start_button.display()
        explanation_text.display()
        m.SCREEN.blit(start_text, (m.WIDTH/1.3, m.HEIGHT/1.08))

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            q.quit_game(event)

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN and start_button.mouse_on_button():
                m.correct_answer_sound.play()
                return

        # the window should be updated after each while-loop
        m.pygame.display.update()


