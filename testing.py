import unittest
from unittest.mock import Mock
import tkinter as tk
from GUI import LoginWindow


class TestGUI(unittest.TestCase):

    def start(self):
        """Start the testing environment."""
        self.root = tk.Tk()
        self.gui = LoginWindow(self.root)
        self.gui.login = Mock(name='login')

    def end(self):
        """End the GUI after each test is run."""
        self.root.destroy()

    def test_login_true(self):
        """Test the login functionality is correct by using the correct login credentials."""
        # Predefined username and password entries (only one solution).
        self.gui.entry_username.insert(0, 'admin')
        self.gui.entry_password.insert(0, 'cct211')

        # Press the login button.
        self.gui.button.invoke()
        # Check that the login was called.
        self.gui.login.assert_called_once()

    def test_when_fail(self):
        """Test when the login was purposely incorrect using the wrong the login credentials."""
        self.gui.entry_username.insert(0, 'abc')
        self.gui.entry_password.insert(0, '123')

        # Press the login button
        self.gui.button.invoke()

        # Check that the login was called.
        self.gui.login.assert_called_once()


if __name__ == '__main__':
    unittest.main()
