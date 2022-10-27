import pygame       # is a 2D-grafic liberary
from widgets.keyboard import *
from widgets.text_frame import *
from constants import *
from widgets.button import *
from windows.start_window import *
from windows.explanation_window import *
from windows.games_window import *
from windows.end_window import *
from windows.admin_mode import *
from windows.teamname_window import team_name_window


# initializing the pygame ( preventing unexpected behavior )
pygame.init()

# global variables
HEIGHT = pygame.display.Info().current_h     # height of the displayed window
WIDTH = pygame.display.Info().current_w     # width of the displayed window
TEAMS_NAMES = ["11", "22", "33", "44", "55"]
TEAMS_SCORES = ["11", "22", "33", "44", "55"]

########################### load Assets ###########################

pygame.display.set_caption("Speelklok")  # title of the window
ICON = pygame.image.load("Assets/images/saxophone.png")  # icon of the game
pygame.display.set_icon(ICON)

#############################################################################################
################################# ( te verwijderen ) ########################################
#############################################################################################
# images
background_start = pygame.image.load("Assets/images/background_start.jpg")
background_start = pygame.transform.scale(background_start, (WIDTH, HEIGHT))
background_game_1 = pygame.image.load("Assets/images/background_game_1.jpg")
background_game_1 = pygame.transform.scale(background_game_1, (WIDTH, HEIGHT))
background_game_2 = pygame.image.load("Assets/images/background_game_2.jpg")
background_game_2 = pygame.transform.scale(background_game_2, (WIDTH, HEIGHT))
background_game_3 = pygame.image.load("Assets/images/background_game_3.jpg")
background_game_3 = pygame.transform.scale(background_game_3, (WIDTH, HEIGHT))
background_game_4 = pygame.image.load("Assets/images/background_game_4.jpg")
background_game_4 = pygame.transform.scale(background_game_4, (WIDTH, HEIGHT))
background_game_5 = pygame.image.load("Assets/images/background_game_5.jpg")
background_game_5 = pygame.transform.scale(background_game_5, (WIDTH, HEIGHT))
background_game_6 = pygame.image.load("Assets/images/background_game_6.jpg")
background_game_6 = pygame.transform.scale(background_game_6, (WIDTH, HEIGHT))
background_end = pygame.image.load("Assets/images/background_end.jpg")
background_end = pygame.transform.scale(background_end, (WIDTH, HEIGHT))
background_gears = pygame.image.load("Assets/images/background_gearsv1.jpg")
background_gears = pygame.transform.scale(background_gears, (WIDTH, HEIGHT))
yellowbar = pygame.image.load("Assets/images/yellowbar.jpg")
yellowbar = pygame.transform.scale(yellowbar, (1400, 120))

message = pygame.image.load("Assets/images/message.png")
instruction_box = pygame.image.load("Assets/images/instructions_text_box.png")
tip_message_box = pygame.image.load("Assets/images/tip_message_box.png")

# buttons
button_verder = pygame.image.load("Assets/images/button_verder.jpg")
button_verder = pygame.transform.scale(button_verder, (166, 45))
button_verder_small = pygame.transform.scale(
    button_verder, (166 - 100, 45 - 10))

button_start = pygame.image.load("Assets/images/button_start.png")
button_start = pygame.transform.scale(button_start, (166, 45))
tip_button_small = pygame.image.load("Assets/images/tip_button.png")

# code frame
text_frame = pygame.image.load("Assets/images/frame.png")

#############################################################################################
################################# ( te gebruiken ) ##########################################
#############################################################################################
# images

# museum_logo
ms_logo = pygame.image.load("Assets/images/ms_logo.png")
ms_logo = pygame.transform.scale(ms_logo, (120, 36))
museum_logo_grey = pygame.image.load("Assets/images/museum_logo_grey.png")

# backgrounds
background_games_template = pygame.image.load(
    "Assets/images/background_games_template.png")
black_screen_background = pygame.image.load(
    "Assets/images/black_screen_background.png")

# frames
instruction_screen_games = pygame.image.load(
    "Assets/images/instruction_screen_games.png")
metal_plate_empty = pygame.image.load("Assets/images/metal_plate_empty.png")
metal_plate_infoboard = pygame.image.load(
    "Assets/images/metal_plate_infoboard.png")
metal_plate_museumlogo = pygame.image.load(
    "Assets/images/metal_plate_museumlogo.png")
white_input_field_teamname = pygame.image.load(
    "Assets/images/white_input_field_teamname.png")
code_input_frame = pygame.image.load("Assets/images/code_input_frame.png")

# gears
blue_gear = pygame.image.load("Assets/images/blue_gear.png")
orange_gear = pygame.image.load("Assets/images/orange_gear.png")
purple_gear = pygame.image.load("Assets/images/purple_gear.png")
red_gear = pygame.image.load("Assets/images/red_gear.png")
green_gear = pygame.image.load("Assets/images/green_gear.png")
yellow_gear = pygame.image.load("Assets/images/yellow_gear.png")
rings_for_gears = pygame.image.load("Assets/images/rings_for_gears.png")
rings_for_gears_with_gears = pygame.image.load(
    "Assets/images/rings_for_gears_with_gears.png")

single_screw = pygame.image.load("Assets/images/single_screw.png")

# buttons
green_start_button = pygame.image.load("Assets/images/green_start_button.png")
green_start_button_pushed = pygame.image.load(
    "Assets/images/green_start_button_pushed.png")
small_green_button = pygame.image.load("Assets/images/small_green_button.png")

tip_button = pygame.image.load("Assets/images/tip_button.png")
tip_button_grey = pygame.image.load("Assets/images/tip_button_grey.png")
tip_button_pushed = pygame.image.load("Assets/images/tip_button_pushed.png")

# keyboard buttons
number_0 = pygame.image.load("Assets/images/number_0.png")
number_0_after_click = pygame.image.load(
    "Assets/images/number_0_after_click.png")

number_1 = pygame.image.load("Assets/images/number_1.png")
number_1_after_click = pygame.image.load(
    "Assets/images/number_1_after_click.png")

number_2 = pygame.image.load("Assets/images/number_2.png")
number_2_after_click = pygame.image.load(
    "Assets/images/number_2_after_click.png")

number_3 = pygame.image.load("Assets/images/number_3.png")
number_3_after_click = pygame.image.load(
    "Assets/images/number_3_after_click.png")

number_4 = pygame.image.load("Assets/images/number_4.png")
number_4_after_click = pygame.image.load(
    "Assets/images/number_4_after_click.png")

number_5 = pygame.image.load("Assets/images/number_5.png")
number_5_after_click = pygame.image.load(
    "Assets/images/number_5_after_click.png")

number_6 = pygame.image.load("Assets/images/number_6.png")
number_6_after_click = pygame.image.load(
    "Assets/images/number_6_after_click.png")

number_7 = pygame.image.load("Assets/images/number_7.png")
number_7_after_click = pygame.image.load(
    "Assets/images/number_7_after_click.png")

number_8 = pygame.image.load("Assets/images/number_8.png")
number_8_after_click = pygame.image.load(
    "Assets/images/number_8_after_click.png")

number_9 = pygame.image.load("Assets/images/number_9.png")
number_9_after_click = pygame.image.load(
    "Assets/images/number_9_after_click.png")

enter_button = pygame.image.load("Assets/images/enter.png")
enter_button_after_click = pygame.image.load(
    "Assets/images/enter_after_click.png")

delete_button = pygame.image.load("Assets/images/delete.png")
delete_button_after_click = pygame.image.load(
    "Assets/images/delete_after_click.png")


# sound effects
intro_sound = pygame.mixer.Sound("Assets/sounds/intro2.wav")
wrong_answer_sound = pygame.mixer.Sound("Assets/sounds/wrong_answer.wav")
correct_answer_sound = pygame.mixer.Sound("Assets/sounds/correct_answer.wav")
clapping_sound = pygame.mixer.Sound("Assets/sounds/clapping.wav")
click_sound = pygame.mixer.Sound("Assets/sounds/click.wav")
clock_tik = pygame.mixer.Sound("Assets/sounds/clock_tik.wav")

# texts
text_file = open("Assets/texts/text_1.txt", 'r')
text_1 = text_file.read().split('\n')
text_file = open("Assets/texts/text_2.txt", 'r')
text_2 = text_file.read().split('\n')
text_file = open("Assets/texts/game_1_explanation.txt", 'r')
game_1_explanation = text_file.read().split('\n')
text_file = open("Assets/texts/game_2_explanation.txt", 'r')
game_2_explanation = text_file.read().split('\n')
text_file = open("Assets/texts/game_3_explanation.txt", 'r')
game_3_explanation = text_file.read().split('\n')
text_file = open("Assets/texts/game_4_explanation.txt", 'r')
game_4_explanation = text_file.read().split('\n')
text_file = open("Assets/texts/game_5_explanation.txt", 'r')
game_5_explanation = text_file.read().split('\n')
text_file = open("Assets/texts/game_6_explanation.txt", 'r')
game_6_explanation = text_file.read().split('\n')

# fonts
main_font = pygame.font.SysFont("cambria", text_size)
code_font = pygame.font.SysFont("cambria", code_size)
start_font = pygame.font.SysFont("cambria", text_size + 20)
speelklok_website_font = pygame.font.Font("Assets/fonts/Avenir Next.ttc", 70)

# the variable that represent the displayed window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

TOTAL_PLAY_TIME = 0


#######################################################################################
def from_millisecond_to_clock(time_in_millisecond):

    milliseconds = time_in_millisecond % 1000
    seconds = int((time_in_millisecond / 1000) % 60)
    minutes = int(((time_in_millisecond / 1000) / 60) % 60)
    hours = int((((time_in_millisecond / 1000) / 60) / 60) % 60)

    return "{:<2}:{:<2}:{:<2}:{:<5}".format(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2), str(milliseconds).zfill(3))


#######################################################################################
def main():

    if __name__ == "__main__":

        keep_going = True

        while True:

            if start_window() == 1:
                keep_going = False
            if keep_going:
                if explanation_window() == 1:
                    keep_going = False
            if keep_going:
                if team_name_window() == 1:
                    keep_going = False
            if keep_going:
                if games_window(1, game_1_explanation) == 1:
                    keep_going = False
            if keep_going:
                if games_window(2, game_2_explanation) == 1:
                    keep_going = False
            if keep_going:
                if games_window(3, game_3_explanation) == 1:
                    keep_going = False
            if keep_going:
                if games_window(4, game_4_explanation) == 1:
                    keep_going = False
            if keep_going:
                if games_window(5, game_5_explanation) == 1:
                    keep_going = False
            if keep_going:
                if games_window(6, game_6_explanation) == 1:
                    keep_going = False
            if keep_going:
                if end_window() == 1:
                    keep_going = False

            if not keep_going:
                admin_mode()
                keep_going = True


main()