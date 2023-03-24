def proverb(*input_data, qualifier=None):
    if not input_data:
        return []
    if qualifier:
        return [f"For want of a {input_data[i]} the {input_data[i+1]} was lost." for i in range(len(input_data)-1)] + [f"And all for the want of a {qualifier} {input_data[0]}."]
    else:
        return [f"For want of a {input_data[i]} the {input_data[i+1]} was lost." for i in range(len(input_data)-1)] + [f"And all for the want of a {input_data[0]}."]
