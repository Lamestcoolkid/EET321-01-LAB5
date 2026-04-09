# Written by John Milne, with help from Austin Knorr.
# This script detects the measurement instruments that are connected
# to this PC and that use the PYVISA communications protocol to
# communicate.

# Assumptions:
# 1) The libraries numpy and pyvisa have been installed and are
#    available libraries to the python installation.
# 2) The instruments to be detected have been powered on.

# Imports of import
import numpy as np

# Function definition for the function detect instruments.
# To call this function from another script, use the import command:
#     from detect_Instruments import detect_instruments.
# Then call the function detect_instruments()
def detect_instruments():

    # Imports of import.
    import pyvisa

    # Create the Resource Manager Object and grab the addresses
    # of the connected instruments using the list_resources()
    # function in the ResourceManager() object, then print out
    # those addresses as well as return them to the function
    # call.
    rm = pyvisa.ResourceManager()
    addresses = rm.list_resources()

    # Use the addresses list determined above to open the currently
    # available instruments for use, setting timeouts as needed.
    for j in range(len(addresses)):
        if len(addresses[j]) >= 25:
            match addresses[j][22:25]:
                case 'SPD':
                    supply = rm.open_resource(addresses[j])
                case 'SDM':
                    dmm = rm.open_resource(addresses[j], open_timeout=10000)
                case 'SDG':
                    fungen = rm.open_resource(addresses[j])
                case 'SDS':
                    oscope = rm.open_resource(addresses[j], open_timeout=10000)
                case _:
                    print("No matching instrument")

    # As an error check, but especially for the common case of one of the
    # instruments not being turned on, use the TRY:EXCEPT structure against
    # the truthiness of its name existing to determine if the variable got
    # set, and if not, set it to NaN.
    try:
        supply
    except NameError as e:
        supply = np.nan
    try:
        dmm
    except NameError as e:
        dmm = np.nan
    try:
        fungen
    except NameError as e:
        fungen = np.nan
    try:
        oscope
    except NameError as e:
        oscope = np.nan

    return [supply,fungen,dmm,oscope]