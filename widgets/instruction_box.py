import main as m


class Instruction_Box():
    """
    useful for displaying more than one line of text,
    the text should be in a .txt file 
    ex: by instructions or tips
    """

    #######################################################################################
    def __init__(self, image, image_width, image_height, input_text, text_color, x_pos, y_pos, text_font=None, lines_height=None, text_x_pos=None, text_y_pos=None):
        """initializer"""

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text_x_pos = text_x_pos
        if self.text_x_pos == None:
            self.text_x_pos = x_pos + 45
        self.text_y_pos = text_y_pos
        if self.text_y_pos == None:
            self.text_y_pos = y_pos + 50
        self.lines_height = lines_height
        if self.lines_height == None:
            self.lines_height = m.line_space
        self.image = m.pygame.transform.scale(
            image, (image_width, image_height))

        # render the text
        self.text = []
        for line in input_text:
            if text_font is None:
                self.text.append(m.main_font.render(line, True, text_color))
            else:
                self.text.append(text_font.render(line, True, text_color))

    #######################################################################################
    def display(self):
        """displays the text"""

        x_pos = self.x_pos
        y_pos = self.y_pos
        m.SCREEN.blit(self.image, (x_pos, y_pos))
        for element in self.text:
            m.SCREEN.blit(
                element, (x_pos + self.text_x_pos, y_pos + self.text_y_pos))
            y_pos += self.lines_height
