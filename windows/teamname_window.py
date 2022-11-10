import main as m
from widgets.button import Button
from widgets.text_frame import Text_frame
from pygame_vkeyboard import *

# Consumer created for onscreen keyboard
def consumer(text):
    print('current text: %s' %text)

def team_name_window():

    # Create the widgets to be displayed on the screen
    team_name = ""
    continue_button = Button(m.small_green_button, m.small_green_button, m.small_green_button,
                             (m.WIDTH*0.6), (m.HEIGHT*0.35), (m.WIDTH*0.03), (m.WIDTH*0.03))
    team_name_inputbox = Text_frame(m.white_input_field_teamname, m.WIDTH*0.35,
                                    m.HEIGHT*0.1, "", text_color=m.black_color, x_pos=0.5*m.WIDTH, y_pos=0.5*m.HEIGHT)
    black_screen_background = m.pygame.transform.scale(
        m.black_screen_background, (m.WIDTH, m.HEIGHT))
    continue_text = m.MagdaClean_font_70.render('Verder', True, m.green_color)
    continue_text_rect = continue_text.get_rect(center=(m.WIDTH*0.5, m.HEIGHT*0.35))
    enter_teamname_text = m.MagdaClean_font_70.render('Vul hier je teamnaam in!', True, m.green_color)
    enter_teamname_text_rect = enter_teamname_text.get_rect(center=(m.WIDTH*0.5, m.HEIGHT*0.25))
 

    # Initialize keyboard
    layout = VKeyboardLayout(VKeyboardLayout.AZERTY)
    keyboard = VKeyboard(m.SCREEN, consumer, layout, True, renderer=VKeyboardRenderer.DARK)

    # game loop ( to prevent the window from closing )
    while True:

        # display the background image and the widgets, first the background and the rest on top
        m.SCREEN.blit(black_screen_background, (0, 0))
        #team_name_inputbox.display()
        continue_button.display()
        m.SCREEN.blit(continue_text, continue_text_rect)
        m.SCREEN.blit(enter_teamname_text, enter_teamname_text_rect)

        # Indicates that you can now type input, should display a keyboard on screen if necessary
        m.pygame.key.start_text_input()

        events = m.pygame.event.get()

        # update keyboard events
        keyboard.update(events)

        keyboard.draw(m.SCREEN, True)

        m.SCREEN.blit(m.museum_logo_grey, (m.WIDTH*0.85, m.HEIGHT*0.9))

        # every interaction with the game is an event ( mouse, Keyboard )
        for event in events:

            # when pressing the close button "X" or at the top-right of the game-window or escape key
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.key.stop_text_input()
                m.pygame.quit()

            # when pressing the continue key
            if event.type == m.pygame.MOUSEBUTTONDOWN and continue_button.mouse_on_button():
                m.pygame.key.stop_text_input()
                return

            if event.type == m.pygame.TEXTINPUT:
                # text
                if len(team_name) >= 20:
                    continue

                else:
                    team_name = team_name_inputbox.input_text + event.text
                    team_name_inputbox.change_input_text(team_name)

            if event.type == m.pygame.KEYDOWN:
                if event.key == m.pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    if team_name == "":
                        continue
                    else:
                        team_name_inputbox.change_input_text(team_name[:-1])
                        team_name = team_name[:-1]

        # the window should be updated after each while-loop
        m.pygame.display.update()
