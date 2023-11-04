# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/

# Given a list, write a Python program to swap first and last element of the list.

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

# Approach #1: Find the length of teh list and simply swap
# element with (n-1)th element (n-1 inci elemanla) öğe ile

# Python3 program to swap first
# and last element of a list

# Swap function

# def swapList(newList):
#     size = len(newList)

#     #Swapping
#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size -1] = temp

#     return newList

# #Driver code
# newList = [12, 35, 9, 56, 24]

# print(swapList(newList))

########
# Approach #2

# def swapList(newList):

#     newList[0], newList[-1] = newList[-1], newList[0]

#     return newList

# # Driver codes
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))


#####

# def swapList(list):
#     # Storing the first and last element
#     # as apair in a tuple variable get
#     get = list[-1], list[0]

#     # inpacking those elements
#     list[0], list[-1] = get

#     return list

# # Driver code
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))



#### Approach #4 Using * operand.

# list = [1, 2, 3, 4]

# a, *b, c = list

# print(a)
# print(b)
# print(c)

# # Now let's see the implementation of above approach:
# # Şimdi yukarıdaki yaklaşımın uygulamasını görelim.

# def swapList(list):

#     start, *middle, end = list
#     list = [end, *middle, start]

#     return list

# newList = [12, 35, 9, 56, 24]

# print(swapList(newList))


# Approach #5

# def swapList(list):

#     first = list.pop(0)
#     last = list.pop(-1)

#     list.insert(0, last)
#     list.append(first)

#     return list

# newList = [12, 35, 9, 56, 24]

# print(swapList(newList))


# Approach #6 Using slicig

# def swap_first_last_3(lst):
#     #Check if list has at least 2 elemens
#     if len(lst) >= 2:
#         #Swap the first and last elements using slicing
#         lst = lst[-1:] + lst[1:-1] + lst[:1]
#     return lst

# # Initializing the input
# inp = [12, 35, 9, 56, 24]

# # Printing the original input
# print("The original input is:", inp)

# result=swap_first_last_3(inp)

# # Printing the result
# print("The output after swap first and last is:", result)
