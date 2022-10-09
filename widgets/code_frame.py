import main as m


class Text_frame():

    # initializer
    def __init__(self, image, input_text, x_pos, y_pos):
        self.image = image
        self.text = m.code_font.render(input_text, True, "white")
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.textrect = self.text.get_rect(
            center=(self.x_pos - 50, self.y_pos))

    #######################################################################################
    def display(self):
        m.SCREEN.blit(self.image, self.rect)
        m.SCREEN.blit(self.text, self.textrect)

    #######################################################################################
    def change_input_text(self, input_text):
        self.text = m.code_font.render(input_text, True, "white")
