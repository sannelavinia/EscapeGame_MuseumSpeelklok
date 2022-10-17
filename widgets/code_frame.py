import main as m


class Text_frame():

    # initializer
    def __init__(self, image, input_text, text_color, code_font, x_pos, y_pos):
        self.image = image
        self.text = code_font.render(input_text, True, text_color)
        self.x_pos = x_pos
        self.y_pos = y_pos
        if self.image != None:
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.textrect = self.text.get_rect(
            center=(self.x_pos - 50, self.y_pos))

    #######################################################################################
    def display(self):
        if self.image != None:
            m.SCREEN.blit(self.image, self.rect)
        m.SCREEN.blit(self.text, self.textrect)

    #######################################################################################
    def change_input_text(self, input_text, text_color):
        self.text = m.code_font.render(input_text, True, text_color)
