def main():
    print("Welcome to the login system")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if check_credentials(username, password):
        print("Login successful!")
    else:
        print("Login failed. Invalid username or password.")

def check_credentials(username, password):
    valid_username = "haha"
    valid_password = "haha"

    return username == valid_username and password == valid_password

if __name__ == "__main__":
    main()
