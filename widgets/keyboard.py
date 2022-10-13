import main as m
from widgets.button import *
from widgets.code_frame import *


class Keyboard():

    # initializer
    def __init__(self, x_pos, y_pos):
        self.button_0 = Button(m.number_0,
                               m.number_0, m.number_0_small, x_pos + m.button_spaces, y_pos + 3 * m.button_spaces)
        self.button_1 = Button(
            m.number_1, m.number_1, m.number_1_small, x_pos, y_pos)
        self.button_2 = Button(m.number_2, m.number_2, m.number_2_small,
                               x_pos + m.button_spaces, y_pos)
        self.button_3 = Button(m.number_3, m.number_3, m.number_3_small,
                               x_pos + 2 * m.button_spaces, y_pos)
        self.button_4 = Button(m.number_4, m.number_4, m.number_4_small,
                               x_pos, y_pos + m.button_spaces)
        self.button_5 = Button(m.number_5, m.number_5, m.number_5_small, x_pos + m.button_spaces,
                               y_pos + m.button_spaces)
        self.button_6 = Button(m.number_6, m.number_6, m.number_6_small, x_pos + 2 *
                               m.button_spaces, y_pos + m.button_spaces)
        self.button_7 = Button(m.number_7, m.number_7, m.number_7_small,
                               x_pos, y_pos + 2 * m.button_spaces)
        self.button_8 = Button(m.number_8, m.number_8, m.number_8_small, x_pos + m.button_spaces,
                               y_pos + 2 * m.button_spaces)
        self.button_9 = Button(m.number_9, m.number_9, m.number_9_small, x_pos + 2 * m.button_spaces,
                               y_pos + 2 * m.button_spaces)
        self.enter_button = Button(m.enter_button, m.enter_button, m.enter_button_small,
                                   x_pos + 2 * m.button_spaces, y_pos + 3 * m.button_spaces)
        self.delete_button = Button(m.delete_button, m.delete_button,
                                    m.delete_button_small, x_pos, y_pos + 3 * m.button_spaces)
        self.text_frame = Text_frame(
            m.text_frame, "", m.white_color, m.code_font, x_pos + m.button_spaces, y_pos - m.button_spaces)

    #######################################################################################
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

    #######################################################################################
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

    #######################################################################################
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

    #######################################################################################
    def move_to(self, x_pos, y_pos):
        self.__init__(x_pos, y_pos)

    #######################################################################################
    def keyboard_button_pressed(self, pressed_button, code):
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
