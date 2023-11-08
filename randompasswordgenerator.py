import random
import string

def gen_password():
    try:
        password_length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
        return

    all_char = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    
    if password_length < len(all_char):
        password = ''.join(random.choice(all_char) for _ in range(password_length))
        return password
    else:
        print("Password length is too long. It should be less than or equal to", len(all_char))
        return

if __name__ == "__main__":
    password = gen_password()
    if password:
        print(f"Generated Random Password: {password}")


