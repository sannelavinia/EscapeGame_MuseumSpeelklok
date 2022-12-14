import main as m


def quit_game(event):
    """Quit game when pressing the close button "X" at the top-right of the game-window
    or the escape button on the keyboard"""

    if event.type == m.pygame.QUIT or (
        event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE
    ):
        return m.pygame.quit()
