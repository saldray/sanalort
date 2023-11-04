# def remove_blank_lines("/home/other/Desktop/emptylinetryremove.txt"):
# # Read the contents of the file
# with open("/home/other/Desktop/emptylinetryremove.txt, 'r'") as file:
# lines = file.readlines()

# # Remove blank lines
# lines = [line for line in lines if line.strip()]

# # Write the modified contents back to the file
# with open("/home/other/emptylinetryremove.txt, 'w'") as file:
# file.writelines(lines)




def remove_blank_lines(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove blank lines
    lines = [line for line in lines if line.strip()]

    # Write the modified contents back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

# Call the function with the file path as a parameter
remove_blank_lines("/home/other/Desktop/emptylinetryremove.txt")
