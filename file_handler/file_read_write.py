# File Read & Write with Error Handling assignment.

def modify_content(line, choice):
    """
    Modify each line based on user's choice.
    1 - Uppercase
    2 - Lowercase
    3 - Replace "Python" with "PY"
    4 - Reverse line
    """
    if choice == "1":
        return line.upper()
    elif choice == "2":
        return line.lower()
    elif choice == "3":
        return line.replace("Python", "PY")
    elif choice == "4":
        return line[::-1]
    else:
        return line  # no modification if the choice is invalid.


# Ask user for input file
input_file = input("Enter the name of the file to read: ")
output_file = "modified_" + input_file

# Let user choose modification type.
print("Choose modification type:")
print("1 - Convert to UPPERCASE")
print("2 - Convert to lowercase")
print("3 - Replace 'Python' with 'PY'")
print("4 - Reverse each line")
mod_choice = input("Enter your choice (1/2/3/4): ")

try:
    # Read the input file
    with open(input_file, "r") as f_in:
        lines = f_in.readlines()

    # Modify the content
    modified_lines = [modify_content(line, mod_choice) for line in lines]

    # Write to the new file
    with open(output_file, "w") as f_out:
        f_out.writelines(modified_lines)

    print(f"Modified file has been saved as '{output_file}'")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except IOError:
    print(f"Error: Could not read/write file '{input_file}'.")
