import main as m
from widgets.keyboard import *
import pygame


class Button:

    #######################################################################################
    def __init__(
        self,
        current_image,
        image,
        after_click_image,
        x_pos,
        y_pos,
        image_width=200,
        image_height=100,
    ):
        """initializer"""

        self.current_image = m.pygame.transform.scale(
            current_image, (image_width, image_height)
        )
        self.image = m.pygame.transform.scale(image, (image_width, image_height))
        self.after_click_image = m.pygame.transform.scale(
            after_click_image, (image_width, image_height)
        )
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.clicked = False

    #######################################################################################
    def display(self):
        """displays the button"""

        m.SCREEN.blit(self.current_image, self.rect)

    #######################################################################################
    def mouse_on_button(self):
        """
        checking whether the mouse cursor is on the button
        ( returns True if it is on it )
        """

        mouse_position = m.pygame.mouse.get_pos()
        if mouse_position[0] in range(
            self.rect.left, self.rect.right
        ) and mouse_position[1] in range(self.rect.top, self.rect.bottom):
            return True

    #######################################################################################
    def display_click_animation(self):
        """set the small image of the button instead of the current image"""

        self.current_image = self.after_click_image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    #######################################################################################
    def restore_normal_size(self):
        """set the normal size image of the button instead of the current image"""

        self.current_image = self.image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    # .....................................................................................#
    def pressed_button(self):
        action = False
        if self.mouse_on_button():
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        return action
