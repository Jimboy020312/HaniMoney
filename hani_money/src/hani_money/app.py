"""
HaniMoney is a simple and efficient finance tracker designed to help Hanisah manage her daily expenses effortlessly. With a quick-entry iOS widget, she can log spending without opening the app, categorizing transactions for better budgeting. All data is automatically compiled into an Excel file, making it easy to track and analyze financial habits over time.
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HaniMoney(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return HaniMoney()



