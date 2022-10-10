import main as m
from widgets.massage_box import Massage_box

#######################################################################################


def explanation_window():

    massage = Massage_box(m.message, 400, 300, m.text_2,
                          m.black_color, 400, 300)
    # background music
    # m.intro_sound.play()
    # m.pygame.mixer.music.load("Assets/sounds/start.wav")
    # m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(m.background_gears, (0, 0))
        massage.display()

        #display yellow title bar
        m.SCREEN.blit(m.yellowbar, (0,30))
        title1 = m.speelklok_website_font.render('Spelregels', True, m.black_color)
        text_rect_title1 = title1.get_rect(center=(m.WIDTH/2, (m.HIGHT/2)-255))
        m.SCREEN.blit(title1, text_rect_title1)

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
