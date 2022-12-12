import main as m
from constants import *
from windows.save_data import save_data
import pygame
from widgets.instruction_box import Instruction_Box
from widgets.button import Button
import widgets.button as b
import widgets.text_frame as t
from windows.print_high_score import *


#######################################################################################
def high_score():
    

    # the end time
    milliseconds = m.TOTAL_PLAY_TIME % 1000
    seconds = int((m.TOTAL_PLAY_TIME ) / 1000)
    minutes = int(((m.TOTAL_PLAY_TIME / 1000) / 60) % 60)
    hours = int((((m.TOTAL_PLAY_TIME / 1000) / 60) / 60) % 60)
    time_end = "{:<2}:{:<2}:{:<2}:{:<5}".format(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2), str(milliseconds).zfill(3))

    team_name = save_data.team_name_save
    read_file(str(team_name), int(seconds))

    text_1 = t.Text_frame(
        None, None, None, "High scores ", m.green_color, m.MagdaClean_font_70, m.WIDTH/2.5, m.HEIGHT/7)
    text_3 = t.Text_frame(
        None, None, None, "Tijd in seconden     Naam " , m.green_color, m.MagdaClean_font_50, m.WIDTH/2.5, (m.HEIGHT/7)*2)
    # text_4 = t.Text_frame(
    #      None, None, None, "Bedankt voor jullie hulp!, we zijn weer in onze eigen tijd beland! "  , m.green_color, m.MagdaClean_font_50, m.WIDTH/2, (m.HEIGHT/7)*3)
    # text_2 = t.Text_frame(
    #      None, None, None, "Dat was een wilde maar gave rit zeg! Woohoo! "  , m.green_color, m.MagdaClean_font_50, m.WIDTH/2,  (m.HEIGHT/7)*4)
    
    # print ("the time until now is: " + time_end)
    
    text_file = open("Assets/texts/highscore.txt", "r")
    high_score_1 = text_file.read().split("\n")
    explanation_text = Instruction_Box(m.transparent_box, 1000,
                                450, high_score_1, m.green_color, m.WIDTH/9, (m.HEIGHT/7), m.MagdaClean_font_50)
    
   
    # create title object that will be displayed on the screen

    # if len(o) < 10:
    #title = m.MagdaClean_font_70.render("De teamname is " + team_name + "\n en het kost " + time_end + "om het spel te eindigen", True, m.green_color)


    # start_button = Button(m.small_green_button, m.small_green_button,
    #                       m.small_green_button, m.WIDTH / 1.2, m.HEIGHT / 1.07, 50, 50)
    # start_text = m.MagdaClean_font_30.render('End', True, m.green_color)

    start_time = m.pygame.time.get_ticks()
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

        # restart the game after a 5 min (no action needed)
        if m.pygame.time.get_ticks() > start_time + m.restart_time_end_window:
            return

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        celebration_background = pygame.transform.scale(
            m.celebration_background, (m.WIDTH, m.HEIGHT))
        m.SCREEN.blit(celebration_background, (0, 0))

        # This should be a button eventually
        m.SCREEN.blit(m.museum_logo_grey, (m.WIDTH/1.17, m.HEIGHT/1.10))
        # m.SCREEN.blit(title, (m.WIDTH/2, m.HEIGHT/2))

        # message.display()

        # start_button.display()
        text_1.display()
        text_3.display()
        # text_4.display()
        # text_2.display()
        explanation_text.display()
        logo_button.display()
        if logo_button_pressed and logo_button.mouse_on_button():
            restart_timer += 1
            # print ("pressed")
        else:
            logo_button_pressed = False
            restart_timer = 0
        # m.SCREEN.blit(explanation_text, (m.WIDTH/2, m.HEIGHT/1.08))

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.MOUSEBUTTONDOWN:

                if logo_button.mouse_on_button():
                        logo_button_pressed = True
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.quit()


            # when pressing a mouse button
            # if event.type == m.pygame.MOUSEBUTTONDOWN and start_button.mouse_on_button():
            #     m.correct_answer_sound.play()
            #     return

        # the window should be updated after each while-loop
        m.pygame.display.update()


