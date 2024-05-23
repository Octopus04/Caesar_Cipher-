# Import the art library
from art import *

# Define the name you want to design
name = "Birju"

# Generate ASCII art for the name
ascii_art = text2art(name)

# Print the ASCII art
print(ascii_art)

print("\n---------------------------------------*Encryption & Decryption using Caesar_Cipher Algorithm*---------------------------------------")

#Function for encrypt the text!
def encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + shift) % 26) + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

##Function for decrypt the text!
def decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - 65 - shift) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 - shift) % 26) + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

#Function for select the choice for what you want to do encrypt or decrypt the text!
def main():
    while True:
        print("\n-------------------------------------------------------- By Birju Kansara -----------------------------------------------------------")
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Quit\n")
        
        #choice 1 can select the function of encrypt the code and encrypt the text
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)

        #choice 2 can select the function of decrypt the code and decrypt the text
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        
        #choice 3 is for exit from the code 
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# this code checks if the script is being run directly, and if so, it calls the main() function.
if __name__ == "__main__":
    main()
