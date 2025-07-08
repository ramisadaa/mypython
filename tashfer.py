import os
import random
import string

def encrypt(text, chars, key):
    cipher_text = ""
    for letter in text:
        if letter in key:
            index = key.index(letter)
            cipher_text += chars[index]
        else:
            cipher_text += letter  # الاحتفاظ بالمسافات والأحرف غير المعروفة
    return cipher_text

def decrypt(cipher_text, chars, key):
    plain_text = ""
    for letter in cipher_text:
        if letter in chars:
            index = chars.index(letter)
            plain_text += key[index]
        else:
            plain_text += letter
    return plain_text

def main():
    os.system('cls')
    print("Welcome to the Tashfer program!") 
    
    # إنشاء القوائم الأساسية
    char = string.ascii_letters + string.digits + string.punctuation + ' '
    key = list(char)
    chars = key.copy()
    random.shuffle(chars)
    
    while True:
        os.system('cls')
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            plain_text = input("\nEnter a message to encrypt: ")
            cipher_text = encrypt(plain_text, chars, key)
            print("Encrypted message:", cipher_text)
            input("Press Enter to continue...")

        elif choice == '2':
            cipher_text = input("\nEnter a message to decrypt: ")
            plain_text = decrypt(cipher_text, chars, key)
            print("Decrypted message:", plain_text)
            input("Press Enter to continue...")

        elif choice == '3':
            print("\nThank you for using Tashfer!")
            input("Press Enter to exit...")
            os.system('cls')
            break
            
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()