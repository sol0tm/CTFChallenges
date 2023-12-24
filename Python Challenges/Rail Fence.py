import hashlib

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Store the hashed password for user 'joe'
stored_username = "joe"
stored_password_hash = hash_password("password")  # Hash the password "password"

def login():
    # Get username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered credentials are correct
    if username == stored_username and hash_password(password) == stored_password_hash:
        print("Login successful!")
        print("Secret Phrase: slCF0100C1X1X1XXXXXX1C1SMSCALooT{XX1X000000000000_HITA_HL}")
    else:
        print("Login failed. Incorrect username or password.")
        print("Please try again.")

# Perform multiple login attempts
for _ in range(3):  # Allow 3 login attempts
    login()
    print("\n")  # Separate each login attempt with a newline

print("Maximum login attempts reached. Access denied.")
