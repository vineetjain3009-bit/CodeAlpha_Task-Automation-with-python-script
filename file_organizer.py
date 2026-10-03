"""Move JPG images from one folder to another.

This beginner-friendly script asks for two folder paths and moves every JPG
file found directly inside the source folder. Existing files are never
overwritten: a number is added to a duplicate filename when needed.
"""

import os
import shutil


def get_available_path(destination_folder, filename):
    """Return a destination path that will not overwrite an existing file."""
    name, extension = os.path.splitext(filename)
    destination_path = os.path.join(destination_folder, filename)
    number = 1

    # Add " (1)", " (2)", and so on until the name is available.
    while os.path.exists(destination_path):
        new_filename = f"{name} ({number}){extension}"
        destination_path = os.path.join(destination_folder, new_filename)
        number += 1

    return destination_path


def move_jpg_files(source_folder, destination_folder):
    """Move JPG files and return the number of files moved successfully."""
    moved_files = 0

    try:
        # os.listdir finds files directly inside the source folder.
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)

            # Check for files only, and accept both .jpg and .JPG extensions.
            if os.path.isfile(source_path) and filename.lower().endswith(".jpg"):
                destination_path = get_available_path(destination_folder, filename)

                try:
                    shutil.move(source_path, destination_path)
                    moved_files += 1
                    print(f"Moved: {filename}")
                except OSError as error:
                    # One problem file should not stop the rest of the files.
                    print(f"Could not move '{filename}': {error}")
    except OSError as error:
        print(f"Could not read the source folder: {error}")

    return moved_files


def main():
    """Ask for folder paths, prepare the destination, and move JPG files."""
    print("JPG File Organizer")

    # strip removes accidental spaces; expanduser supports paths beginning with ~.
    source_input = input("Source folder path: ").strip()
    destination_input = input("Destination folder path: ").strip()

    if not source_input or not destination_input:
        print("Please enter both a source folder and a destination folder.")
        return

    source_folder = os.path.abspath(os.path.expanduser(source_input))
    destination_folder = os.path.abspath(os.path.expanduser(destination_input))

    if not os.path.isdir(source_folder):
        print("The source folder does not exist or is not a valid folder.")
        return

    if os.path.exists(destination_folder) and not os.path.isdir(destination_folder):
        print("The destination path exists but is not a folder.")
        return

    try:
        # This creates the destination folder and any missing parent folders.
        os.makedirs(destination_folder, exist_ok=True)
    except OSError as error:
        print(f"Could not create the destination folder: {error}")
        return

    if os.path.normcase(source_folder) == os.path.normcase(destination_folder):
        print("The source and destination folders must be different.")
        return

    moved_files = move_jpg_files(source_folder, destination_folder)
    print(f"\nFiles moved: {moved_files}")


if __name__ == "__main__":
    main()
