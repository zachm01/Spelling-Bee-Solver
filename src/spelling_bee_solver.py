"""Use to solve the New York Times Spelling Bee game"""

ALLOWED_LETTERS = 'bpnaeil'  # put the letters for the day in here
                             # first letter of the string is the yellow center
                             # letter of the hexagon on the NYT website/app
                             # in this case, that would be the letter 'o'

with open('data/common_words.txt', 'r', encoding='utf-8') as f:   # name of your words file
    lines = [i.replace('\n', '') for i in f.readlines()]

ALLOWED_LETTERS = list(ALLOWED_LETTERS)
good_words = []

for i, line in enumerate(lines):
    NUM_ALLOWED_LETTERS = 0
    for j, char in enumerate(line):
        if char in ALLOWED_LETTERS:
            NUM_ALLOWED_LETTERS += 1
    if NUM_ALLOWED_LETTERS == len(line) and len(line) >= 4 and ALLOWED_LETTERS[0] in line:
        good_words.append(line)

print(f'\nFound {len(good_words)} matches out of {len(lines)} words\n')

for i in enumerate(good_words):
    print(i)

