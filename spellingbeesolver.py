'''Solve the NYT Spelling Bee'''

allowed_letters = 'oaflmru'  # put the letters for the day in here
                             # first letter of the string is the yellow center letter of the hexagon on the NYT website/app
                             # in this case, that would be the letter 'o'

str_to_chars = lambda str: [char for char in str] # for ease of entering allowed letters

with open('words_alpha.txt', 'r') as f:   # name of your words file
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

allowed_letters = str_to_chars(allowed_letters)
good_words = []

for i in range(len(lines)):
    num_allowed_letters = 0
    for j in range(len(lines[i])):
        if lines[i][j] in allowed_letters:
            num_allowed_letters += 1
    
    if num_allowed_letters == len(lines[i]) and len(lines[i]) >= 4 and allowed_letters[0] in lines[i]:
        good_words.append(lines[i])

print(f'\nFound {len(good_words)} matches out of {len(lines)} words\n')

for i in enumerate(good_words):
    print(f'{i[0]+1}\t{i[1]}')
