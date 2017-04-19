import random

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['!', '£', '$', '%', '&' '(', ')', '=', '?', '^', '+', '*', '[', ']', '{', '}',
           'ç', '@', '#', '§', '-', '_', '.', ':', ',', ';', '<', '>']
password = []

lunghezza = int(input("Quanti caratteri deve avere la password desiderata?\n"))
num = int(input("Quanti numeri deve contenere?\n"))
sym = int(input("Quanti simboli?\n"))
residuo = lunghezza - num - sym
ul = random.randint(0, residuo)
ll = residuo - ul
soddisfatto = False

while not soddisfatto:
    if ll > 0:
        for a in range(0, ll):
            password.append(
                lowercase_letters[random.randint(0, len(lowercase_letters) - 1)])

    if ul > 0:
        for b in range(0, ul):
            password.append(
                uppercase_letters[random.randint(0, len(uppercase_letters) - 1)])
    if num > 0:
        for c in range(0, num):
            password.append(numbers[random.randint(0, len(numbers) - 1)])

    if sym > 0:
        for d in range(0, sym):
            password.append(symbols[random.randint(0, len(symbols) - 1)])

    random.shuffle(password)
    sh_pass = "".join(str(p) for p in password)
    print(sh_pass)
    exit = input("Soddisfatto? ('s' o 'n')\n")
    if exit == "s":
        soddisfatto = True
    else:
        password = []
