import pandas

#TODO 1. Create a dictionary in this format:

# {"A": "Alfa", "B": "Bravo"}
file = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in file.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Which word do you want to write in Nato Language: ").upper()
nato = []
for letter in word:
    nato += ([value for (key, value) in (dictionary.items()) if key == letter])
print(nato)

