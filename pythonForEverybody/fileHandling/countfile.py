# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)
# fhand.close()


# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:') :
#         print(line)
# fhand.close()

## metin'den gelen bir \n newline ve print() fonksiyonundan
## gelen \n newline var çıktıda print fonksiyonunun newline
## ından


# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:') :
#         print(line)
# fhand.close()

## Skipping with continue

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:') :
#         continue
#     print(line)
# fhand.close()


## Using in to select lines
## We can look for a string anywhere in a line as our
## selection criteria
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line :
#         continue
#     print(line)
# print(line)
# fhand.close()

## Prompt for File Name

# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:') :
#         count = count + 1
# print('There were', count, 'subject lines in', fname)
# fhand.close()


# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()
# count = 0
# for line in fhand:
#     if line.startswith('Subject:') :
#         count = count + 1
# print('There were', count, 'subject lines in', fname)
# fhand.close()

