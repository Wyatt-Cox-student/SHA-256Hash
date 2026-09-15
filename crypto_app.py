import hashlib


# Creates a SHA-256 hash from text entered by the user
def hash_text():
    text = input("Enter text to hash: ")

    hash_object = hashlib.sha256(text.encode())
    hash_value = hash_object.hexdigest()

    print("\nOriginal text:", text)
    print("SHA-256 Hash:", hash_value)


# Create a SHA-256 hash from a file
def hash_file():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, "rb") as file:
            file_data = file.read()

        hash_object = hashlib.sha256(file_data)
        hash_value = hash_object.hexdigest()

        print("\nFile:", file_name)
        print("SHA-256 Hash:", hash_value)

    except FileNotFoundError:
        print("File was not found.")


# Encrypts text using a Caesar cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""

    for character in text:
        if character.isalpha():

            if character.isupper():
                start = ord("A")
            else:
                start = ord("a")

            new_character = chr(
                (ord(character) - start + shift) % 26 + start
            )

            encrypted_text += new_character

        else:
            encrypted_text += character

    return encrypted_text


# Decrypts text using a Caesar cipher
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Caesar cipher menu
def cipher_menu():
    print("\n1. Encrypt Text")
    print("2. Decrypt Text")

    choice = input("Choose an option: ")

    text = input("Enter text: ")
    shift = int(input("Enter shift amount: "))

    if choice == "1":
        result = caesar_encrypt(text, shift)

        print("\nOriginal text:", text)
        print("Encrypted text:", result)
        print("Shift:", shift)

    elif choice == "2":
        result = caesar_decrypt(text, shift)

        print("\nEncrypted text:", text)
        print("Decrypted text:", result)
        print("Shift:", shift)

    else:
        print("Invalid option.")


# Main program menu
def main():
    while True:
        print("\n--- Cryptography Demo ---")
        print("1. SHA-256 Hash Text")
        print("2. SHA-256 Hash File")
        print("3. Caesar Cipher")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            hash_text()

        elif choice == "2":
            hash_file()

        elif choice == "3":
            cipher_menu()

        elif choice == "4":
            print("Program closed.")
            break

        else:
            print("Invalid option.")


main()