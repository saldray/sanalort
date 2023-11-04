# import random

# for i in range(10):
#     x = random.random()
#     print(x)


# def addtwo(a, b):
#     added = a + b
#     return added

# x = addtwo(3, 5)
# print(x)


# largest = None
# print('Before:', largest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest :
#         largest = itervar
#     print('Loop:', itervar, largest)
# print('Largest:', largest)



# smallest = None
# print('Before:', smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#     print('Loop:', itervar, smallest)
# print('Smallest:', smallest)




# Python program to find largest
# number in a list


# def myMax(list1):

#     # Assume first number in list is largest
#     # initially and assign it to variable "max"
#     max = list1[0]
# # Now traverse through the list and compare
#     # each number with "max" value. Whichever is
#     # largest assign that value to "max'.
#     for x in list1:
#         if x > max:
#             max = x

#     # after complete traversing the list
#     # return the "max" value
#     return max


# # Driver code
# list1 = [10, 20, 4, 45, 99]
# print("Largest element is:", myMax(list1))





# def max_number(arr):
#     return max(arr)

# size = int(input("Girilecek sayı adet: "))
# array = []
# for i in range(size):
#     array.append(int(input("{}.Sayıyı Gir: ".format(i + 1))))

# print("Girilen En Büyük Sayı:", max_number(array))
