# Previous NYT Spelling Bee letters https://www.sbsolver.com/archive

str_to_chars = lambda str: [char for char in str]

with open('data/words_alpha.txt', 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

allowed_letters = str_to_chars('oaflmru') # first letter of the string is the center letter of the hexagon
good_words = []
panagrams = []

for i in range(len(lines)):
    num_allowed_letters = 0
    for j in range(len(lines[i])):
        if lines[i][j] in allowed_letters:
            num_allowed_letters += 1
    
    if num_allowed_letters == len(lines[i]) and len(lines[i]) >= 4 and allowed_letters[0] in lines[i]:
        good_words.append(lines[i])

print(f'\nFound {len(good_words)} matches out of 370105 words\n')

for i in enumerate(good_words):
    print(f'{i[0] + 1}\t{i[1]}')