import main as m
import pygame
import widgets.button as b

# from widgets.text_frame import Text_frame
from widgets.instruction_box import Instruction_Box
import widgets.text_frame as t
import widgets.quit_game as q


def spotdifferences_pq():
    # Scale the background and texts
    black_screen_background = pygame.transform.scale(
        m.black_screen_background, (m.WIDTH, m.HEIGHT)
    )
    # title = m.MagdaClean_font_50.render('Voorvraag 3', True, m.green_color)
    # title_rect = title.get_rect(center=(m.WIDTH/2, m.HEIGHT/14))

    # Get the explanation for prequestion 3
    explanation_text = (
        "Zoek de verschillen. Klik op de rechterafbeelding de verschillen aan."
    )
    prequestion_3_explanation = m.MagdaClean_font_30.render(
        explanation_text, True, m.green_color
    )
    prequestion_3_explanation_rect = prequestion_3_explanation.get_rect(
        center=(m.WIDTH / 2, m.HEIGHT / 7)
    )

    # Get the text that says you found all differences and can continue
    continue_text_string = "Goed zo! Tik op het scherm om verder te gaan."
    continue_text = m.MagdaClean_font_30.render(
        continue_text_string, True, m.green_color
    )
    continue_text_rect = continue_text.get_rect(center=(m.WIDTH / 2, m.HEIGHT / 7))

    # Get the spot_differences image with the right scale
    spot_differences_image = m.pygame.transform.scale(m.spot_differences, (1524, 857))
    spot_differences_rect = spot_differences_image.get_rect(
        center=(m.WIDTH / 2, m.HEIGHT / 1.8)
    )

    # Locations of differences are set in variables
    location_diff_1 = (1385, 273)
    location_diff_2 = (1253, 563)
    location_diff_3 = (1294, 753)
    location_diff_4 = (1356, 799)
    location_diff_5 = (1446, 737)
    location_diff_6 = (1565, 960)

    # Get red circle image and transparent image
    red_circle = m.red_circle
    difference_image = m.pygame.transform.scale(m.transparent_box, (60, 60))

    # Create invisible buttons for each difference
    difference_1_button = b.Button(
        difference_image,
        difference_image,
        difference_image,
        location_diff_1[0],
        location_diff_1[1],
        60,
        60,
    )
    difference_2_button = b.Button(
        difference_image,
        difference_image,
        difference_image,
        location_diff_2[0],
        location_diff_2[1],
        60,
        60,
    )
    difference_3_button = b.Button(
        difference_image,
        difference_image,
        difference_image,
        location_diff_3[0],
        location_diff_3[1],
        60,
        60,
    )
    difference_4_button = b.Button(
        difference_image,
        difference_image,
        difference_image,
        location_diff_4[0],
        location_diff_4[1],
        60,
        60,
    )
    difference_5_button = b.Button(
        difference_image,
        difference_image,
        difference_image,
        location_diff_5[0],
        location_diff_5[1],
        60,
        60,
    )
    difference_6_button = b.Button(
        difference_image,
        difference_image,
        difference_image,
        location_diff_6[0],
        location_diff_6[1],
        60,
        60,
    )

    # Make different red circle rects for each difference
    red_circle_rect_1 = red_circle.get_rect(
        center=(location_diff_1[0], location_diff_1[1])
    )
    red_circle_rect_2 = red_circle.get_rect(
        center=(location_diff_2[0], location_diff_2[1])
    )
    red_circle_rect_3 = red_circle.get_rect(
        center=(location_diff_3[0], location_diff_3[1])
    )
    red_circle_rect_4 = red_circle.get_rect(
        center=(location_diff_4[0], location_diff_4[1])
    )
    red_circle_rect_5 = red_circle.get_rect(
        center=(location_diff_5[0], location_diff_5[1])
    )
    red_circle_rect_6 = red_circle.get_rect(
        center=(location_diff_6[0], location_diff_6[1])
    )

    # Set up difference counter
    diff = 0  # keeps track of how many differences were found
    found_differences = [
        0,
        0,
        0,
        0,
        0,
        0,
    ]  # keeps track of which differences were found

    play_time_as_text = t.Text_frame(
        None,
        None,
        None,
        m.from_millisecond_to_clock(m.TOTAL_PLAY_TIME),
        m.green_color,
        m.Quantico_font_50,
        m.WIDTH / 9,
        m.HEIGHT / 11,
    )

    start_time = m.pygame.time.get_ticks()

    previous_second = int((m.TOTAL_PLAY_TIME / 1000) % 60)
    prequestion_on = True

    while True:

        # Display static elements of screen
        m.SCREEN.blit(black_screen_background, (0, 0))
        # m.SCREEN.blit(title, title_rect)
        m.SCREEN.blit(spot_differences_image, spot_differences_rect)

        # Display invisible buttons of differences
        difference_1_button.display()
        difference_2_button.display()
        difference_3_button.display()
        difference_4_button.display()
        difference_5_button.display()
        difference_6_button.display()

        # turn timer on when the pre questions are on
        if prequestion_on == True:

            play_time_as_text.display()
            end_time = m.pygame.time.get_ticks()
            time_difference = end_time - start_time

            play_time = m.TOTAL_PLAY_TIME + time_difference

            play_time_seconds = int((play_time / 1000) % 60)
            if play_time_seconds != previous_second:

                previous_second = play_time_seconds
                play_time_seconds = int((play_time / 1000) % 60)
                m.clock_tik.play()

            # m.TOTAL_PLAY_TIME += time_difference
            play_time_as_text.change_input_text(
                m.from_millisecond_to_clock(play_time), m.green_color
            )

        # Display red circle on places where a difference was found
        if found_differences[0] == 1:
            m.SCREEN.blit(red_circle, red_circle_rect_1)
        if found_differences[1] == 1:
            m.SCREEN.blit(red_circle, red_circle_rect_2)
        if found_differences[2] == 1:
            m.SCREEN.blit(red_circle, red_circle_rect_3)
        if found_differences[3] == 1:
            m.SCREEN.blit(red_circle, red_circle_rect_4)
        if found_differences[4] == 1:
            m.SCREEN.blit(red_circle, red_circle_rect_5)
        if found_differences[5] == 1:
            m.SCREEN.blit(red_circle, red_circle_rect_6)

        # update difference counter
        diff = found_differences.count(1)
        diff_counter = m.MagdaClean_font_30.render(
            f"Verschillen gevonden: {diff}/6", True, m.green_color
        )
        m.SCREEN.blit(diff_counter, (m.WIDTH / 1.3, m.HEIGHT / 15))

        # if all differences are found, the continue text should be displayed, else the info text
        if diff >= 6:
            m.SCREEN.blit(continue_text, continue_text_rect)
            prequestion_on = False
            m.TOTAL_PLAY_TIME = play_time
        else:
            m.SCREEN.blit(prequestion_3_explanation, prequestion_3_explanation_rect)

        for event in m.pygame.event.get():

            q.quit_game(event)

            # if the correct answer is chosen and you click on the screen you continue the game
            if event.type == m.pygame.MOUSEBUTTONDOWN and diff >= 6:
                return

            # For each difference, if it is found then the found_difference list will be updated
            # and the correct answer sound will be played.
            if (
                event.type == m.pygame.MOUSEBUTTONDOWN
                and difference_1_button.mouse_on_button()
                and found_differences[0] != 1
            ):
                m.correct_answer_sound.play()
                found_differences[0] = 1
                break  # go out of event for loop so that everything is correctly updated

            if (
                event.type == m.pygame.MOUSEBUTTONDOWN
                and difference_2_button.mouse_on_button()
                and found_differences[1] != 1
            ):
                m.correct_answer_sound.play()
                found_differences[1] = 1
                break  # go out of event for loop so that everything is correctly updated

            if (
                event.type == m.pygame.MOUSEBUTTONDOWN
                and difference_3_button.mouse_on_button()
                and found_differences[2] != 1
            ):
                m.correct_answer_sound.play()
                found_differences[2] = 1
                break  # go out of event for loop so that everything is correctly updated

            if (
                event.type == m.pygame.MOUSEBUTTONDOWN
                and difference_4_button.mouse_on_button()
                and found_differences[3] != 1
            ):
                m.correct_answer_sound.play()
                found_differences[3] = 1
                break  # go out of event for loop so that everything is correctly updated

            if (
                event.type == m.pygame.MOUSEBUTTONDOWN
                and difference_5_button.mouse_on_button()
                and found_differences[4] != 1
            ):
                m.correct_answer_sound.play()
                found_differences[4] = 1
                break  # go out of event for loop so that everything is correctly updated

            if (
                event.type == m.pygame.MOUSEBUTTONDOWN
                and difference_6_button.mouse_on_button()
                and found_differences[5] != 1
            ):
                m.correct_answer_sound.play()
                found_differences[5] = 1
                break  # go out of event for loop so that everything is correctly updated

        m.pygame.display.update()
