from widgets.button import *
from widgets.text_frame import *

# load Assets
# buttons
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

# text frame
text_frame = pygame.image.load("Assets/images/frame.png")
text_frame = pygame.transform.scale(
    text_frame, (button_width * 3, button_hight))


class Keyboard():
    def __init__(self, x_pos, y_pos):
        self.button_0 = Button(number_0,
                               number_0, number_0_small, x_pos + button_spaces, y_pos + 3 * button_spaces)
        self.button_1 = Button(
            number_1, number_1, number_1_small, x_pos, y_pos)
        self.button_2 = Button(number_2, number_2, number_2_small,
                               x_pos + button_spaces, y_pos)
        self.button_3 = Button(number_3, number_3, number_3_small,
                               x_pos + 2 * button_spaces, y_pos)
        self.button_4 = Button(number_4, number_4, number_4_small,
                               x_pos, y_pos + button_spaces)
        self.button_5 = Button(number_5, number_5, number_5_small, x_pos + button_spaces,
                               y_pos + button_spaces)
        self.button_6 = Button(number_6, number_6, number_6_small, x_pos + 2 *
                               button_spaces, y_pos + button_spaces)
        self.button_7 = Button(number_7, number_7, number_7_small,
                               x_pos, y_pos + 2 * button_spaces)
        self.button_8 = Button(number_8, number_8, number_8_small, x_pos + button_spaces,
                               y_pos + 2 * button_spaces)
        self.button_9 = Button(number_9, number_9, number_9_small, x_pos + 2 * button_spaces,
                               y_pos + 2 * button_spaces)
        self.enter_button = Button(enter_button, enter_button, enter_button_small,
                                   x_pos + 2 * button_spaces, y_pos + 3 * button_spaces)
        self.delete_button = Button(delete_button, delete_button,
                                    delete_button_small, x_pos, y_pos + 3 * button_spaces)
        self.text_frame = Text_frame(
            text_frame, "", x_pos + button_spaces, y_pos - button_spaces)

    def display(self):
        self.text_frame.display()
        self.button_1.display()
        self.button_2.display()
        self.button_3.display()
        self.button_4.display()
        self.button_5.display()
        self.button_6.display()
        self.button_7.display()
        self.button_8.display()
        self.button_9.display()
        self.delete_button.display()
        self.button_0.display()
        self.enter_button.display()

    def pressed_button(self):
        if self.button_0.mouse_on_button():
            self.button_0.display_click_animation()
            return 0
        elif self.button_1.mouse_on_button():
            self.button_1.display_click_animation()
            return 1
        elif self.button_2.mouse_on_button():
            self.button_2.display_click_animation()
            return 2
        elif self.button_3.mouse_on_button():
            self.button_3.display_click_animation()
            return 3
        elif self.button_4.mouse_on_button():
            self.button_4.display_click_animation()
            return 4
        elif self.button_5.mouse_on_button():
            self.button_5.display_click_animation()
            return 5
        elif self.button_6.mouse_on_button():
            self.button_6.display_click_animation()
            return 6
        elif self.button_7.mouse_on_button():
            self.button_7.display_click_animation()
            return 7
        elif self.button_8.mouse_on_button():
            self.button_8.display_click_animation()
            return 8
        elif self.button_9.mouse_on_button():
            self.button_9.display_click_animation()
            return 9
        elif self.enter_button.mouse_on_button():
            self.enter_button.display_click_animation()
            return 10
        elif self.delete_button.mouse_on_button():
            self.delete_button.display_click_animation()
            return 11
        return 99

    def resize_buttons(self):
        self.button_0.restore_normal_size()
        self.button_1.restore_normal_size()
        self.button_2.restore_normal_size()
        self.button_3.restore_normal_size()
        self.button_4.restore_normal_size()
        self.button_5.restore_normal_size()
        self.button_6.restore_normal_size()
        self.button_7.restore_normal_size()
        self.button_8.restore_normal_size()
        self.button_9.restore_normal_size()
        self.enter_button.restore_normal_size()
        self.delete_button.restore_normal_size()

    def move_to(self, x_pos, y_pos):
        self.__init__(x_pos, y_pos)
