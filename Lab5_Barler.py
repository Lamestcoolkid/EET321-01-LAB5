#Import Libraries
import pyvisa
import time
import pandas as pd

#sets up Pyvisa & makes address list
rm = pyvisa.ResourceManager()
addresses=rm.list_resources()
print(rm.list_resources())
# Use the addresses list determined above to open the currently
# available instruments for use.
for j in range(len(addresses)):
    if len(addresses[j])>=25:
        match addresses[j][22:25]:
            case 'SPD':
                supply = rm.open_resource(addresses[j])
            case 'SDM':
                dmm = rm.open_resource(addresses[j])
            case 'SDG':
                awg = rm.open_resource(addresses[j])
            case 'SDS':
                oscope = rm.open_resource(addresses[j])
            case _:
                print("No matching instrument")
#sets up input frequency
frequency=str(input("Enter Frequency:"))
awg.write('C1:BSWV FRQ,' + frequency)
voltage = str(input("Enter Voltage:"))
awg.write('C1:BSWV VOL,' + voltage)

#reads output frequency and amplitude
OSfrequency=oscope.write("C1:PAVA? FREQ")
OSamplitude=oscope.write("C1:PAVA? AMPL")

#reads DC values
DCvoltage=dmm.write("MEAS:VOLT:DC?")

#cuts value of readings to numerical values

#calculates Vripple and Ripple factor

