import main as m
from constants import *
import pygame
from widgets.button import Button
import widgets.button as b
import widgets.text_frame as t
import widgets.quit_game as q
from arduino.arduino_control import *
from widgets.instruction_box import Instruction_Box
from arduino.write_to_arduino import *

#######################################################################################

def end_game_instruction():
    explanation_text = Instruction_Box(m.transparent_box, 1000,
                              450, m.end_game_instruction_text, m.green_color, m.WIDTH/18, m.HEIGHT/15, m.MagdaClean_font_50)
   
    # create title object that will be displayed on the screen
    title = m.MagdaClean_font_70.render("Eindspel" , True, m.green_color)


    start_button = Button(m.small_green_button, m.small_green_button,
                          m.small_green_button, m.WIDTH / 1.2, m.HEIGHT / 1.07, 50, 50)
    start_text = m.MagdaClean_font_30.render('Start', True, m.green_color)

    logo_button = b.Button(
        m.museum_logo_grey,
        m.museum_logo_grey,
        m.museum_logo_grey,
        m.WIDTH - (m.WIDTH / 10 - 3) ,
        m.HEIGHT - (m.HEIGHT / 15 + 1),
        m.WIDTH / 10.5,
        m.HEIGHT / 22,
    )
    logo_button_pressed = False
    restart_timer = 0

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:
        if restart_timer >= m.restart_time_logo_pressed:
            if m.admin_mode() == 1:
                return 1
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
        logo_button.display()
        if logo_button_pressed and logo_button.mouse_on_button():
            restart_timer += 1
            # print ("pressed")
        else:
            logo_button_pressed = False
            restart_timer = 0

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            q.quit_game(event)

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN and start_button.mouse_on_button():
                m.SCREEN.blit(black_screen_background, (0, 0))
                m.correct_answer_sound.play()
                return
            if event.type == m.pygame.MOUSEBUTTONDOWN:

                if logo_button.mouse_on_button():
                        logo_button_pressed = True

        # the window should be updated after each while-loop
        m.pygame.display.update()


