# PRODIGY_CS_01 - Caesar Cipher Implementation
# Author: Hamdi Ali Abdullahi

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt only letters
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char  # Keep non-letters unchanged
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("===== PRODIGY_CS_01: Caesar Cipher Program =====")
    text = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    encrypted_text = encrypt(text, shift)
    print("\nEncrypted Text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, shift)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
