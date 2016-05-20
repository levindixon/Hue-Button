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

os.system('node turnAllOff.js')
os.system('node turnAllOn.js')
os.system('node turnAllOff.js')

oneOn = false
twoOn = false
threeOn = false
fourOn = false
fiveOn = false
sixOn = false
sevenOn = false

while True:
    toggleOneChanged = GPIO.input(toggleOne) is not toggleOneLastState
    toggleTwoChanged = GPIO.input(toggleTwo) is not toggleTwoLastState
    toggleThreeChanged = GPIO.input(toggleThree) is not toggleThreeLastState
    toggleFourChanged = GPIO.input(toggleFour) is not toggleFourLastState
    toggleFiveChanged = GPIO.input(toggleFive) is not toggleFiveLastState
    toggleSixChanged = GPIO.input(toggleSix) is not toggleSixLastState
    toggleSevenChanged = GPIO.input(toggleSeven) is not toggleSevenLastState

    if toggleOneChanged:
        print "Toggle one flipped!"
        toggleOneLastState = GPIO.input(toggleOne)
        oneOn = not oneOn
        if oneOn:
            print "Turning on light!"
            os.system('node toggle.js 4 on')
        elif not oneOn:
            print "Turning off light!"
            os.system('node toggle.js 4 off')
    elif toggleTwoChanged:
        print "Toggle two flipped!"
        toggleTwoLastState = GPIO.input(toggleTwo)
        twoOn = not twoOn
        if twoOn:
            print "Turning on light!"
            os.system('node toggle.js 3 on')
        elif not twoOn:
            print "Turning off light!"
            os.system('node toggle.js 3 off')
    elif toggleThreeChanged:
        print "Toggle three flipped!"
        toggleThreeLastState = GPIO.input(toggleThree)
        threeOn = not threeOn
        if threeOn:
            print "Turning on light!"
            os.system('node toggle.js 5 on')
        elif not threeOn:
            print "Turning off light!"
            os.system('node toggle.js 5 off')
    elif toggleFourChanged:
        print "Toggle four flipped!"
        toggleFourLastState = GPIO.input(toggleFour)
        fourOn = not fourOn
        if fourOn:
            print "Turning on light!"
            os.system('node toggle.js 6 on')
        elif not fourOn:
            print "Turning off light!"
            os.system('node toggle.js 6 off')
    elif toggleFiveChanged:
        print "Toggle five flipped!"
        toggleFiveLastState = GPIO.input(toggleFive)
        fiveOn = not fiveOn
        if fiveOn:
            print "Turning on light!"
            os.system('node toggle.js 7 on')
        elif not fiveOn:
            print "Turning off light!"
            os.system('node toggle.js 7 off')
    elif toggleSixChanged:
        print "Toggle six flipped!"
        toggleSixLastState = GPIO.input(toggleSix)
        sixOn = not sixOn
        if sixOn:
            print "Turning on light!"
            os.system('node toggle.js 2 on')
        elif not sixOn:
            print "Turning off light!"
            os.system('node toggle.js 2 off')
    elif toggleSevenChanged:
        print "Toggle seven flipped!"
        toggleSevenLastState = GPIO.input(toggleSeven)
        sevenOn = not sevenOn
        if sevenOn:
            print "Turning on light!"
            os.system('node toggle.js 1 on')
        elif not sevenOn:
            print "Turning off light!"
            os.system('node toggle.js 1 off')

    time.sleep(0.01)

GPIO.cleanup()
