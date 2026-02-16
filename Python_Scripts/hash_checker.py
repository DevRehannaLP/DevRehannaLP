"""
Hash Checker
------------
Calculates and compares file hashes (MD5, SHA-1, SHA-256)
to verify file integrity or detect tampering.

Usage:
    python hash_checker.py
"""

import hashlib

def calculate_hash(file_path, hash_type="sha256"):
    """Calculate the hash of a file using the specified algorithm."""
    try:
        hash_func = hashlib.new(hash_type)

        with open(file_path, "rb") as file:
            # Read file in chunks to handle large files
            for chunk in iter(lambda: file.read(4096), b""):
                hash_func.update(chunk)

        return hash_func.hexdigest()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError:
        print(f"Error: Unsupported hash type '{hash_type}'.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    print("=== File Hash Checker ===")

    file_path = input("Enter file path: ")
    print("\nChoose hash type:")
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-256 (recommended)")

    choice = input("\nEnter choice (1/2/3): ")

    if choice == "1":
        hash_type = "md5"
    elif choice == "2":
        hash_type = "sha1"
    else:
        hash_type = "sha256"

    print(f"\nCalculating {hash_type.upper()} hash...\n")

    file_hash = calculate_hash(file_path, hash_type)

    if file_hash:
        print(f"{hash_type.upper()} Hash:")
        print(file_hash)

        compare = input("\nDo you want to compare it with another hash? (y/n): ").lower()
        if compare == "y":
            known_hash = input("Enter the known hash: ").strip()

            if known_hash.lower() == file_hash.lower():
                print("\n[✔] Hashes match — file integrity verified.")
            else:
                print("\n[✘] Hashes do NOT match — file may be altered.")
        else:
            print("\nHash calculation complete.")


if __name__ == "__main__":
    main()