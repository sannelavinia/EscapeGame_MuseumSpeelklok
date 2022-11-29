import pygame
import main as m
from widgets.instruction_box import Instruction_Box
from widgets.button import Button
import widgets.button as b

def mc_temp(prequestion_x, prequestion_xb, answera, answerb, answerc, answerd):
    # Initializing texts
    mc_temp.prequestion = Instruction_Box(m.transparent_box, 1000,
                              450, prequestion_x, m.green_color, m.WIDTH/18, m.HEIGHT/15, m.MagdaClean_font_50)
    mc_temp.prequestion_b = Instruction_Box(m.transparent_box, 1000,
                              450, prequestion_xb, m.green_color, m.WIDTH/18, m.HEIGHT/15, m.MagdaClean_font_50)
                              
    mc_temp.answera = answera
    mc_temp.answerb = answerb
    mc_temp.answerc = answerc
    mc_temp.answerd = answerd

    mc_temp.answer_a = m.MagdaClean_font_50.render(answera, True, m.green_color)
    mc_temp.answer_b = m.MagdaClean_font_50.render(answerb, True, m.green_color)
    mc_temp.answer_c = m.MagdaClean_font_50.render(answerc, True, m.green_color)
    mc_temp.answer_d = m.MagdaClean_font_50.render(answerd, True, m.green_color)

def multiplechoice_pq(game_number):
    title = m.MagdaClean_font_70.render(f'Voorvraag {game_number}', True, m.green_color)
    title_rect = title.get_rect(center=(m.WIDTH/2, m.HEIGHT/7))

    black_screen_background = pygame.transform.scale(m.black_screen_background, (m.WIDTH, m.HEIGHT))

    # Multiple choice prequestion 1 text
    if game_number == 1:
        mc_temp( m.prequestion_1, m.prequestion_1b, 'a) Slinger', 'b) Klepel', 'c) Was', 'd) Lepel')
        buttonwidth = 205
        button_y = m.WIDTH/4
        answer_a_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/2.50, buttonwidth, 60)
        answer_b_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/2.00, buttonwidth, 60)
        answer_c_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.67, buttonwidth, 60)
        answer_d_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.43, buttonwidth, 60)
        correct_button = answer_b_button
    if game_number == 2:
        mc_temp(m.prequestion_2, m.prequestion_2b, 'a) Een worst', 'b) Gouden bergen', 'c) Een jurk', 'd) Een spiegel')
        buttonwidth = 370
        button_y = m.WIDTH/3.5
        answer_a_button = b.Button(m.green_start_button, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/2.50, buttonwidth, 60)
        answer_b_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/2.00, buttonwidth, 60)
        answer_c_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.67, buttonwidth, 60)
        answer_d_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.43, buttonwidth, 60)
        correct_button = answer_d_button

    

    while True:
        
        m.SCREEN.blit(black_screen_background, (0, 0))
        m.SCREEN.blit(title, title_rect)

        mc_temp.prequestion.display()

        m.SCREEN.blit(mc_temp.answer_a, (m.WIDTH/5, m.HEIGHT/2.7))
        m.SCREEN.blit(mc_temp.answer_b, (m.WIDTH/5, m.HEIGHT/2.12))
        m.SCREEN.blit(mc_temp.answer_c, (m.WIDTH/5, m.HEIGHT/1.75))
        m.SCREEN.blit(mc_temp.answer_d, (m.WIDTH/5, m.HEIGHT/1.49))

        answer_a_button.display()
        answer_b_button.display()
        answer_c_button.display()
        answer_d_button.display() 

        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.quit()

            # if the correct answer is chosen and you click on the screen you continue the game
            if event.type == m.pygame.MOUSEBUTTONDOWN and mc_temp.prequestion == mc_temp.prequestion_b: 
                return

            # when correct answer is chosen you get a congratulatory message
            if event.type == m.pygame.MOUSEBUTTONDOWN and correct_button.mouse_on_button():
                m.correct_answer_sound.play()
                title = m.MagdaClean_font_50.render('', True, m.red_color)
                mc_temp.answer_a = m.MagdaClean_font_50.render('', True, m.red_color)
                mc_temp.answer_b = m.MagdaClean_font_50.render('', True, m.red_color)
                mc_temp.answer_c = m.MagdaClean_font_50.render('', True, m.red_color)
                mc_temp.answer_d = m.MagdaClean_font_50.render('', True, m.red_color)
                mc_temp.prequestion = mc_temp.prequestion_b
                continue

            # answer a) is wrong, it will turn red
            if answer_a_button != correct_button and event.type == m.pygame.MOUSEBUTTONDOWN and answer_a_button.mouse_on_button():
                m.wrong_answer_sound.play()
                mc_temp.answer_a = m.MagdaClean_font_50.render(mc_temp.answera, True, m.red_color)
            # answer b) is wrong, it will turn red 
            if answer_b_button != correct_button and event.type == m.pygame.MOUSEBUTTONDOWN and answer_b_button.mouse_on_button():
                m.wrong_answer_sound.play()
                mc_temp.answer_b = m.MagdaClean_font_50.render(mc_temp.answerb, True, m.red_color)
            # answer c) is wrong, it will turn red
            if answer_c_button != correct_button and event.type == m.pygame.MOUSEBUTTONDOWN and answer_c_button.mouse_on_button():
                m.wrong_answer_sound.play()
                mc_temp.answer_c = m.MagdaClean_font_50.render(mc_temp.answerc, True, m.red_color)
            # answer d) is wrong, it will turn red
            if answer_d_button != correct_button and event.type == m.pygame.MOUSEBUTTONDOWN and answer_d_button.mouse_on_button():
                m.wrong_answer_sound.play()
                mc_temp.answer_b = m.MagdaClean_font_50.render(mc_temp.answerd, True, m.red_color)
     
            

        m.pygame.display.update()