import json, difflib

data = {}

def load():
    with open("data.json", "r") as infile:
        global data
        data = json.load(infile)

def meaning():
    word = None
    while word not in data.keys():
        word = input("Enter a word: ")
        if word not in data.keys():
            word = word.lower()
        if word in data.keys():
            break
        possible_word = difflib.get_close_matches(word, data.keys(), 1, .8)
        if len(possible_word) == 0:
            print("Incorrect input")
            continue
        possible_word = possible_word[0]
        print("Did you mean " + possible_word + "?")        
    for definition in data[word]:
        print(definition)
    
load()
meaning()
