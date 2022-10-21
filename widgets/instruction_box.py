import main as m


class Instruction_Box():
    """
    useful for displaying more than one line of text,
    the text should be in a .txt file 
    ex: by instructions or tips
    """

    #######################################################################################
    def __init__(self, image, image_width, image_height, input_text, text_color, x_pos, y_pos):
        """initializer"""

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = m.pygame.transform.scale(
            image, (image_width, image_height))

        # render the text
        self.text = []
        for line in input_text:
            self.text.append(m.main_font.render(line, True, text_color))

    #######################################################################################
    def display(self):
        """displays the text"""

        x_pos = self.x_pos
        y_pos = self.y_pos
        m.SCREEN.blit(self.image, (x_pos, y_pos))
        for element in self.text:
            m.SCREEN.blit(element, (x_pos + 45, y_pos + 50))
            y_pos += m.line_space
