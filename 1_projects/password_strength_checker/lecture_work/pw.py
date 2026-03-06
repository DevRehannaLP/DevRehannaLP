def greet(name):
    return f"Hello {name}, youre cyberdev enviornment is running smoothly."

def farewell(name):
    return f"Goodbye {name}, see you next session!"

def check_password_strength():
    print("Password checker coming soon!")

print("Choose an option")
print("1. Greet me")
print("2. Say goodbye")
print("3. Check password strength")
print("4. Exit")
choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    user_name = input("Enter your name: ")
    print(greet(user_name))
elif choice == "2":
    user_name = input("Adios!: ")
    print(farewell(user_name))
elif choice == "3":
    check_password_strength()
elif choice == "4":
    user_name = input("Exit: ")
    print("Exiting program...Goodbye!")

