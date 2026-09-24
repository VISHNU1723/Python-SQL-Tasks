# Password Strength Checker
# Uses exception handling

def check_password(password):
    try:
        if len(password) < 8:
            raise ValueError("Password must contain at least 8 characters.")

        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter.")

        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter.")

        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit.")

        special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(char in special_characters for char in password):
            raise ValueError("Password must contain at least one special character.")

        print("Password is Strong.")

    except ValueError as error:
        print("Weak Password:", error)


def main():
    try:
        password = input("Enter your password: ")
        check_password(password)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

    except Exception as error:
        print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()
