from random import choice

symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input("What password length do you want to have? \n"))

for j in range(1, 6):
    password = ""
    for i in range(pass_len):
        password += choice(symbol)
    print(f"Your {j}-st password is '{password}'")