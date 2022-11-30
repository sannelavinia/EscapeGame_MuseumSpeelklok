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

    thinking_boy = pygame.transform.scale(m.thinking_boy, (1433 * 0.15, 1556 * 0.15))
    thinking_girl = pygame.transform.scale(m.thinking_girl, (1768 * 0.15, 1669 * 0.15))

    # Multiple choice prequestion 1 text
    if game_number == 1:
        mc_temp( m.prequestion_1, m.prequestion_1b, 'a) Slinger', 'b) Klepel', 'c) Was', 'd) Lepel')
        buttonwidth = 205
        button_y = m.WIDTH/4
        answer_a_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/2.30, buttonwidth, 60)
        answer_b_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.90, buttonwidth, 60)
        answer_c_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.57, buttonwidth, 60)
        answer_d_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.33, buttonwidth, 60)
        correct_button = answer_b_button
    if game_number == 2:
        mc_temp(m.prequestion_2, m.prequestion_2b, 'a) Een worst', 'b) Gouden bergen', 'c) Een jurk', 'd) Een spiegel')
        buttonwidth = 370
        button_y = m.WIDTH/3.5
        answer_a_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/2.30, buttonwidth, 60)
        answer_b_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.90, buttonwidth, 60)
        answer_c_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.57, buttonwidth, 60)
        answer_d_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.33, buttonwidth, 60)
        correct_button = answer_d_button
    if game_number == 4:
        mc_temp(m.prequestion_4, m.prequestion_4b, 'a) 2 tegen de klok in, 4 tegen de klok in', 'b) 4 met de klok mee, 2 tegen de klok in', 'c) 2 met de klok mee, 4 met de klok mee', 'd) 4 met de klok mee, 2 draait niet')
        buttonwidth = 1050
        button_y = m.WIDTH/2.2
        answer_a_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/2.30, buttonwidth, 60)
        answer_b_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.90, buttonwidth, 60)
        answer_c_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.57, buttonwidth, 60)
        answer_d_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.33, buttonwidth, 60)
        correct_button = answer_b_button
        gears_pq4 = m.pygame.transform.scale(m.gears_pq4, (608 * 0.65, 454 * 0.65)
    )
    if game_number == 5:
        mc_temp(m.prequestion_5, m.prequestion_5b, 'a) dat de muziek is opgenomen en wordt afgespeeld', 'b) dat de muziek ter plekke wordt gespeeld', '', '')
        buttonwidth = 1300
        button_y = m.WIDTH/2.0
        answer_a_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.90, buttonwidth, 60)
        answer_b_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, button_y, m.HEIGHT/1.60, buttonwidth, 60)
        answer_c_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, 0, 0, 0, 0)
        answer_d_button = b.Button(m.transparent_box, m.transparent_box, m.transparent_box, 0, 0, 0, 0)
        correct_button = answer_b_button


    

    while True:
        
        m.SCREEN.blit(black_screen_background, (0, 0))
        m.SCREEN.blit(title, title_rect)

        mc_temp.prequestion.display()

        if game_number == 5:
            answer_height1 = m.HEIGHT/2.0
            answer_height2 = m.HEIGHT/1.68
        else:
            answer_height1 = m.HEIGHT/2.5
            answer_height2 = m.HEIGHT/1.98
        m.SCREEN.blit(mc_temp.answer_a, (m.WIDTH/5, answer_height1))
        m.SCREEN.blit(mc_temp.answer_b, (m.WIDTH/5, answer_height2))
        m.SCREEN.blit(mc_temp.answer_c, (m.WIDTH/5, m.HEIGHT/1.65))
        m.SCREEN.blit(mc_temp.answer_d, (m.WIDTH/5, m.HEIGHT/1.39))

        answer_a_button.display()
        answer_b_button.display()
        answer_c_button.display()
        answer_d_button.display() 

        m.SCREEN.blit(thinking_boy, (m.WIDTH*0.05,m.HEIGHT*0.75))
        m.SCREEN.blit(thinking_girl, (m.WIDTH*0.85,m.HEIGHT*0.75))

        if game_number == 4:
            m.SCREEN.blit(gears_pq4,(m.WIDTH*0.76,m.HEIGHT*0.45))

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
                thinking_boy = m.transparent_box
                thinking_girl = m.transparent_box
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
                mc_temp.answer_d = m.MagdaClean_font_50.render(mc_temp.answerd, True, m.red_color)
     
            

        m.pygame.display.update()