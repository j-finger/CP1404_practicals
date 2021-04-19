"""
CP1404 - Practical 5 - Jacob Finger
Hexadecimal colour code lookup
"""

HEX_CODES = {"VioletRed": "#d02090", "turquoise1": "#00f5ff", "ForestGreen": "#228b22", "DimGray": "#696969",
             "goldenrod2": "#eeb422", "LightCoral": "#f08080", "magenta": "#ff00ff", "red1": "#ff0000",
             "SeaGreen1": "#54ff9f", "sienna1": "#ff8247"}

hex_name = input("Enter the colour name: ")
while hex_name != "":
    if hex_name in HEX_CODES:
        print("The hex code of colour {} is {}".format(hex_name, HEX_CODES[hex_name]))
    else:
        print("Invalid colour name, please try again.")
    hex_name = input("Enter the colour name: ")
