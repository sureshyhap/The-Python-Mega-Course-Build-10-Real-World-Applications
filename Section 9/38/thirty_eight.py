def zero_out_strings(lyst):
    filtered = [item if (not isinstance(item, str)) else 0 for item in lyst]
    return filtered

print(zero_out_strings([99, 'no data', 95, 94, 'no data']))
