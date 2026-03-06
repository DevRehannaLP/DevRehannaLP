# ⭐ Add user input
# This makes the program interact with you, which is a huge step forward
# — almost every real script, automation, or cybersecurity tool uses input in some form.
# Here’s the tiny upgrade:

# Open main.py and replace the contents with:
def greet(name):
    return f"Hello {name}, your cyberdev environment is running smoothly."

# ask the user for their name
user_name = input("Enter your name: ")

# call the function using the user's input
message = greet(user_name)
print(message)

