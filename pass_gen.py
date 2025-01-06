
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy:
import random
ltr_part = random.choices(letters,weights = None, k = nr_letters)
number_part = random.choices(numbers,weights=None,k=nr_numbers)
symbol_part = random.choices(symbols,weights=None,k=nr_symbols)
new_password = ltr_part + symbol_part + number_part
#print("Your new password:")
#for i in new_password:
#   print(i,end='')

#hard:

random.shuffle(new_password)
print("Your new password is: ")
for i in new_password:
    print(i,end='')