def num_char(character, filepath):
    with open(filepath) as infile:
        content = infile.read()
        return content.count(character)
