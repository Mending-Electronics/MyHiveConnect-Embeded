#Calibration Script

# Embeded variables
import _gain
global gain
print("***************************************")
print("Scale (Amplifier Gain)     : " + str(_gain.gain))

# Change Gain value in _var.py after calibration
def edit_gain(new_gain):
    global gain
    gain = new_gain
    with open('_gain.py', 'w') as f:
        f.write('gain = {}'.format(new_gain))
    return gain


# Scale Calibration
#.....

# Change the value of Gain from main.py
edit_gain(45)

# Verify that the value of Gain has changed
print("Scale (New Amplifier Gain) : " + str(gain))