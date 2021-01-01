def ints_not_strings(lyst):
    filtered = [item for item in lyst if isinstance(item, int)]
    return filtered

print(ints_not_strings([99, 'no data', 95, 94, 'no data']))
