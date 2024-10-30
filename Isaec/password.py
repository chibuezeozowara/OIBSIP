import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# easy method
print("Welcome to my password generation")
ps_letters = int(input("How many letters would you like in your password?\n"))
ps_symbols = int(input(f"How many symbols would you like?\n"))
ps_numbers = int(input(f"How many numbers would you like?\n"))
password = []

for letter in range(1, ps_letters + 1):
    password.append(random.choice(letters))

for symbol in range(1, ps_symbols + 1):
    password.append(random.choice(symbols))

for number in range(1, ps_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)

new_password = ""
for char in password:
    new_password += char
print(new_password)
