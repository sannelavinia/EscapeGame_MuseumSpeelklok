import pygame       # is a 2D-grafic liberary
from widgets.keyboard import *
from widgets.code_frame import *
from constants import *
from widgets.button import *
from windows.start_window import *
from windows.explanation_window import *
from windows.game_1_window import *
from windows.game_2_window import *
from windows.game_3_window import *
from windows.game_4_window import *
from windows.game_5_window import *
from windows.game_6_window import *
from windows.end_window import *



# initializing the pygame ( preventing unexpected behavior )
pygame.init()

########################### load Assets ###########################

pygame.display.set_caption("Speelklok")  # title of the window
ICON = pygame.image.load("Assets/images/saxophone.png")  # icon of the game
pygame.display.set_icon(ICON)

# images
background_start = pygame.image.load("Assets/images/background_start.jpg")
background_start = pygame.transform.scale(background_start, (WIDTH, HIGHT))
background_game_1 = pygame.image.load("Assets/images/background_game_1.jpg")
background_game_1 = pygame.transform.scale(background_game_1, (WIDTH, HIGHT))
background_game_2 = pygame.image.load("Assets/images/background_game_2.jpg")
background_game_2 = pygame.transform.scale(background_game_2, (WIDTH, HIGHT))
background_game_3 = pygame.image.load("Assets/images/background_game_3.jpg")
background_game_3 = pygame.transform.scale(background_game_3, (WIDTH, HIGHT))
background_game_4 = pygame.image.load("Assets/images/background_game_4.jpg")
background_game_4 = pygame.transform.scale(background_game_4, (WIDTH, HIGHT))
background_game_5 = pygame.image.load("Assets/images/background_game_5.jpg")
background_game_5 = pygame.transform.scale(background_game_5, (WIDTH, HIGHT))
background_game_6 = pygame.image.load("Assets/images/background_game_6.jpg")
background_game_6 = pygame.transform.scale(background_game_6, (WIDTH, HIGHT))
background_end = pygame.image.load("Assets/images/background_end.jpg")
background_end = pygame.transform.scale(background_end, (WIDTH, HIGHT))
message = pygame.image.load("Assets/images/message.png")

# clock_box = pygame.image.load("Assets/images/clock_box.png")
# clock_box = pygame.transform.scale(clock_box, (WIDTH/8, HIGHT/12))

# buttons
button_start = pygame.image.load("Assets/images/button_start.png")
button_start = pygame.transform.scale(button_start, (200, 150))

number_0 = pygame.image.load("Assets/images/number_0.png")
number_0 = pygame.transform.scale(number_0, (button_width, button_hight))
number_0_small = pygame.transform.scale(
    number_0, (button_width - reduction_ratio, button_hight - reduction_ratio))

number_1 = pygame.image.load("Assets/images/number_1.png")
number_1 = pygame.transform.scale(number_1, (button_width, button_hight))
number_1_small = pygame.transform.scale(
    number_1, (button_width - reduction_ratio, button_hight - reduction_ratio))

number_2 = pygame.image.load("Assets/images/number_2.png")
number_2 = pygame.transform.scale(number_2, (button_width, button_hight))
number_2_small = pygame.transform.scale(
    number_2, (button_width - reduction_ratio, button_hight - reduction_ratio))

number_3 = pygame.image.load("Assets/images/number_3.png")
number_3 = pygame.transform.scale(number_3, (button_width, button_hight))
number_3_small = pygame.transform.scale(
    number_3, (button_width - reduction_ratio, button_hight - reduction_ratio))

number_4 = pygame.image.load("Assets/images/number_4.png")
number_4 = pygame.transform.scale(number_4, (button_width, button_hight))
number_4_small = pygame.transform.scale(
    number_4, (button_width - reduction_ratio, button_hight - reduction_ratio))

number_5 = pygame.image.load("Assets/images/number_5.png")
number_5 = pygame.transform.scale(number_5, (button_width, button_hight))
number_5_small = pygame.transform.scale(
    number_5, (button_width - reduction_ratio, button_hight - reduction_ratio))

number_6 = pygame.image.load("Assets/images/number_6.png")
number_6 = pygame.transform.scale(number_6, (button_width, button_hight))
number_6_small = pygame.transform.scale(
    number_6, (button_width - reduction_ratio, button_hight - reduction_ratio))

number_7 = pygame.image.load("Assets/images/number_7.png")
number_7 = pygame.transform.scale(number_7, (button_width, button_hight))
number_7_small = pygame.transform.scale(
    number_7, (button_width - reduction_ratio, button_hight - reduction_ratio))

number_8 = pygame.image.load("Assets/images/number_8.png")
number_8 = pygame.transform.scale(number_8, (button_width, button_hight))
number_8_small = pygame.transform.scale(
    number_8, (button_width - reduction_ratio, button_hight - reduction_ratio))

number_9 = pygame.image.load("Assets/images/number_9.png")
number_9 = pygame.transform.scale(number_9, (button_width, button_hight))
number_9_small = pygame.transform.scale(
    number_9, (button_width - reduction_ratio, button_hight - reduction_ratio))

enter_button = pygame.image.load("Assets/images/enter.png")
enter_button = pygame.transform.scale(
    enter_button, (button_width - 3, button_hight - 3))
enter_button_small = pygame.transform.scale(
    enter_button, (button_width - reduction_ratio, button_hight - reduction_ratio))
delete_button = pygame.image.load("Assets/images/delete.png")
delete_button = pygame.transform.scale(
    delete_button, (button_width - 3, button_hight - 3))
delete_button_small = pygame.transform.scale(
    delete_button, (button_width - reduction_ratio, button_hight - reduction_ratio))

# code frame
text_frame = pygame.image.load("Assets/images/frame.png")
text_frame = pygame.transform.scale(
    text_frame, (button_width * 3, button_hight))

# sound effects
intro_sound = pygame.mixer.Sound("Assets/sounds/intro2.wav")
wrong_answer_sound = pygame.mixer.Sound("Assets/sounds/wrong_answer.wav")
correct_answer_sound = pygame.mixer.Sound("Assets/sounds/correct_answer.wav")
clapping_sound = pygame.mixer.Sound("Assets/sounds/clapping.wav")
click_sound = pygame.mixer.Sound("Assets/sounds/click.wav")

# texts
text_file = open("Assets/texts/text_1.txt", 'r')
text_1 = text_file.read().split('\n')
text_file = open("Assets/texts/text_2.txt", 'r')
text_2 = text_file.read().split('\n')
text_file = open("Assets/texts/game_1_explanation.txt", 'r')
game_1_explanation = text_file.read().split('\n')

# fonts
main_font = pygame.font.SysFont("cambria", text_size)
code_font = pygame.font.SysFont("cambria", code_size)

# the variable that represent the displayed window
SCREEN = pygame.display.set_mode((WIDTH, HIGHT))


#######################################################################################
def main():

    if __name__ == "__main__":

        start_window()
        explanation_window()
        game_1_window()
        game_2_window()
        game_3_window()
        game_4_window()
        game_5_window()
        game_6_window()
        end_window()


main()
