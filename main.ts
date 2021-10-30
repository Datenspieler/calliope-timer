function ZeigeZiffer (num: number, pos: number) {
    numTemp = num
    if (numTemp > 5) {
        led.plot(pos, 0)
        numTemp += -5
    }
    led.plot(pos, 5 - numTemp)
}
input.onPinPressed(TouchPin.P0, function () {
    statusNr += -1
    if (statusNr < 2) {
        for (let index = 0; index < 4; index++) {
            led.toggle(statusNr, 0)
            basic.pause(100)
        }
    } else if (statusNr < 4) {
        for (let index = 0; index < 4; index++) {
            led.toggle(statusNr + 1, 0)
            basic.pause(100)
        }
    } else {
        basic.showString("" + (statusTxtList[statusNr]))
    }
})
input.onButtonPressed(Button.A, function () {
    if (statusNr == 0) {
        t += 1 * 600
        ZeigeTimer(t)
    } else if (statusNr == 1) {
        t += 1 * 60
        ZeigeTimer(t)
    } else if (statusNr == 2) {
        t += 1 * 10
        ZeigeTimer(t)
    } else if (statusNr == 3) {
        t += 1 * 1
        ZeigeTimer(t)
    } else if (statusNr == 4) {
        ton = !(ton)
        basic.showString(convertToText(ton))
    } else {
    	
    }
})
input.onButtonPressed(Button.B, function () {
    statusNr += 1
    if (statusNr < 2) {
        for (let index = 0; index < 4; index++) {
            led.toggle(statusNr, 0)
            basic.pause(100)
        }
    } else if (statusNr < 4) {
        for (let index = 0; index < 4; index++) {
            led.toggle(statusNr + 1, 0)
            basic.pause(100)
        }
    } else {
        basic.showString("" + (statusTxtList[statusNr]))
    }
})
function ZeigeTimer (tIn: number) {
    basic.clearScreen()
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
}
let tTemp2 = 0
let tTemp = 0
let numTemp = 0
let ton = false
let statusTxtList: string[] = []
let statusNr = 0
let t = 0
t = 10
statusNr = 0
statusTxtList = ["setze10Min", "setzeMin", "setze10Sek", "setzeSek", "setzeTon", "laufe", "abgelaufene"]
ton = false
basic.clearScreen()
ZeigeTimer(t)
basic.forever(function () {
	
})
