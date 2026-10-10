"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort items of type {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Error: exactly two arguments are required. Usage: python3 main.py <filename> <yes|no>")
        print("Provide the word-list file path first; use 'yes' to remove duplicates or 'no' to keep them (only 'yes', case-insensitive, removes duplicates).")
        sys.exit(1)

    print(f"Attempting to read words from file '{filename}'.")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File '{filename}' was not found. Using the built-in sample word list instead.")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(f"Words sorted in ascending order (duplicates {'removed' if remove_duplicates else 'kept'}): {sort_list(word_list)}")
