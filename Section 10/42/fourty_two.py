def process_strings(*args):
    lyst_strings = [elem for elem in args]
    lyst_upper = lyst_strings[:]
    for i in range(len(lyst_strings)):
        lyst_upper[i] = lyst_strings[i].upper()
    lyst_upper.sort()
    return lyst_upper

print(process_strings("snow", "glacier", "iceberg"))
