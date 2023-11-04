# fhand = open('mbox.txt', 'r')
# print(fhand)
# fhand.close()

# xfile = open('mbox.txt')
# for cheese in xfile:
#     print(cheese)

# üstte satırlları tek tek sayar

# Şimdi satırları sayan bir kod yazacağız.

# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)
# fhand.close()


# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# fhand.close()

# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(inp[:20])

## Searching Through a File

# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:') :
#         print(line)

## Çıktıdaki yeni satırlar print statement tan gelen  \n
## ve okuduğu satırlardaki \n yeni satırlar var.

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:') :
#         print(line)

## Skipping with continue

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)

## iki kod da tamamen aynı

# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)
# fhand.close()


## Bad File Names

# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()

# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject line in', fname)
