import main as m
import constants as c


class Text_frame():
    """
    useful for displaying one line of text,
    can be used to make an animated text,
    ex: changing color in the course of time or by changing the font
    """

    #######################################################################################
    def __init__(self, image=None, image_width=40, image_height=20, input_text="", text_color=c.white_color,
                 font=None, x_pos=0, y_pos=0):
        """initializer"""

        self.color = text_color
        self.input_text = input_text
        self.font = font
        if self.font == None:
            self.font = m.main_font
        self.text = self.font.render(input_text, True, text_color)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.textrect = self.text.get_rect(
            center=(self.x_pos, self.y_pos))
        self.image = image
        if self.image != None:
            self.image = m.pygame.transform.scale(
                image, (image_width, image_height))
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    #######################################################################################
    def display(self):
        """displays the text"""

        if self.image != None:
            m.SCREEN.blit(self.image, self.rect)
        m.SCREEN.blit(self.text, self.textrect)

    #######################################################################################
    def change_input_text(self, input_text=None, text_color=None, font=None):
        """to change the text, color or the font"""

        if input_text != None:
            input_text = self.input_text
        if text_color != None:
            text_color = self.color
        if font != None:
            font = self.font

        self.text = font.render(input_text, True, text_color)
