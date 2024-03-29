"""Solve the New York Times' Spelling Bee game without using their word list"""

import requests
from bs4 import BeautifulSoup

AUTOMATICALLY_GET_LETTERS = True # set to "True" if you would like the letters
                                 # to be downloaded automatically
good_words = []

# download list of words
try:
    # 466,000 words (split with '\n')
    response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")
    if response.status_code == 200:
        lines = response.text.split('\n')
except Exception as exc:
    raise ConnectionError("Could not get HTTP request for words") from exc

try:
    # 58,000 "common" words (split with '\r\n')
    # Used to identify the most commonly occuring in English solutions
    response = requests.get("http://www.mieliestronk.com/corncob_lowercase.txt")
    if response.status_code == 200:
        common_words = response.text.split('\r\n')
except Exception as exc:
    raise ConnectionError("Could not get HTTP request for common words") from exc

# download the allowed letters
if AUTOMATICALLY_GET_LETTERS:
    try:
        page = requests.get("https://www.nytimes.com/puzzles/spelling-bee")
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            TXT = str(soup.find(id="js-hook-pz-moment__game"))
            LETTERS = TXT[TXT.index('validLetters\":'):TXT.index('pangrams')]
            ALLOWED_LETTERS = LETTERS[LETTERS.index('[')+1:LETTERS.index(']')]
            ALLOWED_LETTERS = ''.join([i for i in list(ALLOWED_LETTERS) if i.isalnum()])
    except Exception as exc:
        raise ConnectionError("Could not get HTTP request for letters") from exc
else:
    ALLOWED_LETTERS = input("Today's letters (center letter comes first): ")

def is_pangram(word: str) -> bool:
    """Check if a word is a pangram"""
    return len(set(word)) == 7

if __name__ == "__main__":
    for i, line in enumerate(lines):
        NUM_ALLOWED_LETTERS = 0
        for j, char in enumerate(line):
            if char in ALLOWED_LETTERS:
                NUM_ALLOWED_LETTERS += 1
        if NUM_ALLOWED_LETTERS == len(line) and len(line) >= 4 and ALLOWED_LETTERS[0] in line:
            good_words.append(line)

    common_solutions = []

    print(f"\nFound {len(good_words)} total solutions from {len(lines)} words ", end='')
    print(f"using letters {list(ALLOWED_LETTERS)}.\n")

    print("All solutions:\n")

    for i, word in enumerate(good_words):
        out = ""
        if word in common_words:
            out = "\033[3m"
            common_solutions.append(word)
        elif is_pangram(word):
            out = "\033[3m\033[1m"
        print(out + f"{i}\t{word}\033[0m")

    print(f"\nFound {len(common_solutions)} common solutions:\n")

    for i, word in enumerate(common_solutions):
        out = ""
        if is_pangram(word):
            out += "\033[3m\033[1m"
        print(out + f"{i}\t{word}\033[0m")
