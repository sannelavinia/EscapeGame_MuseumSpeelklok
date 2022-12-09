import main as m
from constants import *
from windows.save_data import save_data
import pygame
from widgets.instruction_box import Instruction_Box
from widgets.button import Button
import widgets.quit_game as q
import widgets.button as b
import widgets.text_frame as t
from arduino.arduino_control import *


#######################################################################################
def end_window():
    arduino("aStatus=8\n")

    # the end time
    milliseconds = m.TOTAL_PLAY_TIME % 1000
    seconds = int((m.TOTAL_PLAY_TIME / 1000) % 60)
    minutes = int(((m.TOTAL_PLAY_TIME / 1000) / 60) % 60)
    hours = int((((m.TOTAL_PLAY_TIME / 1000) / 60) / 60) % 60)
    time_end = "{:<2}:{:<2}:{:<2}:{:<5}".format(
        str(hours).zfill(2),
        str(minutes).zfill(2),
        str(seconds).zfill(2),
        str(milliseconds).zfill(3),
    )

    team_name = save_data.team_name_save

    text_1 = t.Text_frame(
        None,
        None,
        None,
        "Gefeliciteerd " + team_name,
        m.green_color,
        m.MagdaClean_font_50,
        m.WIDTH / 2,
        m.HEIGHT / 7,
    )
    text_3 = t.Text_frame(
        None,
        None,
        None,
        "Jullie eindtijd is: " + time_end,
        m.green_color,
        m.MagdaClean_font_50,
        m.WIDTH / 2,
        (m.HEIGHT / 7) * 2,
    )
    text_4 = t.Text_frame(
        None,
        None,
        None,
        "Bedankt voor jullie hulp!, we zijn weer in onze eigen tijd beland! ",
        m.green_color,
        m.MagdaClean_font_50,
        m.WIDTH / 2,
        (m.HEIGHT / 7) * 3,
    )
    text_2 = t.Text_frame(
        None,
        None,
        None,
        "Dat was een wilde maar gave rit zeg! Woohoo! ",
        m.green_color,
        m.MagdaClean_font_50,
        m.WIDTH / 2,
        (m.HEIGHT / 7) * 4,
    )

    print("the time until now is: " + time_end)

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        celebration_background = pygame.transform.scale(
            m.celebration_background, (m.WIDTH, m.HEIGHT)
        )
        m.SCREEN.blit(celebration_background, (0, 0))

        # This should be a button eventually
        m.SCREEN.blit(m.museum_logo_grey, (m.WIDTH / 1.17, m.HEIGHT / 1.10))

        # message.display()

        text_1.display()
        text_3.display()
        text_4.display()
        text_2.display()

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            q.quit_game(event)

            if event.type == m.pygame.MOUSEBUTTONDOWN:
                return

        # the window should be updated after each while-loop
        m.pygame.display.update()
