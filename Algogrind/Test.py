import math

# Given values for the new capacitor
capacitance_microfarad_new = 76  # capacitance in microFarads
frequency_hz_new = 230           # frequency in Hz

# Convert capacitance to Farads
capacitance_farad_new = capacitance_microfarad_new * 10**-6  # convert microFarads to Farads

# Calculate impedance for the new capacitor
impedance_new = 1 / (2 * math.pi * frequency_hz_new * capacitance_farad_new)
print(impedance_new)