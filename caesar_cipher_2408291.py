# Name - Rohit Ghimire
# Student id - 2408291

def welcome():
    print("Welcome to the Caesar Cipher"
          "This program encrypts and decrypts text with the Caesar Cipher.")


def enter_message():
    """
    Request input from the user to determine the mode of conversion
    and the message.Check if the mode is valid, and prompt the user
    until a valid mode is selected.Return a tuple containing the
    mode, the message(converted to uppercase), and the shift number.
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        print("Invalid Mode")
    message = input(f"What message would you like to"
                    f" {'encrypt' if mode == 'e' else 'decrypt'}: ").upper()
    return mode, message


def encrypt(message, shift_num):
    """
    Takes in message and shift_num as parameter
    Returns encrypted_message according to the shift_num\
    """
    # Declaring an empty string for encrypted message
    encrypted_message = ""
    # Using for loop to iterate through message
    for char in message:
        # Checking is the given message is either letter or number
        if char.isalnum():
            # ord() function to convert to ASCII encoding and adding the shift_num
            char = ord(char) + shift_num
            # Checking if ASCII of i is greater than 90
            if char > 90:
                # Concat the encrypted letters
                # to return the ascii code of z(90) -26 =76(a) starting from a
                encrypted_message += chr(char - 26)
            else:
                # Concat the encrypted letters
                encrypted_message += chr(char)
        else:
            # Concat the blank space
            encrypted_message += char

    return encrypted_message


def decrypt(message, shift_num):
    """
    Takes in message and shift_num as parameter
    Returns decrypted_message according to the shift_num
    """
    # Declaring an empty string for encrypted message
    decrypted_message = ""
    # Using for loop to iterate through message
    for char in message:
        # Checking is the given message is either letter or number using isalnum
        if char.isalnum():
            # ord() function to convert to ASCII encoding and adding the shift_num
            char = ord(char) - shift_num
            # Checking if ASCII of i is less than 65
            if char < 65:
                # chr() function to convert the ASCII encoding back to alphabets
                # Concat the decrypted letters
                decrypted_message += chr(char + 26)
            else:
                # Concat the decrypted letters
                decrypted_message += chr(char)
        else:
            # Concat the blank space
            decrypted_message += char

    # Returning the encrypted_message
    return decrypted_message


def is_file(filename):
    """It returns true if the given file exists"""
    try:
        with open(filename, 'r', encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False


def message_or_file():
    """It requests user where to run the code either in file or in console
    :returns the given mode,message and file
    """
    while True:
        while True:
            # done whether to use in console or file
            file_or_console = input("Would you like to read from (f) or the console (c)? ")
            if file_or_console in ("f", "c"):
                break
            print("Invalid")

        message = None
        filename = None
        if file_or_console == "c":
            task, message = enter_message()
            return task, message, filename
        if file_or_console == "f":
            while True:
                task = input("Would you like to encrypt (e) or decrypt (d) :")
                if task in ("e", "d"):
                    break
                print("Invalid mode")
                continue

            while True:
                filename = input("Enter a filename : ")
                if is_file(filename):
                    break
                print("Invalid Filename")

            return task, message, filename


def process_file(filename, task):
    """Return the encrypted or decrypted mode of file lines"""
    while True:
        # Exception handling if input shift has value error
        try:
            shift_num = int(input("What is the shift number : "))
            break
        except ValueError:
            print("Invalid Shift")
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if task == "e":
            encrypted = []
            for line in lines:
                encrypted.append(encrypt(line.upper(), shift_num))
            return encrypted
        if task == "d":
            decrypted = []

            for line in lines:
                decrypted.append(decrypt(line.upper(), shift_num))
            return decrypted


def write_messages(strings):
    """
    It helps to write the given lines into a file
    """
    with open("results.txt", "w", encoding="utf-8") as file:
        for i in strings:
            file.write(i)


def main():
    """
    Iy is the main function which is used for running the code where all the functions are called
    :return: mode message filename shift and other values
    """
    welcome()
    while True:
        mode, message, filename = message_or_file()
        if message is None:
            strings = process_file(filename, mode)
            write_messages(strings)
        elif filename is None:
            while True:
                try:
                    shift_num = int(input("What is the shift number: "))
                    break
                except ValueError:
                    print("Invalid Shift")
            if mode == "e":
                print(encrypt(message, shift_num))
            elif mode == "d":
                print(decrypt(message, shift_num))

        user_input = input("Would you like to encrypt or decrypt another message? (y/n) : ")
        if user_input == "y":
            continue
        print("Thanks for using the program, goodbye!")
        break


main()
