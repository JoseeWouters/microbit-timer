from microbit import *

while True:
    if button_a.is_pressed():
        display.clear()
        for x in range(0, 5):
            for y in range(0, 5):
                display.set_pixel(x,y,9)
                sleep(3000)
        display.clear()