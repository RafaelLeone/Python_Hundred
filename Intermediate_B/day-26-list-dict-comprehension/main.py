from random import randint
import pandas
import os


# List comprehension.
names = ["Angela", "Alex", "Nick", "Fred", "Daphne", "Scoob", "Shag", "Velma"]

short_names = [name for name in names if len(name) < 5]
big_names = [name.upper() for name in names if len(name) >= 5]

print(f"{short_names}\n{big_names}")

numbers = [1, 2, 3, 4, 5]

doubled_odd_numbers = [n*2 for n in numbers if n%2 == 0]
stringed_numbers = [str(n) for n in numbers if n%2 != 0]

print(f"{doubled_odd_numbers}\n{stringed_numbers}")

numbers_1 = [3, 18, 33, 18, 2, 2, 9, 10, 15, 101, 10]
numbers_2 = [3, 18, 100, 105, 10, 91, 90, 18, 3, 27]

new_list = [number for number in numbers_1 if number in numbers_2]

print(new_list)

# Dict comprehension.
students_scores_dict = {student: randint(0, 100) for student in names}

print(students_scores_dict)

approved_students_dict = {student: score for (student, score) in students_scores_dict.items() if score > 59}

print(approved_students_dict)

sentence = input()
result = {word: len(word) for word in sentence.split()}
print(result)

# With pandas.
# Get the absolute path to the directory containing the script.
file_name = "nato_phonetic_alphabet"
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f"{file_name}.csv")

data = pandas.read_csv(file_path)
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)
user_name = input("Enter name: ").upper()
nato_list = [nato_dict[letter] for letter in user_name]
print(nato_list)
