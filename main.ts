input.onButtonPressed(Button.A, function () {
    basic.showString("" + (statusTxtList[statusNr]))
    if (statusNr == 0) {
        t += 1 * 600
        ZeigeTimer(t)
    } else if (statusNr == 1) {
        t += 1 * 60
        ZeigeTimer(t)
    } else {
    	
    }
})
function ZeigeTimer (t0: number) {
    basic.showString(convertToText(t0))
}
let statusTxtList: string[] = []
let statusNr = 0
let t = 0
t = 10
statusNr = 0
statusTxtList = ["setze10Min", "setzeMin", "setze10Sek", "setzeSek", "setzeTon", "laufe", "abgelaufene"]
basic.clearScreen()
basic.forever(function () {
	
})
