import main as m
import pygame

def multiplechoice_pq(game_number):
    if game_number:
        print('')
    black_screen_background = pygame.transform.scale(m.black_screen_background, (m.WIDTH, m.HEIGHT))

    while True:

        m.SCREEN.blit(black_screen_background, (0, 0))

        for event in m.pygame.event.get():

            # when pressing the close button "X" at the top-right of the game-window
            if event.type == m.pygame.QUIT or \
                    (event.type == m.pygame.KEYDOWN and event.key == m.pygame.K_ESCAPE):
                m.pygame.quit()

            if event.type == m.pygame.MOUSEBUTTONDOWN:
                return

        m.pygame.display.update()