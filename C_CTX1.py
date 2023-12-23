def admin_login(username, password):
    if password == "login" and username == "admin":
        print("Login successful!")
        print("Secret Key: NGHDLJBMNFHALKBPPJFMKNAIOLEOJADFMHGCPEFBLIBNPLFOLEBBPJFMLMBJODEGLABFIBCEMIGNJKDPMFGAPFFAMFGAPCFHIPCK")  # Replace with your actual secret key
    else:
        print("Warning: Invalid username or password.")

# Example usage:
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

admin_login(username_input, password_input)



