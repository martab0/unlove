import shutil
import unicodedata

# Function to get the Unicode name of a character
def get_char_name(char):
    try:
        name = unicodedata.name(char).lower().replace(' ', '_').replace('-', '_')
        return f'_{name}_'
    except ValueError:
        return f'_unicode_{ord(char):04x}_'

def unlove_filename(filename):
    # Define the standard characters
    standard_chars = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.-')

    # Check if filename contains non-standard characters
    if set(filename) <= standard_chars:
        return filename, False

    # Replace non-standard characters with their Unicode names
    new_filename = ''
    for char in filename:
        if char in standard_chars:
            new_filename += char
        else:
            new_filename += get_char_name(char)

    return new_filename, True

def process_file(filename):
    new_filename, renamed = unlove_filename(filename)

    if renamed:
        try:
            shutil.copy2(filename, new_filename)
            print(f"File renamed and copied: {filename} -> {new_filename}")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except PermissionError:
            print(f"Error: Permission denied when trying to copy '{filename}'.")
            return None
        return new_filename
    else:
        print(f"No renaming needed for: {filename}")
        return filename

# Example usage
input_filename = input("Enter the file name: ")
result = process_file(input_filename)

if result:
    print(f"Final filename: {result}")
