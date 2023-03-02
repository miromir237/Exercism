def label(colors):
    colours = [
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
    unit_value = 10 ** colours.index(colors[2])
    value = (colours.index(colors[0]) * 10 + colours.index(colors[1])) * unit_value

    if value >= 1000000000:  
        return f"{value//1000000000:.0f} gigaohms"
    elif value >= 1000000:
        return f"{value//1000000:.0f} megaohms"
    elif value >= 1000:
        return f"{value//1000:.0f} kiloohms"
    elif value >= 1:
        return f"{value:.0f} ohms"
    else:
        return f"{value:.0f} ohms"
