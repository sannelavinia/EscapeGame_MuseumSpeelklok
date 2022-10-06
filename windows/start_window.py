import main as m


#######################################################################################
def start_window():

    text, message_box = m.render_text(m.text_1, m.white_color, 400, 300)

    # background music
    m.intro_sound.play()
    m.pygame.mixer.music.load("Assets/sounds/start.wav")
    m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(m.background_start, (0, 0))

        m.display_text(message_box, text, 800, 100)

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.QUIT:
                m.pygame.quit()

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN:
                m.correct_answer_sound.play()
                return

        # the window should be updated after each while-loop
        m.pygame.display.update()
