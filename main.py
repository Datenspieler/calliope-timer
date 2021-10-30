def ZeigeZiffer(num: number, pos: number):
    global numTemp
    numTemp = num
    if numTemp > 5:
        led.plot(pos, 0)
        numTemp += -5
    led.plot(pos, 5 - numTemp)

def on_pin_pressed_p0():
    global statusNr
    statusNr += -1
    if statusNr < 2:
        for index in range(4):
            led.toggle(statusNr, 0)
            basic.pause(100)
    elif statusNr < 4:
        for index2 in range(4):
            led.toggle(statusNr + 1, 0)
            basic.pause(100)
    else:
        basic.show_string("" + (statusTxtList[statusNr]))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global t, ton
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
        basic.show_string(convert_to_text(ton))
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global statusNr
    statusNr += 1
    if statusNr < 2:
        for index3 in range(4):
            led.toggle(statusNr, 0)
            basic.pause(100)
    elif statusNr < 4:
        for index4 in range(4):
            led.toggle(statusNr + 1, 0)
            basic.pause(100)
    else:
        basic.show_string("" + (statusTxtList[statusNr]))
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
numTemp = 0
ton = False
statusTxtList: List[str] = []
statusNr = 0
t = 0
t = 10
statusNr = 0
statusTxtList = ["setze10Min",
    "setzeMin",
    "setze10Sek",
    "setzeSek",
    "setzeTon",
    "laufe",
    "abgelaufene"]
ton = False
basic.clear_screen()
ZeigeTimer(t)

def on_forever():
    pass
basic.forever(on_forever)
