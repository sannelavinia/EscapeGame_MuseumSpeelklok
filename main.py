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

background_gears = pygame.image.load("Assets/images/background_gearsv1.jpg")
background_gears = pygame.transform.scale(background_gears, (WIDTH, HIGHT))
yellowbar = pygame.image.load("Assets/images/yellowbar.jpg")
yellowbar = pygame.transform.scale(yellowbar, (1400, 120))
ms_logo = pygame.image.load("Assets/images/ms_logo.png")
ms_logo = pygame.transform.scale(ms_logo, (120, 36))


message = pygame.image.load("Assets/images/message.png")
instruction_box = pygame.image.load("Assets/images/instructions_text_box.png")

tip_message_box = pygame.image.load("Assets/images/tip_message_box.png")


# clock_box = pygame.image.load("Assets/images/clock_box.png")
# clock_box = pygame.transform.scale(clock_box, (WIDTH/8, HIGHT/12))

# buttons
button_verder = pygame.image.load("Assets/images/button_verder.jpg")
button_verder = pygame.transform.scale(button_verder, (166, 45))
button_verder_small = pygame.transform.scale(
    button_verder, (166 - 100, 45 - 10))

button_start = pygame.image.load("Assets/images/button_start.png")
button_start = pygame.transform.scale(button_start, (166, 45))

tip_button = pygame.image.load("Assets/images/tip_button.png")
tip_button = pygame.transform.scale(tip_button, (75, 75))
tip_button_small = pygame.transform.scale(
    tip_button, (75 - reduction_ratio, 75 - reduction_ratio))

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
clock_tik = pygame.mixer.Sound("Assets/sounds/clock_tik.wav")

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
speelklok_website_font = pygame.font.Font("Assets/fonts/Avenir Next.ttc", 70)

# the variable that represent the displayed window
SCREEN = pygame.display.set_mode((WIDTH, HIGHT))

TOTAL_PLAY_TIME = 0


#######################################################################################
def from_millisecond_to_clock(time_in_millisecond):

    milliseconds = time_in_millisecond % 1000
    seconds = int((time_in_millisecond / 1000) % 60)
    minutes = int(((time_in_millisecond / 1000) / 60) % 60)
    hours = int((((time_in_millisecond / 1000) / 60) / 60) % 60)

    return f"{hours}:{minutes}:{seconds}:{milliseconds}"


def admin_mode():
    keyboard = Keyboard(WIDTH/2, HIGHT/2)
    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0  # used for animating the buttons

    while True:

        SCREEN.fill(black_color)
        keyboard.display()

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

        # resize the clicked button
        if timer >= button_resizing_delay:
            # to the next window (if the code was correct)
            if pressed_button == 10:
                if code == admin_code:
                    correct_answer_sound.play()
                    return
                else:
                    wrong_answer_sound.play()
            else:
                click_sound.play()
            code = keyboard.keyboard_button_pressed(pressed_button, code)
            keyboard.text_frame.change_input_text(code, m.white_color)
            # reset
            keyboard.resize_buttons()
            button_pressed = False
            pressed_button = 99
            timer = 0

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.QUIT:
                m.pygame.quit()

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN:
                pressed_button = keyboard.pressed_button()

                if pressed_button in range(0, 12):
                    button_pressed = True
        # the window should be updated after each while-loop
        m.pygame.display.update()


#######################################################################################
def main():

    if __name__ == "__main__":

        while True:
            if start_window() != 1 and explanation_window() != 1 and \
                    game_1_window() != 1 and game_2_window() != 1 and \
                    game_3_window() != 1 and game_4_window() != 1 and \
                    game_5_window() != 1 and game_6_window() != 1 and \
                    end_window() != 1:
                pass
            else:
                admin_mode()


main()
