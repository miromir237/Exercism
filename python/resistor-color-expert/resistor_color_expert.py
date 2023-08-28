def resistor_value(value):
    if value >= 1000000000:  
        return f"{value/1000000000:.3g} gigaohms"
    elif value >= 1000000:
        return f"{value/1000000:.3g} megaohms"
    elif value >= 1000:
        return f"{value/1000:.3g} kiloohms"
    elif value >= 1:
        return f"{value:.0f} ohms"
    else:
        return f"{value:.0f} ohms"    
    
def resistor_label(colors):
    colour_band = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
            ] 
    tolerance_band = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }

    if len(colors) == 5:
        value = (colour_band.index(colors[0]) * 100 + colour_band.index(colors[1]) * 10 + colour_band.index(colors[2])) * 10 ** colour_band.index(colors[3])
        tolerance = tolerance_band[colors[4]]
        return f"{resistor_value(value)} ±{tolerance}%"
    if len(colors) == 4:
        value = (colour_band.index(colors[0]) * 10 + colour_band.index(colors[1])) * 10 ** colour_band.index(colors[2])
        tolerance = tolerance_band[colors[3]]
        return f"{resistor_value(value)} ±{tolerance}%"
    elif len(colors) == 3:
        unit_value = 10 ** colour_band.index(colors[2])
        value = (colour_band.index(colors[0]) * 10 + colour_band.index(colors[1])) * unit_value
        return f"{resistor_value(value)} ohms ±{tolerance}%"
    elif len(colors) == 1:
        value = colour_band.index(colors[0])
        return f"{resistor_value(value)}"
    else:
        return "Invalid number of bands"
    