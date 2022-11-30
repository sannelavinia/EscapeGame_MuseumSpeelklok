import main as m
from arduino.arduino_control import *
from open_the_project import *
import pygame

#######################################################################################
def end_game():
    arduino("activeGame=0")
    arduino("activeMachine=4")

    start_time = m.pygame.time.get_ticks()
    open_end_game()

    end_time = m.pygame.time.get_ticks()
    time_difference = end_time - start_time
    play_time = m.TOTAL_PLAY_TIME + time_difference
    play_time_seconds = int((play_time / 1000) % 60)

    # game loop ( to prevent the window from closing after going throw the current events )
    pygame.time.wait(5000)
    return

