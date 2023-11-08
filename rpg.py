import random
import string

def gen_password():
    try:
        password_length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
        return

    all_char = ''
    while True:
        print('Enter "uc" for uppercase\nEnter "lc" for lowercase\nEnter "dig" for digits\nEnter "spl" for special characters')
        choice = input("Enter your choice to generate (or press Enter to exit): ")
        
        if choice == 'uc':
            all_char += string.ascii_uppercase
        elif choice == 'lc':
            all_char += string.ascii_lowercase
        elif choice == 'dig':
            all_char += string.digits
        elif choice == 'spl':
            all_char += string.punctuation
        elif choice == '':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    
    if not all_char:
        print("No character types selected. Exiting.")
        return
    
    password = ''.join(random.choice(all_char) for _ in range(password_length))
    return password

if __name__ == "__main":
    password = gen_password()
    if password:
        print(f"Generated Random Password: {password}")
