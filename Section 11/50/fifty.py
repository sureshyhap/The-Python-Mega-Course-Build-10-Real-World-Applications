with open("data.txt", "a+") as d:
    d.seek(0)
    contents = d.read()
    d.write(contents + contents)
