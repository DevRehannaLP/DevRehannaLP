"""
Simple Log Parser
-----------------
Reads a log file and searches for keywords such as:
    - ERROR
    - WARNING
    - FAILED
    - CRITICAL

Usage:
    python log_parser.py
"""

def parse_log(file_path, keywords):
    """Read a log file and print lines containing any of the keywords."""
    try:
        with open(file_path, "r") as file:
            print(f"\n=== Parsing Log: {file_path} ===\n")
            for line in file:
                if any(keyword.lower() in line.lower() for keyword in keywords):
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("=== Simple Log Parser ===")
    file_path = input("Enter log file path: ")

    # Default keywords commonly used in security logs
    keywords = ["error", "warning", "failed", "critical"]

    print("\nSearching for:")
    for k in keywords:
        print(f" - {k}")

    parse_log(file_path, keywords)
    print("\nParsing complete.")


if __name__ == "__main__":
    main()