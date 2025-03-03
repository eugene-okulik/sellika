text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

words = text.split()
new_text = []

for word in words:
    if word.isalpha():
       word += 'ing'
    else:
        last_symbol = word[-1]
        first_part_of_word = word[:-1]
        word = first_part_of_word + 'ing' + last_symbol

    new_text.append(word)


result = " ".join(new_text)
print(result)
