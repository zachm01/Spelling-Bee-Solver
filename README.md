# Spelling-Bee-Solver
A program that solves the NYT Spelling Bee game found at https://www.nytimes.com/puzzles/spelling-bee.

It automatically downloads today's letters and solves the game without using the list of correct answers found in the source of Spelling Bee's HTML. 

# Usage
Run the file. No user input is ordinarily necessary. However, if the HTTP request to download today's letters is to fail, the user is prompted to input the letters. By default, the program will automatically scrape the letters, but if you would like to always input them manually, change the variable on line 6 ```AUTOMATICALLY_GET_LETTERS``` from ```True``` to ```False```.

