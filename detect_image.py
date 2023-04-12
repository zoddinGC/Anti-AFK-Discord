import pyautogui
from time import sleep
from PIL import Image


def click_on_image(x1, y1, x2, y2, image, add_x:bool=False):
    try:
        x1, y1, x2, y3 = pyautogui.locateOnScreen(
            image,
            region=(x1, y1, x2, y2),
        )

        if add_x:
            x1 += 70

        pyautogui.moveTo((x1, y1, x2, y3), duration=0.3)
        pyautogui.click()

    except TypeError:
        print('Programa bom (ironia)')


def click_on_discord():
    image = Image.open('images/chrome_not_selected.png')
    width, height = pyautogui.size()

    x1, x2 = (width // 2) - width // 5, (width // 2) + width // 8
    y1, y2 = height - height // 10, height - 1

    click_on_image(x1, y1, x2, y2, image, add_x=True)

    image = Image.open('images/discord_not_selected.png')

    x1, x2 = 0, (width // 2)
    y1, y2 = 0, 50

    click_on_image(x1, y1, x2, y2, image)
