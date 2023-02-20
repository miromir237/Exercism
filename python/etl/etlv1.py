def transform(legacy_data):
    data = {}
    for key, value in legacy_data.items():
        for letter in value:
            data[letter.lower()] = key
    return data

def transform(old):
    return { value.lower(): key for key,values in old.items() for value in values }