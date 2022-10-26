import main as m
from widgets.text_frame import Text_frame
import widgets.keyboard as k


#######################################################################################
def start_window():

    metalic_background_logo = m.pygame.transform.scale(
        m.metal_plate_museumlogo, (m.WIDTH/2, m.HEIGHT))
    
    metalic_background__info_board = m.pygame.transform.scale(
        m.metal_plate_infoboard, (m.WIDTH/2, m.HEIGHT))
        
    one_screw = m.pygame.transform.scale(
        m.single_screw, (m.WIDTH/20, m.WIDTH/20))

    

    welkom_text_1 = Text_frame(None, None, None, "Welkom bij de",
                               m.white_color, m.code_font, m.WIDTH * 0.23, m.HEIGHT*0.42)
    welkom_text_2 = Text_frame(None, None, None, "Escaperoom van",
                               m.white_color, m.code_font, m.WIDTH * 0.245, m.HEIGHT*0.46)                           
    instruction_1 = Text_frame(None, None, None, "Voer de code in die je bij de ​",
                               m.black_color, m.start_font, m.WIDTH * 0.78, m.HEIGHT*0.2)
    instruction_2 = Text_frame(None, None, None, "balie hebt gekregen om het spel ​",
                               m.black_color, m.start_font, m.WIDTH * 0.78, m.HEIGHT*0.24 )
    instruction_3 = Text_frame(None, None, None, "te starten.​",
                               m.black_color, m.start_font, m.WIDTH * 0.77, m.HEIGHT*0.28 )
    #keyboard 

    keyboard = k.Keyboard(m.WIDTH * 0.68, m.HEIGHT * 0.52)



    button_pressed = False
    pressed_button = 99
    code = ""
    timer = 0




    # background music
    m.intro_sound.play()
    m.pygame.mixer.music.load("Assets/sounds/start.wav")
    m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # displaying the background images 

        m.SCREEN.blit(metalic_background_logo, (0, 0))
        m.SCREEN.blit(metalic_background__info_board, (m.WIDTH/2 , 0))

        #displaying the screws
        m.SCREEN.blit(one_screw, (m.WIDTH/40, m.HEIGHT/20))
        m.SCREEN.blit(one_screw, (m.WIDTH/2-(m.WIDTH/40) -
                      (m.WIDTH/20), m.HEIGHT/20))
        m.SCREEN.blit(one_screw, (m.WIDTH/2+(m.WIDTH/40), m.HEIGHT/20))
        m.SCREEN.blit(one_screw, (m.WIDTH-(m.WIDTH/40) -
                      (m.WIDTH/20), m.HEIGHT/20))
        m.SCREEN.blit(one_screw, (m.WIDTH/40, m.HEIGHT-(m.HEIGHT/20) -
                      (m.WIDTH/20)))
        m.SCREEN.blit(one_screw, (m.WIDTH/2-(m.WIDTH/40) -
                      (m.WIDTH/20), m.HEIGHT-(m.HEIGHT/20) -
                      (m.WIDTH/20)))
        m.SCREEN.blit(one_screw, (m.WIDTH/2+(m.WIDTH/40), m.HEIGHT-(m.HEIGHT/20)-
                      (m.WIDTH/20)))
        m.SCREEN.blit(one_screw, (m.WIDTH-(m.WIDTH/40) -
                      (m.WIDTH/20), m.HEIGHT-(m.HEIGHT/20) -
                      (m.WIDTH/20)))

        welkom_text_1.display()
        welkom_text_2.display()
        instruction_1.display()
        instruction_2.display()
        instruction_3.display()
        keyboard.display()

        # delay after clicking before resizing
        if button_pressed:
            timer += 1

        # resize the clicked button
        if timer >= int(m.button_resizing_delay / 3):

            # to the next window (if the code was correct)
            if pressed_button == 10:
                if code == m.game_1_code:
                    m.correct_answer_sound.play()
                    return
                else:
                    m.wrong_answer_sound.play()
            else:
                m.click_sound.play()
            code = keyboard.keyboard_button_pressed(pressed_button, code)

            # reset
            keyboard.resize_buttons()
            button_pressed = False
            pressed_button = 99
            timer = 0

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            # or the escape button on the keyboard
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.quit()


            if event.type == m.pygame.MOUSEBUTTONDOWN:
                pressed_button = keyboard.pressed_button()

                if pressed_button in range(0, 12):
                    button_pressed = True


            # # when pressing a mouse button
            # if event.type == m.pygame.MOUSEBUTTONDOWN and start_button.mouse_on_button():
            #     m.correct_answer_sound.play()
            #     return

        # the window should be updated after each while-loop
        m.pygame.display.update()