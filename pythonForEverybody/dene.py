# def greet(lang):
#    if lang == 'es':
#        print('hola')
#    elif lang == 'fr':
#        print('bonjour')
#    else:
#        print('hello')
#
#print(greet('fr'))
#greet('en')


# iteration

# n = 5
# while  n > 0 :
#     print(n)
#     n = n - 1
# print('Blastoff!')
# print(n)


# n = 5
# while n > 0 :
#     print(n)
#     n = n - 1
# print('Blastoff!')
# print(n)

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done')

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

#while True:
#    line = input('> ')
#    if line == 'done':
#        break
#    print(line)
#print('Done!')    


#while True:
#    line = input('> ')
#    if line == 'done':
#        break
#    print(line)
#print('Done!')



# while True:
#     line = input('> ')
#     if line == 'done':
#         break
# print('Done!')

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

#### Finishing an Iteration with continue

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

#### A Simple Definite Loop

# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print('Blastoff!')

# for i in range(5,0,-1):
#     print(i)
# print("Blastoff!")

# n = 5
# while n > 0 :
#     print(n)
#     n = n - 1
# print('Blastoff!')
# print(n)

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy New Year:', friend)
# print('Done!')


########## Loop Idioms ##########
##### What We Do in Loops #####

## Looping through a Set
# basicloop.py

# print('Before')
# for thing in [9, 41, 12, 3, 74, 15] :
#     print(thing)
# print('After')

## What is the Largest Number?
## largest.py

# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)

# print('After', largest_so_far)

## Counting in a Loop

# zork = 0
# print('Before', zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + 1
#     print(zork, thing)
# print('After', zork)

## Summing in a Loop

# zork = 0
# print('Before', zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + thing
#     print(zork, thing)
# print('After', zork)

## Finding the Average in a Loop
## averageloop.py

# count = 0
# sum = 0
# print('Before', count, sum)
# for value in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
#     print('After', count, sum, sum / count)

## Filtering in a Loop

# print('Before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if value > 20:
#         print('Large number', value)
# print('After')


## Search Using a Boolean Variable

# dakika 2:45:43


# found = False
# print('Before', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3 :
#         found = True
#     print(found, value)
# print('After', found)

# found = False
# print('Before', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(found, value)
# print('After', found)


# found = False
# print('Before', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(found, value) #
# print('After', found)

#### How to find the smallest value
## python_largest.py

# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)

# print('After', largest_so_far)

#### How to find the smallest value
## smallbad.py

# smallest_so_far = -1
# print('Before', smallest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num < smallest_so_far:
#         smallest_so_far = the_num
#     print(smallest_so_far, the_num)

# print('After', smallest_so_far)

# smallest_so_far = 100 # or more big number
# print('Before', smallest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num < smallest_so_far:
#         smallest_so_far = the_num
#     print(smallest_so_far, the_num)

# print('After', smallest_so_far)

#### Finding the smallest value
## smallest.py

# smallest = None
# print('Before')
# for value in [9, 41, 12, 3, 74, 15] :
#     if smallest is None :
#         smallest = value
#     elif value < smallest :
#         smallest = value
#     print(smallest, value)


# smallest = None
# print('Before', smallest)
# for value in [9, 41, 12, 3, 74, 15] :
#     if smallest is None :
#         smallest = value
#     elif value < smallest :
#         smallest =  value
#     print(smallest, value)
#
# print('After', smallest)

#smallest = None
#print('Before', smallest)
#for value in [9, 41, 12, 3, 74, 15]:
#    if smallest is None:
#        smallest = value
#    elif value < smallest:
#        smallest = value
#    print(smallest, value)
#
#print('After', smallest)

