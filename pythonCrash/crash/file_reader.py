# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line)

# f = open("pi_digits.txt", "w")
# f.close()

# f = open("pi_digits.txt", "a")
# f.write('''3.1415926535
#   8979323846
#   2643383279''')
# f.close()

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line)


# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())


# Make a List of Lines from a File
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
