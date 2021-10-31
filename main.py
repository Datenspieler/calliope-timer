def ZeigeZiffer(num: number, pos: number):
    global numTemp
    numTemp = num
    if numTemp > 5:
        led.plot(pos, 0)
        numTemp += -5
    led.plot(pos, 5 - numTemp)

def on_button_pressed_a():
    global t, ton, showTimer
    if statusNr == 0:
        t += 1 * 600
        ZeigeTimer(t)
    elif statusNr == 1:
        t += 1 * 60
        ZeigeTimer(t)
    elif statusNr == 2:
        t += 1 * 10
        ZeigeTimer(t)
    elif statusNr == 3:
        t += 1 * 1
        ZeigeTimer(t)
    elif statusNr == 4:
        ton = not (ton)
        if ton == True:
            basic.show_string("an")
        else:
            basic.show_string("aus")
    elif statusNr == 5:
        showTimer = not (showTimer)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global statusNr, tLast
    statusNr += 1
    if statusNr == 0:
        ZeigeTimer(t)
    if statusNr < 2:
        for index in range(4):
            led.toggle(statusNr, 0)
            basic.pause(100)
    elif statusNr < 4:
        for index2 in range(4):
            led.toggle(statusNr + 1, 0)
            basic.pause(100)
    elif statusNr == 4:
        basic.show_string("Ton:")
    elif statusNr == 5:
        ZeigeTimer(t)
        tLast = t
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def ZeigeTimer(tIn: number):
    global tTemp, tTemp2
    basic.clear_screen()
    tTemp = tIn
    tTemp2 = tTemp % 10
    ZeigeZiffer(tTemp2, 4)
    tTemp = (tTemp - tTemp2) / 10
    tTemp2 = tTemp % 6
    ZeigeZiffer(tTemp2, 3)
    tTemp = (tTemp - tTemp2) / 6
    tTemp2 = tTemp % 10
    ZeigeZiffer(tTemp2, 1)
    tTemp = (tTemp - tTemp2) / 10
    tTemp2 = tTemp % 6
    ZeigeZiffer(tTemp2, 0)
tTemp2 = 0
tTemp = 0
tLast = 0
numTemp = 0
showTimer = False
ton = False
statusNr = 0
t = 0
t = 0
statusNr = 0
statusTxtList = ["setze10Min",
    "setzeMin",
    "setze10Sek",
    "setzeSek",
    "setzeTon",
    "laufe",
    "abgelaufene"]
ton = False
showTimer = True
basic.clear_screen()
ZeigeTimer(t)
for index3 in range(4):
    led.toggle(0, 0)
    basic.pause(100)

def on_forever():
    global t, statusNr
    if statusNr == 5:
        basic.clear_screen()
        basic.set_led_color(0xff0000)
        if showTimer == True:
            ZeigeTimer(t)
        basic.pause(1000)
        t += -1
        if t == 0:
            statusNr += 1
    if statusNr == 6:
        basic.set_led_color(0x00ff00)
        basic.show_icon(IconNames.NO)
        if ton == True:
            for index4 in range(4):
                music.play_tone(523, music.beat(BeatFraction.WHOLE))
                basic.pause(100)
        statusNr = -1
        t = tLast
basic.forever(on_forever)
