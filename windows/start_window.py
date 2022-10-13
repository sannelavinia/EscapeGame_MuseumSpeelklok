import main as m
from widgets.massage_box import Massage_box
from widgets.button import Button
from widgets.code_frame import Text_frame


#######################################################################################
def start_window():

    # massage = Massage_box(m.message, 400, 300, m.text_1,
    #                       m.white_color, 400, 300)
    start_window_museum_logo = m.pygame.image.load("Assets/images/start_window_museum_logo.png")
    start_window_museum_logo = m.pygame.transform.scale(start_window_museum_logo, (120, 36))
    logo = Button(start_window_museum_logo, start_window_museum_logo, start_window_museum_logo, m.WIDTH - 70, m.HIGHT - 25)
    start_button = Button(m.button_start, m.button_start, m.button_start, m.WIDTH / 2, m.HIGHT * 2/3 )

    title_1 = Text_frame(None, "Escaperoom Museum", m.black_color, m.code_font, (m.WIDTH / 2) + 50, (m.HIGHT / 2) - 50 )
    title_2 = Text_frame(None, "Speelklok", m.black_color, m.code_font, (m.WIDTH / 2) + 50, (m.HIGHT / 2) )
    instruction_1 = Text_frame(None, "Klik op start om het spel te beginnen!", m.black_color, m.main_font, (m.WIDTH / 2) + 50, (m.HIGHT / 2) + 50 )

    # background music
    m.intro_sound.play()
    m.pygame.mixer.music.load("Assets/sounds/start.wav")
    m.pygame.mixer.music.play(-1)  # play the music in an infinite loop

    # game loop ( to prevent the window from closing after going throw the current events )
    while True:

        # display the background image ( it should be the fisrt image to display,
        # so that the other objects will be displayed ontop of it )
        m.SCREEN.blit(m.background_start, (0, 0))
        # massage.display()
        title_1.display()
        title_2.display()
        instruction_1.display()
        start_button.display()
        logo.display()

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.QUIT:
                m.pygame.quit()

            # when pressing a mouse button
            if event.type == m.pygame.MOUSEBUTTONDOWN and start_button.mouse_on_button():
                m.correct_answer_sound.play()
                return

        # the window should be updated after each while-loop
        m.pygame.display.update()
