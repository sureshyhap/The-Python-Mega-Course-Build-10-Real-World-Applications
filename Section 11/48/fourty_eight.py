with open("bear.txt", "r") as infile:
    contents = infile.read()
    with open("first.txt", "w") as outfile:
        outfile.write(contents[:90])
