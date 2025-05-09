import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a random password with specified complexity"""
    characters = string.ascii_lowercase  # Always include lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Ensure password meets complexity requirements
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def get_valid_input(prompt, input_type=int, min_value=1, max_value=50):
    """Get and validate user input"""
    while True:
        try:
            value = input_type(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    print("=== Password Generator ===")
    
    # Get password length
    length = get_valid_input(
        "Enter password length (8-50 recommended): ",
        min_value=4,
        max_value=100
    )
    
    # Get complexity options
    print("\nPassword complexity options:")
    use_uppercase = input("Include uppercase letters? (Y/n): ").lower() != 'n'
    use_digits = input("Include digits? (Y/n): ").lower() != 'n'
    use_special = input("Include special characters? (Y/n): ").lower() != 'n'
    
    # Generate password
    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_digits=use_digits,
        use_special=use_special
    )
    
    # Display results
    print("\nGenerated Password:")
    print("-" * 30)
    print(password)
    print("-" * 30)
    print(f"Length: {len(password)} characters")
    print(f"Complexity: {'Strong' if (use_uppercase and use_digits and use_special) else 'Medium' if (use_uppercase or use_digits or use_special) else 'Weak'}")

if __name__ == "__main__":
    main()