# Interactive File Read & Write with Error Handling

## Description
This Python program demonstrates how to **read from a file**, **modify its contents interactively**, and **write to a new file**. Users can choose how each line of the file is modified. The program also includes **error handling** to manage cases where the file does not exist or cannot be read.

---

## Features
- Prompts the user to enter the name of the input file.
- Lets the user choose the type of modification:
  1. Convert all text to **UPPERCASE**
  2. Convert all text to **lowercase**
  3. **Replace** occurrences of `"Python"` with `"PY"`
  4. **Reverse** each line
- Writes the modified content to a new file named `modified_<original_filename>`.
- Handles `FileNotFoundError` and `IOError` to prevent program crashes.

---

## Usage

1. Save `file_read_write.py` in your project folder.
2. Run the program:

```bash
python file_read_write.py
