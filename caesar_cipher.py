# Caesar Cipher - Encrypt or Decrypt with User Menu

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.isupper():
                result += chr((ord(char) - 65 + shift_amount) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift_amount) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("=== Caesar Cipher Tool ===")
print("1. Encrypt a Message")
print("2. Decrypt a Message")

choice = input("Choose an option (1/2): ")

if choice not in ["1", "2"]:
    print("Invalid choice! Please select 1 or 2.")
else:
    message = input("Enter your message: ")
    shift_val = int(input("Enter shift value: "))

    if choice == "1":
        encrypted = encrypt(message, shift_val)
        print("\nEncrypted Message:", encrypted)

    elif choice == "2":
        decrypted = decrypt(message, shift_val)
        print("\nDecrypted Message:", decrypted)
