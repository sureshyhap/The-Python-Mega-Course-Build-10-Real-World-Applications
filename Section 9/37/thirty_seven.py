def greater_than_zero(lyst):
    filtered = [item for item in lyst if item > 0]
    return filtered

print(greater_than_zero([-5, 3, -1, 101]))
