import main as m
from widgets.button import Button
from widgets.text_frame import Text_frame


class Keyboard():

    # initializer
    def __init__(self, x_pos, y_pos):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.button_0 = Button(m.number_0, m.number_0, m.number_0_after_click, x_pos +
                               m.button_width, y_pos + 3 * m.button_height, m.button_width, m.button_height)
        self.button_1 = Button(m.number_1, m.number_1, m.number_1_after_click,
                               x_pos, y_pos, m.button_width, m.button_height)
        self.button_2 = Button(m.number_2, m.number_2, m.number_2_after_click,
                               x_pos + m.button_width, y_pos, m.button_width, m.button_height)
        self.button_3 = Button(m.number_3, m.number_3, m.number_3_after_click,
                               x_pos + 2 * m.button_width, y_pos, m.button_width, m.button_height)
        self.button_4 = Button(m.number_4, m.number_4, m.number_4_after_click,
                               x_pos, y_pos + m.button_height, m.button_width, m.button_height)
        self.button_5 = Button(m.number_5, m.number_5, m.number_5_after_click, x_pos + m.button_width,
                               y_pos + m.button_height, m.button_width, m.button_height)
        self.button_6 = Button(m.number_6, m.number_6, m.number_6_after_click, x_pos + 2 *
                               m.button_width, y_pos + m.button_height, m.button_width, m.button_height)
        self.button_7 = Button(m.number_7, m.number_7, m.number_7_after_click,
                               x_pos, y_pos + 2 * m.button_height, m.button_width, m.button_height)
        self.button_8 = Button(m.number_8, m.number_8, m.number_8_after_click, x_pos + m.button_width,
                               y_pos + 2 * m.button_height, m.button_width, m.button_height)
        self.button_9 = Button(m.number_9, m.number_9, m.number_9_after_click, x_pos + 2 * m.button_width,
                               y_pos + 2 * m.button_height, m.button_width, m.button_height)
        self.enter_button = Button(m.enter_button, m.enter_button, m.enter_button_after_click,
                                   x_pos + 2 * m.button_width, y_pos + 3 * m.button_height, m.button_width, m.button_height)
        self.delete_button = Button(m.delete_button, m.delete_button,
                                    m.delete_button_after_click, x_pos, y_pos + 3 * m.button_height, m.button_width, m.button_height)

        # code frame
        self.code_frame_first_number = Text_frame(m.code_input_frame, m.button_width*3/4, m.button_height,
                                                  "", m.white_color, m.code_font, self.x_pos-(m.button_width/8), self.y_pos - m.button_height)
        self.code_frame_second_number = Text_frame(m.code_input_frame, m.button_width*3/4, m.button_height,
                                                   "", m.white_color, m.code_font, self.x_pos+5*(m.button_width/8), self.y_pos - m.button_height)
        self.code_frame_third_number = Text_frame(m.code_input_frame, m.button_width*3/4, m.button_height,
                                                  "", m.white_color, m.code_font, self.x_pos+11 * (m.button_width/8), self.y_pos - m.button_height)
        self.code_frame_fourth_number = Text_frame(m.code_input_frame, m.button_width*3/4, m.button_height,
                                                   "", m.white_color, m.code_font, self.x_pos+17 * (m.button_width/8), self.y_pos - m.button_height)

    #######################################################################################
    def display(self):

        self.code_frame_first_number.display()
        self.code_frame_second_number.display()
        self.code_frame_third_number.display()
        self.code_frame_fourth_number.display()
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
        if pressed_button == 11:    # when pressing the delete button
            if len(code) > 0:
                code = code[:-1]
                self.code_frame_first_number.change_input_text("")
                self.code_frame_second_number.change_input_text("")
                self.code_frame_third_number.change_input_text("")
                self.code_frame_fourth_number.change_input_text("")

        # changing the displayed code
        if len(code) > 0:
            self.code_frame_first_number.change_input_text(code[0])
            if len(code) > 1:
                self.code_frame_second_number.change_input_text(code[1])
                if len(code) > 2:
                    self.code_frame_third_number.change_input_text(code[2])
                    if len(code) > 3:
                        self.code_frame_fourth_number.change_input_text(
                            code[3])

        return code
