def func(password):
    if isinstance(password, str):
        if len(password) < 8:
            return False
        else:
            return True
