def tell_temp(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature <= 25 and temperature >= 15:
        return "Warm"
    else:
        return "Cold"
