# this is for high score printing
#high_score_screen
import main as m
from constants import *
from windows.save_data import save_data
import pygame
from widgets.instruction_box import Instruction_Box
from widgets.button import Button
import widgets.button as b
import widgets.text_frame as t

def read_file(current_team_name, current_team_time):
    with open("Assets/texts/highscore.txt", "r") as f: 
        contents = f.read() 
        i =0
        # print(contents + str(i))
        i+=1
    
    team = ''
    team_s = []
    team_name = ""
    team_score = 0
    teams_info = []
    for x in contents:

    #print(len(contents))    
    # while (x<len(contents)):
        # print (x)
        # team = team + x
        # print (team)
        if (x !='\n'):
            team = team + x
        elif (x =='\n' and team != None):
            team_s.append(team)
            # print (team + str(1))
            team = ""
    

    for o in team_s:
        if len(str(o))>1:
            team_info = []
            ty = o.split(" ")
            team_score = int(ty[0])
            team_name = str(ty[1])
            team_info.append(team_score)
            team_info.append(team_name)
            teams_info.append(team_info)
            ty.clear()
        # print ("team score is: " + str (team_score) + " " +  str (team_score + 1))
        # print ("team name is: " + team_name)
    
    tema_extra = []
    # del team_info[1]
    # del team_info[0]
    tema_extra.append(int(current_team_time))
    tema_extra.append(str(current_team_name))
    teams_info.append(tema_extra)

    teams_info = sort_high_score(teams_info)
    # print (teams_info[0][0])
    print (teams_info)
    write_file(teams_info)

def write_file(self):
    # write to the folder
    print ("self is" )
    print (self)
    if (len(self)>10):
        del self[0]
    
    temp = ""
    for x in self:
        temp = temp + str(x[0]) + " " + x[1] + "\n" + '\n' + '\n'
    
    with open("Assets/texts/highscore.txt", 'w') as f:
        f.write (temp )
        # f.write('\n')
        # f.write('\n')

    print (" from write functione: " + temp)
    
def sort_high_score(self):
    o = 0
    x = 0
    while x<len(self):
        while o<len(self)-1:
            if self[o][0]>self[o+1][0]:
                temp = self[o][0]
                self[o][0] = self[o+1][0]
                self[o+1][0] = temp
            o+=1
        x+=1
    return self

