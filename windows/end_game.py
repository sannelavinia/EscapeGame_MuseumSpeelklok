import main as m
from arduino.arduino_control import *
from open_the_project import *
import pygame
# import subprocess
import psutil

#######################################################################################
def end_game():
    arduino("activeMachine=4&activeGame=0\n")

    start_time = m.pygame.time.get_ticks()

    open_end_game()
    closed = False
    while closed==False:
        counter = 0
        for p in psutil.process_iter(attrs=['pid', 'name']):            
            if "my project (1).exe" in (p.info['name']).lower():
                counter += 1
        if counter==0:

            closed=True

    end_time = m.pygame.time.get_ticks()
    time_difference = end_time - start_time
    play_time = m.TOTAL_PLAY_TIME + time_difference
    play_time_seconds = int((play_time / 1000) % 60)

    return

