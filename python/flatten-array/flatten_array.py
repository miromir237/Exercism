def flatten(iterable):
    flat = []
    for item in iterable:
        if item is not None:
            if isinstance(item, list):
                flat.extend(flatten(item))
            else:
                flat.append(item)
    return flat
