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
    black_screen_background = m.pygame.transform.scale(
        m.black_screen_background, (m.WIDTH, m.HEIGHT))
    continue_text = m.MagdaClean_font_70.render('Verder', True, m.green_color)
    continue_text_rect = continue_text.get_rect(center=(m.WIDTH*0.5, m.HEIGHT*0.35))
    enter_teamname_text = m.MagdaClean_font_70.render('Vul hier je teamnaam in!', True, m.green_color)
    enter_teamname_text_rect = enter_teamname_text.get_rect(center=(m.WIDTH*0.5, m.HEIGHT*0.25))

    # Initialize keyboard
    layout = VKeyboardLayout(VKeyboardLayout.QWERTY)
    keyboard = VKeyboard(m.SCREEN, consumer, layout, True, renderer=VKeyboardRenderer.DARK)

    # game loop ( to prevent the window from closing )
    while True:

        # display the background image and the widgets, first the background and the rest on top
        m.SCREEN.blit(black_screen_background, (0, 0))
        continue_button.display()
        m.SCREEN.blit(continue_text, continue_text_rect)
        m.SCREEN.blit(enter_teamname_text, enter_teamname_text_rect)

        events = m.pygame.event.get()

        # Update keyboard events
        keyboard.update(events)

        # Make sure that the length of the teamname is not longer than 30
        if len(keyboard.get_text()) >= 30:
                keyboard.set_text(keyboard.get_text()[:-1])

        # Draw keyboard on the screen
        keyboard.draw(m.SCREEN, True)

        # Museum logo should be visible on keyboard
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
                # if there is no teamname the message that a teamname should be entered is displayed in red
                if len(keyboard.get_text()) == 0:
                    m.wrong_answer_sound.play()
                    enter_teamname_text = m.MagdaClean_font_70.render('Vul hier je teamnaam in!', True, m.red_color)
                    enter_teamname_text_rect = enter_teamname_text.get_rect(center=(m.WIDTH*0.5, m.HEIGHT*0.25))
                else:
                    team_name = keyboard.get_text()
                    return
            
            if len(keyboard.get_text()) > 0:
                enter_teamname_text = m.MagdaClean_font_70.render('Vul hier je teamnaam in!', True, m.green_color)
                enter_teamname_text_rect = enter_teamname_text.get_rect(center=(m.WIDTH*0.5, m.HEIGHT*0.25))

        # the window should be updated after each while-loop
        m.pygame.display.update()
