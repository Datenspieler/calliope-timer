function ZeigeZiffer (num: number, pos: number) {
    numTemp = num
    if (numTemp > 5) {
        led.plot(pos, 0)
        numTemp += -5
    }
    led.plot(pos, 5 - numTemp)
}
input.onButtonPressed(Button.A, function () {
    if (statusNr == 0) {
        t += 1 * 600
        t = t % 5400
        ZeigeTimer(t)
    } else if (statusNr == 1) {
        t += 1 * 60
        t = t % 600
        ZeigeTimer(t)
    } else if (statusNr == 2) {
        t += 1 * 10
        t = t % 60
        ZeigeTimer(t)
    } else if (statusNr == 3) {
        t += 1 * 1
        t = t % 10
        ZeigeTimer(t)
    } else if (statusNr == 4) {
        ton = !(ton)
        if (ton == true) {
            basic.showString("an")
        } else {
            basic.showString("aus")
        }
    } else if (statusNr == 5) {
        showTimer = !(showTimer)
    } else {
    	
    }
})
input.onButtonPressed(Button.B, function () {
    statusNr += 1
    if (statusNr == 0) {
        ZeigeTimer(t)
    }
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
    } else if (statusNr == 4) {
        basic.showString("Ton:")
    } else if (statusNr == 5) {
        ZeigeTimer(t)
        tLast = t
    } else {
    	
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
    tTemp2 = tTemp % 10
    ZeigeZiffer(tTemp2, 0)
}
let tTemp2 = 0
let tTemp = 0
let tLast = 0
let numTemp = 0
let showTimer = false
let ton = false
let statusNr = 0
let t = 0
t = 0
statusNr = 0
let statusTxtList = ["setze10Min", "setzeMin", "setze10Sek", "setzeSek", "setzeTon", "laufe", "abgelaufene"]
ton = false
showTimer = true
basic.clearScreen()
ZeigeTimer(t)
for (let index = 0; index < 4; index++) {
    led.toggle(0, 0)
    basic.pause(100)
}
basic.forever(function () {
    if (statusNr == 5) {
        basic.clearScreen()
        basic.setLedColor(0xff0000)
        if (showTimer == true) {
            ZeigeTimer(t)
        }
        basic.pause(1000)
        t += -1
        if (t == 0) {
            statusNr += 1
        }
    }
    if (statusNr == 6) {
        basic.setLedColor(0x00ff00)
        basic.showIcon(IconNames.No)
        if (ton == true) {
            for (let index = 0; index < 4; index++) {
                music.playTone(523, music.beat(BeatFraction.Whole))
                basic.pause(100)
            }
        }
        statusNr = -1
        t = tLast
    }
})
