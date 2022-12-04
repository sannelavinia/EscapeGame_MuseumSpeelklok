import main as m
import pygame
import widgets.button as b

class OrganMaze: 

    def __init__(self, last_clicked_letter_button=-1, correct_corresponding_organ=-1):
        self.last_clicked_letter_button = last_clicked_letter_button
        self.correct_corresponding_organ = correct_corresponding_organ

        # Initialize static locations of buttons. Locations of  buttons are set as variables.
        self.location_A = (430, 395)
        self.location_B = (422, 485)
        self.location_C = (432, 570)
        self.location_D = (425, 653)
        self.location_E = (405, 732)
        self.location_F = (430, 812)
        self.location_organ1 = (1330, 340)
        self.location_organ2 = (1470, 500)
        self.location_organ3 = (1270, 600)
        self.location_organ4 = (1460, 650)
        self.location_organ5 = (1480, 860)
        self.location_organ6 = (1250, 830)

        # Button transparent images resizing
        self.bellow_transparent = m.pygame.transform.scale(m.transparent_box, (250, 120))

        ## Create invisible buttons for each pressable object ## 
        # Buttons of letter locations are set as class variables
        self.location_A_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_A[0], self.location_A[1], 170, 70)
        self.location_B_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_B[0], self.location_B[1], 170,70)
        self.location_C_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_C[0], self.location_C[1], 170,70)
        self.location_D_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_D[0], self.location_D[1], 170,70)
        self.location_E_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_E[0], self.location_E[1], 170,70)
        self.location_F_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_F[0], self.location_F[1], 170,70)

        # Buttons of letter locations are set as class variables
        self.location_organ1_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_organ1[0], self.location_organ1[1], 240, 160)
        self.location_organ2_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_organ2[0], self.location_organ2[1], 180, 120)
        self.location_organ3_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_organ3[0], self.location_organ3[1], 170, 120)
        self.location_organ4_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_organ4[0], self.location_organ4[1], 170, 150)
        self.location_organ5_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_organ5[0], self.location_organ5[1], 240, 160)
        self.location_organ6_button = b.Button(self.bellow_transparent, self.bellow_transparent, self.bellow_transparent, \
            self.location_organ6[0], self.location_organ6[1], 170, 150)

        # Create a dictionary where the letter button is the key and the organ button is the corresponding value. 
        self.buttons_dict = {self.location_A_button: self.location_organ6_button, self.location_B_button: self.location_organ4_button, \
            self.location_C_button: self.location_organ2_button, self.location_D_button: self.location_organ1_button,
            self.location_E_button: self.location_organ5_button, self.location_F_button: self.location_organ3_button}

        # Create a dictionary that keeps track of all the correct answers that were found
        self.correct_buttons_dict = {}    

    def organmaze_pq(self):
        # Get background
        black_screen_background = pygame.transform.scale(m.black_screen_background, (m.WIDTH, m.HEIGHT))

        # Get organ_maze image
        organ_maze = pygame.transform.scale(m.organ_maze, (m.WIDTH * 0.7, m.HEIGHT * 0.7))
        organ_maze_rect = organ_maze.get_rect(center=(m.WIDTH/2, m.HEIGHT/1.8))

        # Get images
        orange_circle = pygame.image.load("Assets/images/orange_circle.png")
        orange_circle = m.pygame.transform.scale(orange_circle, (75, 75))

        green_check = pygame.image.load("Assets/images/green_check.png")
        green_check = m.pygame.transform.scale(green_check, (75, 75))

        # Get the explanation for prequestion 6
        explanation_text1 = "Voordat jullie kunnen beginnen aan het laatste spel, moeten jullie eerst deze opdracht doen:" 
        explanation_text2 = "Loop door het doolhof van slangen en breng lucht naar het orgel."
        explanation_text3 = "Klik eerst op een blaasbalg en dan op een orgel."
        prequestion_6_explanation1 = m.MagdaClean_font_30.render(explanation_text1, True, m.green_color)
        prequestion_6_explanation1_rect = prequestion_6_explanation1.get_rect(center=(m.WIDTH/2, m.HEIGHT/10))
        prequestion_6_explanation2 = m.MagdaClean_font_30.render(explanation_text2, True, m.green_color)
        prequestion_6_explanation2_rect = prequestion_6_explanation2.get_rect(center=(m.WIDTH/2, m.HEIGHT/8))
        prequestion_6_explanation3 = m.MagdaClean_font_30.render(explanation_text3, True, m.green_color)
        prequestion_6_explanation3_rect = prequestion_6_explanation3.get_rect(center=(m.WIDTH/2, m.HEIGHT/6))


        while True:
            # Display images and explanations
            m.SCREEN.blit(black_screen_background, (0, 0))
            m.SCREEN.blit(organ_maze, organ_maze_rect)
            m.SCREEN.blit(prequestion_6_explanation1, prequestion_6_explanation1_rect)
            m.SCREEN.blit(prequestion_6_explanation2, prequestion_6_explanation2_rect)
            m.SCREEN.blit(prequestion_6_explanation3, prequestion_6_explanation3_rect)

            self.location_A_button.display()
            self.location_B_button.display()
            self.location_C_button.display()
            self.location_D_button.display()
            self.location_E_button.display()
            self.location_F_button.display()

            self.location_organ1_button.display()
            self.location_organ2_button.display()
            self.location_organ3_button.display()
            self.location_organ4_button.display()
            self.location_organ5_button.display()
            self.location_organ6_button.display()

            if self.last_clicked_letter_button!=-1 and self.correct_corresponding_organ!=-1 \
                and (self.last_clicked_letter_button in self.buttons_dict) and (self.last_clicked_letter_button not in self.correct_buttons_dict):
                m.SCREEN.blit(orange_circle, (self.last_clicked_letter_button.x_pos - 37.5, self.last_clicked_letter_button.y_pos - 37.5))

            for button in self.correct_buttons_dict:
                m.SCREEN.blit(green_check, (button.x_pos - 37.5, button.y_pos - 37.5))


            for event in m.pygame.event.get():

                # when pressing the close button "X" at the top-right of the game-window
                if event.type == m.pygame.QUIT or \
                        (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                    m.pygame.quit()

                # if all correct answers are chosen and you click on the screen you continue the game
                if event.type == m.pygame.MOUSEBUTTONDOWN and len(self.correct_buttons_dict) == 6:
                    return 

                for button in self.buttons_dict:
                    corresponding_organ = self.buttons_dict[button]

                    if event.type == m.pygame.MOUSEBUTTONDOWN and button.mouse_on_button():
                        self.correct_corresponding_organ = corresponding_organ
                        self.last_clicked_letter_button = button
                        break
                    
                    if event.type == m.pygame.MOUSEBUTTONDOWN and corresponding_organ.mouse_on_button():
                        if corresponding_organ == self.correct_corresponding_organ:
                            m.correct_answer_sound.play()
                            self.correct_buttons_dict[button] = corresponding_organ
                            # del self.buttons_dict[button]
                            break
                        else:
                            self.wrong_answer_clicked = True
                            m.wrong_answer_sound.play()

                if event.type == m.pygame.MOUSEBUTTONDOWN and len(self.correct_buttons_dict) == 6:
                    # Get the congratulatory message for prequestion 6
                    congratulatory_text1 = "Goed gedaan!" 
                    congratulatory_text2 = "Klik op het scherm om verder te gaan."
                    prequestion_6_explanation1 = m.MagdaClean_font_30.render(congratulatory_text1, True, m.green_color)
                    prequestion_6_explanation1_rect = prequestion_6_explanation1.get_rect(center=(m.WIDTH/2, m.HEIGHT/10))
                    prequestion_6_explanation2 = m.MagdaClean_font_30.render(congratulatory_text2, True, m.green_color)
                    prequestion_6_explanation2_rect = prequestion_6_explanation2.get_rect(center=(m.WIDTH/2, m.HEIGHT/8))
                    prequestion_6_explanation3 = m.MagdaClean_font_30.render('', True, m.green_color) # Remove text
    


        

            m.pygame.display.update()