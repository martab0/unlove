# unlove
 Un...love file name

Replace problematic characters in file name with their Unicode descriptions.
Allowed characters are defined in variable `standard_chars`.

* Specification: Marta Bartnicka
* Written by: Claude v3.5 Sonnet

## How to run
```
python unlove_filename.py
```

## How to use

1. Unlove asks for a name of the file to process. It assumes the file is located in the same directory.
2. Unlove parses the file name and looks for characters that are not on the list defined in variable `standard_chars`.
3. If no such characters are found, the file is left unchanged.
4. If any characters outside the list are found, the file is renamed to a safer name where each non-standard character is replaced by its Unicode name. The original file is not deleted.


