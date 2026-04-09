EET-321 Lab 5 – Rectifier Ripple Factor Measurement

Objective:
	To design and build a full-wave rectifier circuit using 1N4001 diodes and analyze its performance with a capacitor filter.
	To use Python scripting to automate measurements using Siglent test equipment (function generator, oscilloscope, and DMM).
	To measure and calculate the ripple factor for different capacitor values and input frequencies.
	To record and analyze the data in an Excel file.

Equipment Required:
	Siglent Function Generator (e.g., SDG1032X): To generate AC signals.
	Siglent Oscilloscope (e.g., SDS1202X-E): To measure the output waveform and ripple voltage.
	Siglent Digital Multimeter (e.g., SDM3055): To measure DC voltage and ripple voltage.
	Breadboard, 1N4001 diodes (4), capacitors (e.g., 100 µF and 470 µF), resistors, and connecting wires.
	Computer with Python installed: To run the automated test script.
	PyVISA and OpenPyXL libraries: For instrument control and Excel file handling.

<img width="726" height="531" alt="image" src="https://github.com/user-attachments/assets/f81dd860-fb8a-41a9-b75f-aa819c57b849" />

Circuit Design:
	Full-Wave Rectifier Circuit:
	Use 4 x 1N4001 diodes in a bridge rectifier configuration.
	Connect the output of the rectifier to a capacitor filter (start with 100 µF).
	Add a load resistor (e.g., 1 kΩ) across the capacitor.

	Test Setup:
	Connect the function generator to the input of the rectifier circuit.
	Connect the oscilloscope probes to the output of the rectifier to measure the waveform.
	Connect the DMM to measure the DC voltage and ripple voltage.

Lab Procedure:
Step 1: Build the Circuit
	Assemble the full-wave rectifier circuit on a breadboard.
	Ensure the capacitor and load resistor are properly connected.
Step 2: Configure the Test Equipment
	Set the function generator to generate a 5V amplitude sine wave at 50 Hz.
	Configure the oscilloscope to capture the output waveform.
	Use the DMM to measure the DC voltage and ripple voltage.
Step 3: Develop the Python Script
	Write a Python script to automate the following tasks:
	Control the function generator to set the frequency and amplitude.
	Capture the output waveform using the oscilloscope.
	Measure the DC voltage and ripple voltage using the DMM.
	Calculate the ripple factor using the formula:
	Vripple:
    √((V_rms^2-V_DC^2 ) )  

	Ripple Factor:
    V_ripple/V_DC
     
	Repeat the measurements for different frequencies (50 Hz, 60 Hz, 120 Hz, 1 kHz) and capacitors (100 µF and 470 µF) and load resistors (510 Ohm, 2kOhm).
	Save the data (frequency, capacitor value, DC voltage, ripple voltage, ripple factor) to an Excel file.
Step 4: Run the Automated Test
	Execute the Python script to perform the measurements.
	Verify the results by comparing them with manual measurements.
Step 5: Analyze the Data
	Open the Excel file and analyze the ripple factor for different frequencies, capacitor values, and resistor values.
	Plot graphs to visualize the relationship between ripple factor, frequency, and capacitance.
Discussion Questions:
	How does the ripple factor change with frequency and capacitance? Explain the underlying principles.
	What are the limitations of using a capacitor filter in a rectifier circuit?
	How could the circuit be modified to further reduce the ripple factor?

