# open unity file (the end game)

import os


def open_end_game():
    if os.name == "nt":
        os.startfile("gears\\" + "My project (1).exe")
    elif os.name == "mac":
        print("mac")
    else:
        os.system("wine 'gears\\My project (1).exe'")
