"""Case-study #6 Генерация предложений
Разработчики:
Шарков К., Кеда С., Ермоленко В.
"""
import random

cor_symb = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', '0', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '.', ',', '?', '!']


lines = []
with open('ansibig.txt') as dict_file:
    first_lst = dict_file.read()
lines = first_lst.split()
new = []
for word in lines:
    for symbol in word:
        if symbol.lower() not in cor_symb:                # getting a list of consecutive words
            word = word[:word.find(str(symbol))] + word[1 + word.find(str(symbol)):]
    new.append(word)
while True:
    try:
        new.remove('')
    except ValueError:
        break
print(len(new), new)


start_words = []
for word in new:
    if word.istitle():
        start_words.append(word)      # list of capitalized words
print(len(start_words),start_words)

spsp=[]
for word in range(len(new)-1):
    chet = 0
    for i in range(len(spsp)):
        if new[word] == spsp[i][0]:
            if new[word+1] not in spsp[i]:
                spsp[i].append(new[word+1])  # spsp - list of lists, the zero word of each sublist is the key
            chet = 1
    if chet == 0 and not(new[word].endswith('.') or new[word].endswith('!') or new[word].endswith('?')):
        spsp.append([new[word],new[word+1]])
print(len(spsp), spsp)

# TODO:(Vova): def that generates a random sentence. Output a certain number of sentences. The first word of each sentence is taken from start_words.

# TODO:(Sveta): PEP-8, adaptation for english text.


