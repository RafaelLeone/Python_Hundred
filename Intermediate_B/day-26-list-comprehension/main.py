names = ["Angela", "Alex", "Nick", "Fred", "Daphne", "Scoob", "Shag", "Velma"]

short_names = [name for name in names if len(name) < 5]
big_names = [name.upper() for name in names if len(name) >= 5]

print(f"{short_names}\n{big_names}")

numbers = [1, 2, 3, 4, 5]

doubled_odd_numbers = [n*2 for n in numbers if n%2 == 0]
stringed_numbers = [str(n) for n in numbers if n%2 != 0]

print(f"{doubled_odd_numbers}\n{stringed_numbers}")
