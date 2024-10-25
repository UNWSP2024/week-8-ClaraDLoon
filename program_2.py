#Program #2: Word Separator
#Clara Riley
#Luke Snell
#10/24/24

def word_separator(sentence):
    new_sentence = sentence[0]  # Start with the first character

    for char in sentence[1:]:
        if char.isupper():
            new_sentence += ' ' + char.lower()
        else:
            new_sentence += char

    return new_sentence.strip().capitalize() + '.'

sentence = input('Please enter your sentence.')
new_sentence = word_separator(sentence)
print(new_sentence)
