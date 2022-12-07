import unittest
from widgets.keyboard import Keyboard
from widgets.quit_game import quit_game

class WidgetTests(unittest.TestCase):

    def setUp(self) -> None:
        self.test_keyboard = Keyboard(200, 200)
        return super().setUp()

    def test(self):        
        """Test that is always true."""
        self.assertTrue(True)

    def test_keyboard_button_pressed(self):
        """Test whether the right numbers are inserted in the code."""
        for i in range(10):
            self.assertEqual(self.test_keyboard.keyboard_button_pressed(i, "123"), "123"+f"{i}")

    def test_keyboard_button_pressed_longcode(self):
        """Test whether no extra digits can be added to a code longer than 4 digits."""
        self.assertEqual(self.test_keyboard.keyboard_button_pressed(4, "1234"), "1234")
  
    def test_keyboard_delete_button(self):
        """Test whether a digit is deleted when the 11 button is pressed."""
        self.assertEqual(self.test_keyboard.keyboard_button_pressed(11, "12"), "1")
        self.assertEqual(self.test_keyboard.keyboard_button_pressed(11, "1234"), "123")

if __name__ == '__main__':
    unittest.main()
