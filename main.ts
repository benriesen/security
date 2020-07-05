// First security sensor
input.onButtonPressed(Button.A, function () {
    basic.showString("A")
})
// Resets it back to normal
input.onButtonPressed(Button.B, function () {
    basic.showString("")
})
// Second Security Sensor
basic.forever(function () {
    if (input.isGesture(Gesture.Shake)) {
        basic.showString("SHAKE PROBLEM")
    }
})
