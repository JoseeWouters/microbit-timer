from microbit import *

while True:
    if button_a.is_pressed(): #the loop begins after pressing A
        display.clear()
        for x in range(0, 5):
            for y in range(0, 5):
                display.set_pixel(x,y,9)
                sleep(30000) #interval between putting on the leds
        display.clear()
        sleep(500)
        while True:
            display.show(Image.HAPPY)
            sleep(500)
            display.clear()
            sleep(500)
            if button_b.is_pressed(): #stop the end animation
                break
        display.clear()