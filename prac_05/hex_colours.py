NAME_TO_CODE = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUA": "#00ffff", "AQUAMARINE": "#7fffd4",
               "AZURE": "#f0ffff", "BEIGE": "#f5f5dc", "BISQUE": "#ffe4c4", "BLACK": "#000000",
               "BLANCHEDALMOND": "#ffebcd", "BLUE": "#0000ff"}

color_code = input("Enter color name: ").upper()

while color_code:
    try:
        color_name = NAME_TO_CODE[color_code]
        print(color_code, "is", NAME_TO_CODE[color_code])
    except KeyError:
        print("Invalid color name")

    color_code = input("Enter color name: ").upper()
