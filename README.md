# Spelling-Bee-Solver
A program that solves the NYT Spelling Bee game found at https://www.nytimes.com/puzzles/spelling-bee.

It automatically downloads today's letters and solves the game without using the list of correct answers found in the source of Spelling Bee's HTML. 

This is a highly unnecessary tool as one can already find the day's answers by inspecting the website's source code. The list of allowed letters (```validLetters```), pangrams (```pangrams```), answers (```answers```), and all those from the previous day's are located inside a div with ```id="js-hook-pz-moment__game"```. I made this as a programming exercise to develop my limited coding skills.

# Usage
Run the file. No user input is ordinarily necessary. However, if the HTTP request to download today's letters is to fail, the user is prompted to input the letters. By default, the program will automatically scrape the letters, but if you would like to always input them manually, change the variable on line 6 ```AUTOMATICALLY_GET_LETTERS``` from ```True``` to ```False```.

