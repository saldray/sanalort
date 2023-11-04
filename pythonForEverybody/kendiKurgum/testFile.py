# print("Merhaba")

# with open('mbox.txt', 'r') as fhand:
#     print(fhand)

# Satır satır yazdırır.

# with open('mbox.txt') as fhand:
#     for cheese in fhand:
#         print(cheese)

# with open('mbox.txt') as fhand:
#     count = 0
#     for line in fhand:
#         count = count + 1
#     print('Line Count:', count)

# with open('mbox-short.txt') as fhand:
#     inp = fhand.read()
#     print(len(inp))

# with open('mbox-short.txt') as fhand:
#     inp = fhand.read()
#     print(inp[:20])

# Karakter saydırılır

# with open('karakter.txt') as fhand:
#     inp = fhand.read()
#     print(len(inp))

# Satırıları tamamen bastırır \n yeni satırları da bastırır

# with open('satırSaydır.txt', 'r') as fhand:
#     for satır in fhand:
#         print(satır)

# Satır sayısını verir

# with open('satırSaydır.txt') as fhand:
#     count = 0
#     for line in fhand:
#         count += 1
#     print('Line count', count)


# Searching Through a File

# with open('mbox-short.txt') as fhand:
#     for line in fhand:
#         if line.startswith('From'):
#             print(line)

## Çıktıdaki yeni satırlar print statement tan gelen \n
## ve okuduğum satırlardaki \n yeni satrılar var.

# with open('mbox-short.txt') as fhand:
#     for line in fhand:
#         line = line.rstrip()
#         if line.startswith('From:'):
#             print(line)

# with open('satırSaydır.txt') as fhand:
#     for line in fhand:
#         line = line.rstrip()
#         if line.startswith('From:') or line.startswith('from:'):
#             print(line)


# with open('satırSaydır.txt', 'r') as fhand:
#     for line in fhand:
#         line = line.rstrip().lower()
#         if line.startswith('from:'):
#             print(line)


# with open('satırSaydır.txt', 'r') as fhand:
#     lines = [line.rstrip() for line in fhand if line.rstrip().lower().startswith('from:')]
#     for line in lines:
#         print(line)

## skipping with continue

# with open('mbox-short.txt') as fhand:
#     for line in fhand:
#         line = line.rstrip()
#         if not line.startswith('From:'):
#             continue
#         print(line)

# with open('mbox-short.txt') as fhand:
#     for line in fhand:
#         line = line.rstrip()
#         if line.startswith('From:'):
#             print(line)

# Yukarıdaki iki kod da tamamen aynı.

# önce mbox.txt girilir 1797 sonucunu verir
# ardından mbox-short.txt 27 sonucunu verir

# fname = input('Enter the file name: ')
# with open(fname) as fhand:
#     count = 0
#     for line in fhand:
#         if line.startswith('Subject:'):
#             count = count + 1
#     print('There were', count, 'subject lines in', fname)

# Bad file names

# fname = input('Enter the file name: ')
# try:
#     with open(fname) as fhand:
#         count = 0
#         for line in fhand:
#             if line.startswith('Subject:'):
#                 count = count + 1
#         print('There were', count, 'subject line in', fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()

