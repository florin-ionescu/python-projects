import random
#The string module gives you ready-made groups of characters.
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # this contains: abcdefghijklmnopqrstuvwxyz
    characters = string.ascii_lowercase

    if use_uppercase:
        # If True contains: ABCDEFGHIJKLMNOPQRSTUVWXYZ + characters (lowercase)
        characters += string.ascii_uppercase
    if use_numbers:
        # if true:  0123456789 + characters
        characters += string.digits
    if use_symbols:
        # if true: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
        characters += string.punctuation

    # This creates an empty string called password.
    password = ""

    # The underscore _ is used because we do not need the loop number.
    for _ in range(length):
        password += random.choice(characters)

    return password

def ask_yes_no(question):
    answer = input(question).strip().lower()
    if answer == "yes" or answer == "y":
        return True
    else:
        return False

def main():
    print("Password Generator")

    while True:
        length = int(input("Enter the length of the password: "))

        use_uppercase = ask_yes_no("Do you want to use uppercase letters? yes/no: ")
        use_numbers = ask_yes_no("Do you want to use numbers? yes/no: ")
        use_symbols = ask_yes_no("Do you want to use symbols? yes/no: ")

        password = generate_password(
            length,
            use_uppercase,
            use_numbers,
            use_symbols
        )
        print(f"\nGenerated password: {password}")

        again = ask_yes_no("Would you like to generate another password? yes/no: ")
        if not again:
            print("Thank you for using password generator!")
            break

if __name__ == "__main__":
    main()