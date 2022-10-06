from main import *
from widgets.keyboard import *


class Button():

    # initializer
    def __init__(self, current_image, image, small_image, x_pos, y_pos):
        self.current_image = current_image
        self.image = image
        self.small_image = small_image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    # displays the button
    def display(self):
        global SCREEN
        SCREEN.blit(self.current_image, self.rect)

    # checking whether the mouse cursor is on the button ( returns True if it is on it )
    def mouse_on_button(self):
        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] in range(self.rect.left, self.rect.right) and mouse_position[1] in range(self.rect.top, self.rect.bottom):
            return True

    # # changing the color of the button text whenever the mouse-pointer is on it
    # def change_color(self):
    #     mouse_position = pygame.mouse.get_pos()
    #     if mouse_position[0] in range(self.rect.left, self.rect.right) and mouse_position[1] in range(self.rect.top, self.rect.bottom):
    #         self.text = main_font.render(self.text_input, True, "green")
    #     else:
    #         self.text = main_font.render(self.text_input, True, "white")

    def display_click_animation(self):
        self.current_image = self.small_image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def restore_normal_size(self):
        self.current_image = self.image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
