# ∞ ☬ DevRehannaLP ☬ | DevSecOps ∞ 20261603 1739
def greet(name):
    return f"Hello {name}, youre cyberdev enviornment is running smoothly."
def farewell(name):
    return f"Goodbye {name}, see you next session!"

print("Choose an option")
print("1. Greet me")
print("2. Say goodbye")
print("3 Exit")

choice = input("Enter choice (1/2/3): ")


if choice == "1":
    user_name = input("Enter your name: ")
    print(greet(user_name))

elif choice == "2":
    user_name = input("Adios!: ")
    print(farewell(user_name))

elif choice == "3":
    user_name = input("Exit: ")
    print(exit(user_name))

