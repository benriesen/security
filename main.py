# First security sensor

def on_button_pressed_a():
    basic.show_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

# Resets it back to normal

def on_button_pressed_b():
    basic.show_string("")
input.on_button_pressed(Button.B, on_button_pressed_b)

# Second Security Sensor

def on_forever():
    if input.is_gesture(Gesture.SHAKE):
        basic.show_string("SHAKE PROBLEM")
basic.forever(on_forever)
