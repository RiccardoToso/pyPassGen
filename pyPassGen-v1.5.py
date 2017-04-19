import random
import argparse


def main():
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ['!', '£', '$', '%', '&' '(', ')', '=', '?', '^', '+', '*', '[', ']', '{', '}',
               'ç', '@', '#', '§', '-', '_', '.', ':', ',', ';', '<', '>']
    password = []

    parser = argparse.ArgumentParser()
    parser.add_argument('--length', type=int, default=15,
                        help='Specify the desired length of the password')
    parser.add_argument('--num', type=int, default=3,
                        help='Specify how many numbers must have the password')
    parser.add_argument('--sym', type=int, default=2,
                        help='Specify how many symbols must have the password')
    args = parser.parse_args()

    remaining_chars = args.length - args.num - args.sym
    ul = random.randint(0, remaining_chars)
    ll = remaining_chars - ul
    done = False

    while not done:
        if ll > 0:
            for a in range(0, ll):
                password.append(
                    lowercase_letters[random.randint(0, len(lowercase_letters) - 1)])

        if ul > 0:
            for b in range(0, ul):
                password.append(
                    uppercase_letters[random.randint(0, len(uppercase_letters) - 1)])
        if args.num > 0:
            for c in range(0, args.num):
                password.append(numbers[random.randint(0, len(numbers) - 1)])

        if args.sym > 0:
            for d in range(0, args.sym):
                password.append(symbols[random.randint(0, len(symbols) - 1)])

        random.shuffle(password)
        sh_pass = "".join(str(p) for p in password)
        print("\n")
        print(sh_pass)
        print("\n")
        exit = input("Are you satisfied? ('y' o 'n')  ")
        if exit == "y":
            done = True
            print("Good Bye!")
        else:
            password = []


if __name__ == '__main__':
    main()
