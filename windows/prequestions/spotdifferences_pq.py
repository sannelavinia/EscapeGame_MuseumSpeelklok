import main as m
import pygame
import widgets.button as b
#from widgets.text_frame import Text_frame
from widgets.instruction_box import Instruction_Box

def spotdifferences_pq():
    # Scale the background and texts 
    black_screen_background = pygame.transform.scale(m.black_screen_background, (m.WIDTH, m.HEIGHT))
    title = m.MagdaClean_font_50.render('Voorvraag 3', True, m.green_color)
    title_rect = title.get_rect(center=(m.WIDTH/2, m.HEIGHT/14))

    # Get the explanation for prequestion 3
    explanation_text = "Zoek de verschillen. Klik op de rechterafbeelding de verschillen aan."
    prequestion_3_explanation = m.MagdaClean_font_30.render(explanation_text, True, m.green_color)
    prequestion_3_explanation_rect = prequestion_3_explanation.get_rect(center=(m.WIDTH/2, m.HEIGHT/7))

    # Get the spot_differences image with the right scale
    spot_differences_image = m.pygame.transform.scale(m.spot_differences, (1524, 857))
    spot_differences_rect = spot_differences_image.get_rect(center=(m.WIDTH/2, m.HEIGHT/1.8))

    diff = 0    #keeps track of how many differences are found
    found_differences = [0,0,0,0,0,0]
    

    while True:

        # Display static elements of screen
        m.SCREEN.blit(black_screen_background, (0, 0))
        m.SCREEN.blit(title, title_rect)
        m.SCREEN.blit(prequestion_3_explanation, prequestion_3_explanation_rect)
        m.SCREEN.blit(spot_differences_image, spot_differences_rect)

        if found_differences[0] == 1:
            m.SCREEN.blit(difference_1_red_circle, difference_1_red_circle_rect)

        # update diff counter
        diff = found_differences.count(1)
        diff_counter = m.MagdaClean_font_30.render(f'Verschillen gevonden: {diff}/6', True, m.green_color)
        m.SCREEN.blit(diff_counter, (m.WIDTH/1.3, m.HEIGHT/15))

        location_diff_1 = (1385, 273)
        location_diff_2 = (1167, 713)
        location_diff_3 = (1197, 831)
        location_diff_4 = (1234, 875)
        location_diff_5 = (1297, 828)
        location_diff_6 = (1377, 983)
        difference_image = m.pygame.transform.scale(m.transparent_box, (50, 50))

        #Create invisible button and red circle for difference 1
        difference_1_button = b.Button(difference_image, difference_image, difference_image, \
            location_diff_1[0], location_diff_1[1], 50, 50)
        difference_1_red_circle = m.MagdaClean_font_50.render('O', True, m.red_color)
        difference_1_red_circle_rect = title.get_rect(center=(location_diff_1[0], location_diff_1[1]))

        difference_2_button = b.Button(difference_image, difference_image, difference_image, \
            location_diff_2[0], location_diff_2[1], 50, 50)
        difference_3_button = b.Button(difference_image, difference_image, difference_image, \
            location_diff_3[0], location_diff_3[1], 50, 50)
        difference_4_button = b.Button(difference_image, difference_image, difference_image, \
            location_diff_4[0], location_diff_4[1], 50, 50)
        difference_5_button = b.Button(difference_image, difference_image, difference_image, \
            location_diff_5[0], location_diff_5[1], 50, 50)
        difference_6_button = b.Button(difference_image, difference_image, difference_image, \
            location_diff_6[0], location_diff_6[1], 50, 50)

        
        rect_spot_the_differences = m.spot_differences.get_rect()
        
        difference_1_button.display()
        m.SCREEN.blit(m.red_gear, (location_diff_1[0], location_diff_1[1]))

        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.quit()

            diff = found_differences.count(1)
            # if the correct answer is chosen and you click on the screen you continue the game
            if event.type == m.pygame.MOUSEBUTTONDOWN and diff >= 6:
                return
            

            if event.type == m.pygame.MOUSEBUTTONDOWN and difference_1_button.mouse_on_button():
                m.correct_answer_sound.play()
                found_differences[0] = 1
                break
                
            if event.type == m.pygame.MOUSEBUTTONDOWN and difference_2_button.mouse_on_button():
                m.correct_answer_sound.play()
                m.SCREEN.blit(m.red_gear, (location_diff_2[0], location_diff_2[1]))
                found_differences[1] = 1
            if event.type == m.pygame.MOUSEBUTTONDOWN and difference_3_button.mouse_on_button():
                m.correct_answer_sound.play()
                m.SCREEN.blit(m.red_gear, (location_diff_3[0], location_diff_3[1]))
                found_differences[2] = 1
            if event.type == m.pygame.MOUSEBUTTONDOWN and difference_4_button.mouse_on_button():
                m.correct_answer_sound.play()
                m.SCREEN.blit(m.red_gear, (location_diff_4[0], location_diff_4[1]))
                found_differences[3] = 1
            if event.type == m.pygame.MOUSEBUTTONDOWN and difference_5_button.mouse_on_button():
                m.correct_answer_sound.play()
                m.SCREEN.blit(m.red_gear, (location_diff_5[0], location_diff_5[1]))
                found_differences[4] = 1
            if event.type == m.pygame.MOUSEBUTTONDOWN and difference_6_button.mouse_on_button():
                m.correct_answer_sound.play()
                m.SCREEN.blit(m.red_gear, (location_diff_5[0], location_diff_5[1]))
                found_differences[5] = 1


        m.pygame.display.update()