import RPi.GPIO as GPIO
import os
import time

print "Running Hue Button"

toggleOne = 29
toggleTwo = 31
toggleThree = 32
toggleFour = 33
toggleFive = 35
toggleSix = 36
toggleSeven = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup([toggleOne, toggleTwo, toggleThree, toggleFour, toggleFive, toggleSix, toggleSeven], GPIO.IN)

toggleOneLastState = GPIO.input(toggleOne)
toggleTwoLastState = GPIO.input(toggleTwo)
toggleThreeLastState = GPIO.input(toggleThree)
toggleFourLastState = GPIO.input(toggleFour)
toggleFiveLastState = GPIO.input(toggleFive)
toggleSixLastState = GPIO.input(toggleSix)
toggleSevenLastState = GPIO.input(toggleSeven)

while True:
    toggleOneChanged = GPIO.input(toggleOne) is not toggleOneLastState
    toggleTwoChanged = GPIO.input(toggleTwo) is not toggleTwoLastState
    toggleThreeChanged = GPIO.input(toggleThree) is not toggleThreeLastState
    toggleFourChanged = GPIO.input(toggleFour) is not toggleFourLastState
    toggleFiveChanged = GPIO.input(toggleFive) is not toggleFiveLastState
    toggleSixChanged = GPIO.input(toggleSix) is not toggleSixLastState
    toggleSevenChanged = GPIO.input(toggleSeven) is not toggleSevenLastState

    if toggleOneChanged:
        print "Toggle One"
        toggleOneLastState = GPIO.input(toggleOne)
        os.system('node toggle.js 4')
    elif toggleTwoChanged:
        print "Toggle Two"
        toggleTwoLastState = GPIO.input(toggleTwo)
        os.system('node toggle.js 3')
    elif toggleThreeChanged:
        print "Toggle Three"
        toggleThreeLastState = GPIO.input(toggleThree)
        os.system('node toggle.js 5')
    elif toggleFourChanged:
        print "Toggle Four"
        toggleFourLastState = GPIO.input(toggleFour)
        os.system('node toggle.js 6')
    elif toggleFiveChanged:
        print "Toggle Five"
        toggleFiveLastState = GPIO.input(toggleFive)
        os.system('node toggle.js 7')
    elif toggleSixChanged:
        print "Toggle Six"
        toggleSixLastState = GPIO.input(toggleSix)
        os.system('node toggle.js 2')
    elif toggleSevenChanged:
        print "Toggle Seven"
        toggleSevenLastState = GPIO.input(toggleSeven)
        os.system('node toggle.js 1')

    time.sleep(0.01)

GPIO.cleanup()