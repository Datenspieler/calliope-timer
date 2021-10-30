def on_button_pressed_a():
    global t
    basic.show_string("" + (statusTxtList[statusNr]))
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
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def ZeigeTimer(t0: number):
    basic.show_string(convert_to_text(t0))
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

def on_forever():
    pass
basic.forever(on_forever)
