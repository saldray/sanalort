#print('Hello')

# fhand = open('gnu.txt')
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)


# fhand = open('gnu.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# fhand = open('gnu.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)
# fhand.close()

# with open('gnu.txt') as fhand:
#     count = 0
#     for line in fhand:
#         count= count + 1
#     print('Line Count:', count)

# with open('mbox-short.txt') as fhand:
#     inp = fhand.read()
#     print(len(inp))


# with open('nn.txt') as fhand:
#     inp = fhand.read()
#     print(len(inp))

# with open('gnu.txt') as fhand:
#     for line in fhand:
#         line = line.rstrip()
#         if not line.startswith('From:'):
#             continue
#         print(line)

# with open('gnu.txt') as fhand, open('output.txt', 'w') as fout:
#     for line in fhand:
#         line = line.rstrip()
#         if not line.startswith('From:'):
#             continue
#         fout.write(line + '\n')
