
all_digits = ['-', '_', '.', ',', ':', ';', '!', '?', '~', '`']
string = input("add text")
total_digits = 0
for s in string:
    if s in all_digits:
        total_digits += 1
print("Total digits found -", total_digits)