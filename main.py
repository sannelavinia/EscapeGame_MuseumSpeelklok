import pygame       # is a 2D-grafic liberary
from widgets.keyboard import *
from widgets.text_frame import *
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


# # initializing the pygame ( preventing unexpected behavior )
pygame.init()

# load Assets
pygame.display.set_caption("Speelklok")  # title of the window
ICON = pygame.image.load("Assets/images/saxophone.png")  # icon of the game
pygame.display.set_icon(ICON)

# backgrounds images
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

# buttons
button_start = pygame.image.load("Assets/images/button_start.png")
button_start = pygame.transform.scale(button_start, (200, 150))

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

# the variable that represent the displayed window
SCREEN = pygame.display.set_mode((WIDTH, HIGHT))

# fonts
main_font = pygame.font.SysFont("cambria", text_size)
code_font = pygame.font.SysFont("cambria", code_size)


#######################################################################################
def keyboard_button_pressed(pressed_button, code):
    if len(code) < 4:
        if pressed_button == 0:
            code += "0"
        elif pressed_button == 1:
            code += "1"
        elif pressed_button == 2:
            code += "2"
        elif pressed_button == 3:
            code += "3"
        elif pressed_button == 4:
            code += "4"
        elif pressed_button == 5:
            code += "5"
        elif pressed_button == 6:
            code += "6"
        elif pressed_button == 7:
            code += "7"
        elif pressed_button == 8:
            code += "8"
        elif pressed_button == 9:
            code += "9"
    if pressed_button == 11:
        if len(code) > 0:
            code = code[:-1]
    return code


#######################################################################################
def display_text(message_box, text, x_pos, y_pos):

    SCREEN.blit(message_box, (x_pos, y_pos))
    for element in text:
        SCREEN.blit(element, (x_pos + 45, y_pos + 50))
        y_pos += line_space


#######################################################################################
def render_text(input_text, color, message_width, message_hight):

    global message
    message_box = pygame.transform.scale(
        message, (message_width, message_hight))

    # render the text
    text = []
    for line in input_text:
        text.append(main_font.render(line, True, color))

    return text, message_box


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
