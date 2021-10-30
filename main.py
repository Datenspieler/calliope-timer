def on_button_pressed_a():
    global t
    if statusNr == 0:
        basic.show_string("" + (statusTxtList[statusNr]))
        t += 1 * 600
        ZeigeTimer(t)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def ZeigeTimer(t: number):
    basic.show_string(convert_to_text(t))
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
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
