import main as m
import pygame
import widgets.button as b

class OrganMaze: 

    def __init__(self, last_clicked_letter_button=-1, correct_corresponding_organ=-1):
        self.last_clicked_letter_button = last_clicked_letter_button
        self.correct_corresponding_organ = correct_corresponding_organ

        # Initialize static locations of buttons. Locations of  buttons are set as variables.
        self.location_A = (450, 400)
        self.location_B = (420, 490)
        self.location_C = (450, 580)
        self.location_D = (450, 660)
        self.location_E = (420, 730)
        self.location_F = (450, 820)
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


    def organmaze_pq(self):
        # Get background
        black_screen_background = pygame.transform.scale(m.black_screen_background, (m.WIDTH, m.HEIGHT))

        # Get organ_maze image
        organ_maze = pygame.transform.scale(m.organ_maze, (m.WIDTH * 0.7, m.HEIGHT * 0.7))
        organ_maze_rect = organ_maze.get_rect(center=(m.WIDTH/2, m.HEIGHT/1.8))

        # Get images
        orange_circle = pygame.image.load("Assets/images/orange_circle.png")
        orange_circle = m.pygame.transform.scale(orange_circle, (100,100))

        green_check = pygame.image.load("Assets/images/green_check.png")
        green_check = m.pygame.transform.scale(green_check, (100, 100))

        # TODO: delete this!!
        testimage = m.pygame.transform.scale(m.green_start_button, (50, 50))

        # Get the explanation for prequestion 3
        explanation_text1 = "Voordat jullie kunnen beginnen aan het laatste spel, moeten jullie eerst deze opdracht doen:" 
        explanation_text2 = "Loop door het doolhof van slangen en breng lucht naar het orgel."
        prequestion_6_explanation1 = m.MagdaClean_font_30.render(explanation_text1, True, m.green_color)
        prequestion_6_explanation1_rect = prequestion_6_explanation1.get_rect(center=(m.WIDTH/2, m.HEIGHT/9))
        prequestion_6_explanation2 = m.MagdaClean_font_30.render(explanation_text2, True, m.green_color)
        prequestion_6_explanation2_rect = prequestion_6_explanation2.get_rect(center=(m.WIDTH/2, m.HEIGHT/7))

        # Set up correct answer counter
        correct = 0 # keeps track of how many correct answers were found
        found_answers = [0, 0, 0, 0, 0, 0] # keeps track of which answers were found 

        # Pairs of bellows and organs
        # pairs = [(location_A_button, self.location_organ6_button), (location_B_button, self.location_organ4_button), \
        #         (location_C_button, self.location_organ2_button), (location_D_button, self.location_organ1_button),
        #         (location_E_button, self.location_organ5_button), (location_F_button, self.location_organ3_button)]
                
        # selected1 = 0
        # selected2 = 0
        # clicked = 0
        # correct_index = 1000

        while True:

            m.SCREEN.blit(black_screen_background, (0, 0))
            m.SCREEN.blit(organ_maze, organ_maze_rect)
            # m.SCREEN.blit(title, title_rect)
            m.SCREEN.blit(prequestion_6_explanation1, prequestion_6_explanation1_rect)
            m.SCREEN.blit(prequestion_6_explanation2, prequestion_6_explanation2_rect)

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

            if self.last_clicked_letter_button!=-1 and self.correct_corresponding_organ!=-1:
                m.SCREEN.blit(orange_circle, (self.last_clicked_letter_button.x_pos, self.last_clicked_letter_button.y_pos))
                m.SCREEN.blit(testimage, (self.correct_corresponding_organ.x_pos, self.correct_corresponding_organ.y_pos))

            # if clicked in buttons1:
            #     selected1 = clicked
            #     selected_location = location
            # if clicked in buttons2:
            #     selected2 = clicked
            #     selected_location = location
            
            # if selected1 != 0 and selected2 != 0:
            #     if (selected1, selected2) in pairs:
            #         correct_index = pairs.index((selected1, selected2))
            #         selected1 = 0
            #         selected2 = 0
            #     else:
            #         selected1 = 0
            #         selected2 = 0
            
            # if correct_index != 1000:
            #     found_answers[correct_index] = 1
            #     correct_index = 1000

            
            # #Counting correct answers
            # correct = found_answers.count(1)

            #TODO delete this
            # array = m.MagdaClean_font_30.render(str(found_answers), True, m.green_color)
            # m.SCREEN.blit(array, (0,0))
            # selection1 = m.MagdaClean_font_30.render(str(selected1), True, m.green_color)
            # m.SCREEN.blit(selection1, (0,20))
            # selection2 = m.MagdaClean_font_30.render(str(selected2), True, m.green_color)
            # m.SCREEN.blit(selection2, (0,40))




            for event in m.pygame.event.get():

                # when pressing the close button "X" at the top-right of the game-window
                if event.type == m.pygame.QUIT or \
                        (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                    m.pygame.quit()

                for button in self.buttons_dict:
                   if event.type == m.pygame.MOUSEBUTTONDOWN and button.mouse_on_button():
                    self.correct_corresponding_organ = self.buttons_dict[button]
                    self.last_clicked_letter_button = button
                    break

                # if all correct answers are chosen and you click on the screen you continue the game
                # if event.type == m.pygame.MOUSEBUTTONDOWN:
                #     return

                # if event.type == m.pygame.MOUSEBUTTONDOWN and location_A_button.mouse_on_button() and not selected1:
                #     clicked = location_A_button
                #     location = location_A
                # if event.type == m.pygame.MOUSEBUTTONDOWN and self.location_organ6_button.mouse_on_button() and not selected2:
                #     clicked = self.location_organ6_button
                #     location = self.location_organ6

                # if event.type == m.pygame.MOUSEBUTTONDOWN and location_B_button.mouse_on_button() and not selected1:
                #     clicked = location_B_button
                # if event.type == m.pygame.MOUSEBUTTONDOWN and self.location_organ4_button.mouse_on_button() and not selected2:
                #     clicked = self.location_organ4_button

                # # Correct first pair
                # if event.type == m.pygame.MOUSEBUTTONDOWN and location_A_button.mouse_on_button():
                #     m.correct_answer_sound.play()
                #     if found_answers.count([1,0]) == 0:
                #         found_answers[0][0] = 1
                #     else:
                #         # TODO: what happens if already another bellow selected
                #         pass
                #     break
                # if event.type == m.pygame.MOUSEBUTTONDOWN and self.location_organ6_button.mouse_on_button():
                #     m.correct_answer_sound.play()
                #     if found_answers.count([0,1]) == 0:
                #         found_answers[0][1] = 1
                #     else:
                #         # TODO: what happens if another organ is already selected?
                #         pass
                #     break
                    

                # For each difference, if it is found then the found_difference list will be updated
                # and the correct answer sound will be played. 
                # if event.type == m.pygame.MOUSEBUTTONDOWN and _button.mouse_on_button() \
                #     and found_answers[0] != 1:
                #     m.correct_answer_sound.play()
                #     found_differences[0] = 1
                    #break # go out of event for loop so that everything is correctly updated

            m.pygame.display.update()