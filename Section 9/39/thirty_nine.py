def sum_decimal_strings(lyst):
    numerical = [float(item) for item in lyst]
    return sum(numerical)

print(sum_decimal_strings(['1.2', '2.6', '3.3']))
