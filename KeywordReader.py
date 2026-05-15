from datetime import date

user_name = input("Please enter your name ? : ")
user_age = int(input("Please enter your age ? : "))

print("\n")

current_year = date.today().year
print(f"The year the user was born is: {current_year-user_age}")

print("\n")

try:
    with open("notes.txt",'r') as first_file:
        print(first_file.read())
except FileNotFoundError:
    print("The notes.txt file doesn't exist")

print("\n")

keyword = "python"
try:
    with open("notes.txt", "r") as f:
        for line in f:
            if keyword.lower() in line.lower():
                print(line, end="")
except FileNotFoundError:
    print("The notes.txt file doesn't exist")

print("\n")

def listavg(lst):
    if len(lst) == 0:
        return 0
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

raw = input("Enter numbers separated by spaces: ")
numbers = [float(n) for n in raw.split()]
avg = listavg(numbers)
print(avg)

print("\n")






