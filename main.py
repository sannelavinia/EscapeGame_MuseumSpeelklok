import pygame  # is a 2D-grafic liberary
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

from windows.high_score import *

from windows.prequestions.multiplechoice_pq import multiplechoice_pq
from windows.prequestions.spotdifferences_pq import spotdifferences_pq
from windows.prequestions.organmaze_pq import OrganMaze
from windows.end_game_instruction import *
from windows.end_game import *

from arduino.open_port import *
from windows.last_video import *
# initializing the pygame ( preventing unexpected behavior )
pygame.init()

# global variables
HEIGHT = 1080  # height of the displayed window
WIDTH = 1920  # width of the displayed window
TEAMS_NAMES = ["11", "22", "33", "44", "55"]
TEAMS_SCORES = ["11", "22", "33", "44", "55"]

########################### load Assets ###########################

pygame.display.set_caption("Speelklok")  # title of the window
ICON = pygame.image.load("Assets/images/saxophone.png")  # icon of the game
pygame.display.set_icon(ICON)

# images

# museum_logo
ms_logo = pygame.image.load("Assets/images/ms_logo.png")
ms_logo = pygame.transform.scale(ms_logo, (120, 36))
museum_logo_grey = pygame.image.load("Assets/images/museum_logo_grey.png")

# backgrounds
background_games_template = pygame.image.load(
    "Assets/images/background_games_template.png"
)
black_screen_background = pygame.image.load("Assets/images/black_screen_background.png")
celebration_background = pygame.image.load("Assets/images/celebration_background.png")
transparent_box = pygame.image.load("Assets/images/HD_transparent_picture.png")

# frames
instruction_screen_games = pygame.image.load(
    "Assets/images/instruction_screen_games.png"
)
metal_plate_empty = pygame.image.load("Assets/images/metal_plate_empty.png")
metal_plate_infoboard = pygame.image.load("Assets/images/metal_plate_infoboard.png")
metal_plate_museumlogo = pygame.image.load("Assets/images/metal_plate_museumlogo.png")
code_input_frame = pygame.image.load("Assets/images/code_input_frame.png")

# tip images
game_1_tip_image = pygame.image.load("Assets/images/meterstand.png")
game_3_tip_image = pygame.image.load("Assets/images/playmobil.jpg")
game_4_tip_image_1 = pygame.image.load("Assets/images/Olland_schilderij.jpg")
game_4_tip_image_2 = pygame.image.load("Assets/images/sprierkracht-orgel.png")
game_4_tip_image_3 = pygame.image.load("Assets/images/Violina.jpg")
game_4_tip_image_4 = pygame.image.load("Assets/images/koppelduiker.jpg")

# gears
blue_gear = pygame.image.load("Assets/images/blue_gear.png")
orange_gear = pygame.image.load("Assets/images/orange_gear.png")
purple_gear = pygame.image.load("Assets/images/purple_gear.png")
red_gear = pygame.image.load("Assets/images/red_gear.png")
green_gear = pygame.image.load("Assets/images/green_gear.png")
green_gear_1 = pygame.image.load("Assets/images/green_gear_1.png")
green_gear_2 = pygame.image.load("Assets/images/green_gear_2.png")
green_gear_3 = pygame.image.load("Assets/images/green_gear_3.png")
green_gear_4 = pygame.image.load("Assets/images/green_gear_4.png")
red_gear_1 = pygame.image.load("Assets/images/red_gear_1.png")
red_gear_2 = pygame.image.load("Assets/images/red_gear_2.png")
red_gear_3 = pygame.image.load("Assets/images/red_gear_3.png")
red_gear_4 = pygame.image.load("Assets/images/red_gear_4.png")
yellow_gear = pygame.image.load("Assets/images/yellow_gear.png")
rings_for_gears = pygame.image.load("Assets/images/rings_for_gears.png")
rings_for_gears_with_gears = pygame.image.load(
    "Assets/images/rings_for_gears_with_gears.png"
)

single_screw = pygame.image.load("Assets/images/single_screw.png")

# buttons
green_start_button = pygame.image.load("Assets/images/green_start_button.png")
green_start_button_pushed = pygame.image.load(
    "Assets/images/green_start_button_pushed.png"
)
small_green_button = pygame.image.load("Assets/images/small_green_button.png")

tip_button = pygame.image.load("Assets/images/tip_button.png")
tip_button_grey = pygame.image.load("Assets/images/tip_button_grey.png")
tip_button_pushed = pygame.image.load("Assets/images/tip_button_pushed.png")

# keyboard buttons
number_0 = pygame.image.load("Assets/images/number_0.png")
number_0_after_click = pygame.image.load("Assets/images/number_0_after_click.png")

number_1 = pygame.image.load("Assets/images/number_1.png")
number_1_after_click = pygame.image.load("Assets/images/number_1_after_click.png")

number_2 = pygame.image.load("Assets/images/number_2.png")
number_2_after_click = pygame.image.load("Assets/images/number_2_after_click.png")

number_3 = pygame.image.load("Assets/images/number_3.png")
number_3_after_click = pygame.image.load("Assets/images/number_3_after_click.png")

number_4 = pygame.image.load("Assets/images/number_4.png")
number_4_after_click = pygame.image.load("Assets/images/number_4_after_click.png")

number_5 = pygame.image.load("Assets/images/number_5.png")
number_5_after_click = pygame.image.load("Assets/images/number_5_after_click.png")

number_6 = pygame.image.load("Assets/images/number_6.png")
number_6_after_click = pygame.image.load("Assets/images/number_6_after_click.png")

number_7 = pygame.image.load("Assets/images/number_7.png")
number_7_after_click = pygame.image.load("Assets/images/number_7_after_click.png")

number_8 = pygame.image.load("Assets/images/number_8.png")
number_8_after_click = pygame.image.load("Assets/images/number_8_after_click.png")

number_9 = pygame.image.load("Assets/images/number_9.png")
number_9_after_click = pygame.image.load("Assets/images/number_9_after_click.png")

enter_button = pygame.image.load("Assets/images/enter.png")
enter_button_after_click = pygame.image.load("Assets/images/enter_after_click.png")

delete_button = pygame.image.load("Assets/images/delete.png")
delete_button_after_click = pygame.image.load("Assets/images/delete_after_click.png")

# prequestion images
thinking_boy = pygame.image.load("Assets/images/jongen_vragend.png")
thinking_girl = pygame.image.load("Assets/images/meisje_vertwijfeld.png")
organ_maze = pygame.image.load("Assets/images/organmaze_art.png")
spot_differences = pygame.image.load("Assets/images/spotdifferences_art.png")
gears_pq4 = pygame.image.load("Assets/images/gears_pq4.png")

red_circle = pygame.image.load("Assets/images/red_circle.png")
red_circle = m.pygame.transform.scale(red_circle, (60,60))

orange_circle = pygame.image.load("Assets/images/orange_circle.png")
orange_circle = m.pygame.transform.scale(orange_circle, (75, 75))

green_check = pygame.image.load("Assets/images/green_check.png")
green_check = m.pygame.transform.scale(green_check, (75, 75))

red_cross = pygame.image.load("Assets/images/red_cross.png")
red_cross = m.pygame.transform.scale(red_cross, (75, 75))


# sound effectsh
wrong_answer_sound = pygame.mixer.Sound("Assets/sounds/wrong_answer.wav")
correct_answer_sound = pygame.mixer.Sound("Assets/sounds/correct_answer.wav")
click_sound = pygame.mixer.Sound("Assets/sounds/click.wav")
clock_tik = pygame.mixer.Sound("Assets/sounds/clock_tik.wav")

start_game_robot_voice_correct_code = pygame.mixer.Sound(
    "Assets/sounds/start_window_correct_code.wav"
)
start_game_robot_voice_incorrect_code = pygame.mixer.Sound(
    "Assets/sounds/start_window_incorrect_code.wav"
)
game_1_to_6_robot_voice_correct_code = pygame.mixer.Sound(
    "Assets/sounds/games_correct_code.wav"
)
game_1_robot_voice_incorrect_code = pygame.mixer.Sound(
    "Assets/sounds/game_1_incorrect_code.wav"
)
game_2_robot_voice_incorrect_code = pygame.mixer.Sound(
    "Assets/sounds/game_2_incorrect_code.wav"
)
game_3_robot_voice_incorrect_code = pygame.mixer.Sound(
    "Assets/sounds/game_3_incorrect_code.wav"
)
game_4_robot_voice_incorrect_code = pygame.mixer.Sound(
    "Assets/sounds/game_4_incorrect_code.wav"
)
game_5_robot_voice_incorrect_code = pygame.mixer.Sound(
    "Assets/sounds/game_5_incorrect_code.wav"
)
game_6_robot_voice_incorrect_code = pygame.mixer.Sound(
    "Assets/sounds/game_6_incorrect_code.wav"
)

# texts
text_file = open("Assets/texts/game_instruction.txt", "r")
game_instruction = text_file.read().split("\n")

text_file = open("Assets/texts/game_1_explanation.txt", "r")
game_1_explanation = text_file.read().split("\n")
text_file = open("Assets/texts/game_2_explanation.txt", "r")
game_2_explanation = text_file.read().split("\n")
text_file = open("Assets/texts/game_3_explanation.txt", "r")
game_3_explanation = text_file.read().split("\n")
text_file = open("Assets/texts/game_4_explanation.txt", "r")
game_4_explanation = text_file.read().split("\n")
text_file = open("Assets/texts/game_5_explanation.txt", "r")
game_5_explanation = text_file.read().split("\n")
text_file = open("Assets/texts/game_6_explanation.txt", "r")
game_6_explanation = text_file.read().split("\n")

text_file = open("Assets/texts/game_1_tip_1.txt", "r")
game_1_tip_1 = text_file.read().split("\n")
text_file = open("Assets/texts/game_2_tip_1.txt", "r")
game_2_tip_1 = text_file.read().split("\n")
text_file = open("Assets/texts/game_2_tip_2.txt", "r")
game_2_tip_2 = text_file.read().split("\n")
text_file = open("Assets/texts/game_3_tip_1.txt", "r")
game_3_tip_1 = text_file.read().split("\n")
text_file = open("Assets/texts/game_5_tip_1.txt", "r")
game_5_tip_1 = text_file.read().split("\n")
text_file = open("Assets/texts/game_5_tip_2.txt", "r")
game_5_tip_2 = text_file.read().split("\n")
text_file = open("Assets/texts/game_6_tip_1.txt", "r")
game_6_tip_1 = text_file.read().split("\n")
text_file = open("Assets/texts/game_6_tip_2.txt", "r")
game_6_tip_2 = text_file.read().split("\n")

text_file = open("Assets/texts/prequestion_1.txt", "r")
prequestion_1 = text_file.read().split("\n")
text_file = open("Assets/texts/prequestion_1b.txt", "r")
prequestion_1b = text_file.read().split("\n")
text_file = open("Assets/texts/prequestion_2.txt", "r")
prequestion_2 = text_file.read().split("\n")
text_file = open("Assets/texts/prequestion_2b.txt", "r")
prequestion_2b = text_file.read().split("\n")
text_file = open("Assets/texts/prequestion_4.txt", "r")
prequestion_4 = text_file.read().split("\n")
text_file = open("Assets/texts/prequestion_4b.txt", "r")
prequestion_4b = text_file.read().split("\n")
text_file = open("Assets/texts/prequestion_5.txt", "r")
prequestion_5 = text_file.read().split("\n")
text_file = open("Assets/texts/prequestion_5b.txt", "r")
prequestion_5b = text_file.read().split("\n")

text_file = open("Assets/texts/end_game_instruction.txt", "r")
end_game_instruction_text = text_file.read().split("\n")


# fonts
speelklok_website_font = pygame.font.SysFont("cambria", text_size + 20)
MagdaClean_font_30 = pygame.font.Font("Assets/fonts/MagdaClean Regular.otf", 30)
MagdaClean_font_50 = pygame.font.Font("Assets/fonts/MagdaClean Regular.otf", 50)
MagdaClean_font_70 = pygame.font.Font("Assets/fonts/MagdaClean Regular.otf", 70)
Quantico_font_50 = pygame.font.Font("Assets/fonts/Quantico-Regular.otf", 50)
Quantico_font_70 = pygame.font.Font("Assets/fonts/Quantico-Regular.otf", 70)

# the variable that represent the displayed window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

TOTAL_PLAY_TIME = 0


#######################################################################################
def from_millisecond_to_clock(time_in_millisecond, only_min=False):

    milliseconds = time_in_millisecond % 1000
    seconds = int((time_in_millisecond / 1000) % 60)
    minutes = int(((time_in_millisecond / 1000) / 60) % 60)
    hours = int((((time_in_millisecond / 1000) / 60) / 60) % 60)

    if only_min:
        return "{:<2}:{:<2}".format(str(minutes).zfill(2), str(seconds).zfill(2))

    return "{:<2}:{:<2}:{:<2}:{:<5}".format(
        str(hours).zfill(2),
        str(minutes).zfill(2),
        str(seconds).zfill(2),
        str(milliseconds).zfill(3),
    )

arduino
serial_message = port_name() 

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
                push_button_to_start(1)
                if multiplechoice_pq(1) == 1:
                    keep_going = False
            if keep_going:
                if (
                    games_window(
                        1,
                        game_1_explanation,
                        game_1_code,
                        game_1_tip_1,
                        None,
                        None,
                        None,
                        None,
                        game_1_tip_image,
                    )
                    == 1
                ):
                    keep_going = False
            if keep_going:
                if multiplechoice_pq(2) == 1:
                    keep_going = False
            if keep_going:
                if (
                    games_window(
                        2, game_2_explanation, game_2_code, game_2_tip_1, game_2_tip_2
                    )
                    == 1
                ):
                    keep_going = False
            if keep_going:
                if spotdifferences_pq() == 1:
                    keep_going = False
            if keep_going:
                if (
                    games_window(
                        3,
                        game_3_explanation,
                        game_3_code,
                        game_3_tip_1,
                        None,
                        None,
                        None,
                        None,
                        game_3_tip_image,
                    )
                    == 1
                ):
                    keep_going = False
            if keep_going:
                if multiplechoice_pq(4) == 1:
                    keep_going = False
            if keep_going:
                if (
                    games_window(
                        4,
                        game_4_explanation,
                        game_4_code,
                        None,
                        None,
                        game_4_tip_image_1,
                        game_4_tip_image_2,
                        game_4_tip_image_3,
                        game_4_tip_image_4,
                    )
                    == 1
                ):
                    keep_going = False
            if keep_going:
                if multiplechoice_pq(5) == 1:
                    keep_going = False
            if keep_going:
                if (
                    games_window(
                        5, game_5_explanation, game_5_code, game_5_tip_1, game_5_tip_2
                    )
                    == 1
                ):
                    keep_going = False
            if keep_going:
                organ_maze = OrganMaze()
                if organ_maze.organmaze_pq() ==1:
                    keep_going = False
            if keep_going:
                if (
                    games_window(
                        6, game_6_explanation, game_6_code, game_6_tip_1, game_6_tip_2
                    )
                    == 1
                ):
                    keep_going = False
            if keep_going:
                if end_game_instruction() == 1:
                    keep_going = False
            if keep_going:
                if end_game() == 1:
                    keep_going = False
            if keep_going:
                if last_video() == 1:
                    keep_going = False
            if keep_going:
                if end_window() == 1:
                    keep_going = False
            if keep_going:
                if high_score() == 1:
                    keep_going = False
            keep_going = True


main()
