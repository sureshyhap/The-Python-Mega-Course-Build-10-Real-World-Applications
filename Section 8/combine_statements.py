text = None
final_text = []

while text != "\end":
    text = input("Say something: ")
    final_text.append(text)

question_words = ["How", "Who", "What", "When", "Where", "Why", "Which"]
final_final_text = []
for string in final_text:
    part = string.capitalize()
    words = part.split()
    question_mark = False
    if words[0] in question_words:
        question_mark = True
    if question_mark:
        part = part + '?'
    else:
        part = part + '.'
    final_final_text.append(part)

final_final_text.pop()
output = " ".join(final_final_text)
print(output)
