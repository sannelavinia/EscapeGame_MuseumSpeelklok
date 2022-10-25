import main as m
from widgets.button import Button
from widgets.text_frame import Text_frame


#######################################################################################
def start_window():

    metalic_background_logo = m.pygame.transform.scale(
        m.metal_plate_museumlogo, (m.WIDTH/2, m.HEIGHT))
    
    metalic_background__info_board = m.pygame.transform.scale(
        m.metal_plate_infoboard, (m.WIDTH/2, m.HEIGHT))
        
    one_screw = m.pygame.transform.scale(
        m.single_screw, (m.WIDTH/20, m.WIDTH/20))


    # title_1 = Text_frame(None, None, None, "Escaperoom Museum", m.black_color,
    #                      m.code_font, (m.WIDTH / 2) + 50, (m.HEIGHT / 2) - 50)
    # title_2 = Text_frame(None, None, None, "Speelklok", m.black_color,
    #                      m.code_font, (m.WIDTH / 2) + 50, (m.HEIGHT / 2))
    # instruction_1 = Text_frame(None, None, None, "Klik op start om het spel te beginnen!",
    #                            m.black_color, m.main_font, (m.WIDTH / 2) + 50, (m.HEIGHT / 2) + 50)

    # background music
    m.intro_sound.play()
    m.pygame.mixer.music.load("Assets/sounds/start.wav")
    m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(metalic_background_logo, (0, 0))
        m.SCREEN.blit(metalic_background__info_board, (m.WIDTH/2 , 0))
        # title_1.display()
        # title_2.display()
        # instruction_1.display()
        # start_button.display()
        # logo.display()


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

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            # or the escape button on the keyboard
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.quit()

            # # when pressing a mouse button
            # if event.type == m.pygame.MOUSEBUTTONDOWN and start_button.mouse_on_button():
            #     m.correct_answer_sound.play()
            #     return

        # the window should be updated after each while-loop
        m.pygame.display.update()
