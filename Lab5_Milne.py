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
libraries = ["pyvisa", "asyncio", "clickplc", "numpy", "pandas", "openpyxl"]

# Following code loops the install function to download all requested libraries.
for i in range(len(libraries)):
    install(libraries[i])

# Imports of Import
from detect_Instruments import detect_instruments
from time import sleep
import openpyxl
import pandas as pd
import pyvisa


# Set up the instruments
[supply, fungen, dmm, oscope] = detect_instruments()

# Variables
frequency = 50

# Set up the function generator to produce the required 5 volt sine wave at a given f.
fungen.write(f"C1:BaSeWaVe WaVeTyPe,SINe,FRQ,{frequency}")
sleep(1)
fungen.write("C1:OUTPut ON")
sleep(1)

# Set up the oscilloscope to take a measurement.
oscope.write("PACU RMS,C1")
sleep(2)
oscope.query(f"C1:PAVA? RMS")