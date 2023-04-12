import pyautogui

# Import local modules
from detect_image import click_on_discord


class AntiAFK():
    def __init__(self) -> None:
        self.historical_position = []

    def check_afk(self, time_limit:int=9) -> bool:
        time_limit = time_limit
        size_position = len(self.historical_position)

        if size_position > time_limit:
            while len(self.historical_position) > time_limit:
                self.historical_position.pop(0)
            size_position = len(self.historical_position)

        if size_position == time_limit:
            afk = 0
            for key in range(size_position - 1):
                x, y = self.historical_position[key]
                x1, y1 = self.historical_position[key+1]

                if (x == x1) and (y == y1):
                    afk += 1

            if afk == time_limit - 1:
                click_on_discord()
                return True

        return False


    def get_current_position(self) -> tuple:
        print(pyautogui.position())
        self.historical_position.append(pyautogui.position())
