# ∞ ☬ DevRehannaLP ☬ | DevSecOps ∞ 20261603 1739
import os
import shutil

# File categories and their extentions
FILE_TYPES = {
    "python":   [".py"],
    "docs":      [".md", ".txt", ".pdf", ".docx"],
    "images":   [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "audio":    [".mp3", ".wav", ".flac"],
    "video":    [".mp4", ".mov", ".avi"],
    "archives": [".zip", ".tar", ".gz", ".tar.gz"],
    "scripts":  [".sh", ".bash"],
    "data":     [".csv", ".json", ".xml", ".yaml"],
}
# The main orgainzed function
def organize_folder(folder_path):
    folder_path = os.path.expanduser(folder_path)
    print(f"\n=== File Organizer ===")
    print(f"Scanning: {folder_path}\n")

    if not os.path.exists(folder_path):
        print("Error: Folder does not exist!")
        return

    moved = 0
    skipped = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            skipped += 1
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find which catergory it belongs to
        category = None
        for folder_name, extensions in FILE_TYPES.items():
            if ext in extensions:
                category = folder_name
                break

        if category is None:
            category = "misc"

        # Create category folder if it doesn't exist
        dest_folder = os.path.join(folder_path, category)
        os.makedirs(dest_folder, exist_ok=True)

        # Move the file
        dest_path = os.path.join(dest_folder, filename)
        shutil.move(file_path, dest_path)
        print(f"    Moved: {filename} → {category}/")
        moved += 1
    print(f"\nDone! {moved} file(s) moved, {skipped} folder(s) skipped.")

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ")
    organize_folder(folder)

