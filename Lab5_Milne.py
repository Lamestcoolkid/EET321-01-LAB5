# John Milne
# EET 321
# 04/09/2026
# Lab #5
# Group 3 with Lucas Larson and James Barler

# Instructions:
# Step 1: Configure the Test Equipment.
# 	a. Set the function generator to generate a 5V amplitude sine wave at 50 Hz.
# 	b. Configure the oscilloscope to capture the output waveform.
# 	c. Use the DMM to measure the DC voltage and ripple voltage.
#
# Step 2: Develop the Python Script.
# 	a. Control the function generator to set the frequency and amplitude.
# 	b. Capture the output waveform using the oscilloscope.
# 	c. Measure the DC voltage and ripple voltage using the DMM.
# 	d. Calculate the ripple factor using the formulas:
#
# 	    Vripple:
#       √((V_rms^2-V_DC^2 ) )
#
#    	Ripple Factor:
#       V_ripple/V_DC
#
# 	Repeat the measurements for different frequencies (50 Hz, 60 Hz, 120 Hz, 1 kHz)
# 	and capacitors (100 µF and 470 µF) and load resistors (510 Ohm, 2kOhm).
# 	Save the data (frequency, capacitor value, DC voltage, ripple voltage, ripple factor)
# 	to an Excel file.

# Installation process to get the correct libraries installed before trying to import them.
from install import install

# Holds the names of libraries to be installed
libraries = ["pyvisa", "numpy", "pandas", "openpyxl"]

# Following code loops the install function to download all requested libraries.
for i in range(len(libraries)):
    install(libraries[i])

# Imports of Import
from detect_Instruments import detect_instruments
from math import sqrt
from time import sleep
import openpyxl
import pandas as pd
import pyvisa


# Set up the instruments
[supply, fungen, dmm, oscope] = detect_instruments()

# Setup the initial conditions for the instruments.
oscope.write("C1:CPL A1M")
sleep(2)

# Set up the DMM to take a measurement.
dmm.read_termination = "\n"
dmm.write_termination = "\n"
dmm.write("CHDR OFF")
sleep(2)

# Variables
counter = 0
freqs = [50, 60, 120, 1000]

# Create the Excel spreadsheet.
# Change the name of the file between each run to show the Res/Cap used.
filepath = ("./Group3Lab5Data2000-100.xlsx")
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "Group3Lab5Data"
workbook.save(filepath)
worksheet['A1'] = "Frequency"
worksheet['B1'] = "Oscilloscope"
worksheet['C1'] = "DMM"
worksheet['D1'] = "Ripple"
worksheet['E1'] = "Factor"
workbook.save(filepath)

# FOR-loop to take the measurements over several frequencies.
for frequency in freqs:

    # Set up the function generator to produce the required 5 volt sine wave at a given f.
    fungen.write("C1:BSWV WVTP,SIN")
    fungen.write(f"C1:BSWV FRQ,{frequency}")
    fungen.write("C1:BSWV AMP,5")
    fungen.write("C1:OUTP ON")

    # Set up the oscilloscope to take a measurement.
    oscope.write("PACU RMS,C1")
    sleep(2)

    # Take measurements.
    Vrms = round(float(oscope.query(f"C1:PAVA? RMS").split(",")[1].strip("V\n")),6)
    Vdc = round(float(dmm.query("MEAS:VOLT:DC?")),6)
    print(f"Oscilloscope: {Vrms}\tDMM: {Vdc}")
    Ripple = round(sqrt(((Vrms*Vrms) + (Vdc*Vdc)) - (Vdc*Vdc)),6)
    Factor = round(Ripple/Vdc,6)
    print(f"VRipple: {Ripple}\tRipple Factor: {Factor}")
    Factors = pd.DataFrame(columns=["Frequency","Oscilloscope","DMM","VRipple","RFactor"])
    worksheet[f"A{counter+2}"] = frequency
    worksheet[f"B{counter+2}"] = Vrms
    worksheet[f"C{counter+2}"] = Vdc
    worksheet[f"D{counter+2}"] = Ripple
    worksheet[f"E{counter+2}"] = Factor
    workbook.save(filepath)

    counter += 1
    sleep(2)





