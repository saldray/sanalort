# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/?ref=lbp
# def swapList(newList):
#     size = len(newList)

#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp

#     return newList

# newList = [12, 35, 9, 56, 24]

# print(swapList(newList))

# def swapList(newList):
#     size = len(newList)

#     temp = newList[0]
#     newList[0] = newList[size-1]
#     newList[size-1] = temp

#     return newList

# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))


#### list(map()) metodu ile

# Get input from the user. Use map() function to convert each input to int
# user_input = list(map(int, input("Enter numbers separated by a space: ").split()))

# # Call the function with the input list
# print(swapList(user_input))




# # Create an empty list
# my_list = []

# # Get the number of elements to input from the user
# num_elements = int(input("Enter the number of elements you want to add to the list: "))

# # Get the elements from the user
# for i in range(num_elements):
#     element = input(f"Enter element {i+1}: ")
#     my_list.append(element)

# # Use the list (for example, print it)
# print("The final list is:", my_list)

# In this code, we first ask the user how many elements
# they want to add to the list. We then run a for loop
# that number of times, each time asking the user for an
# element and adding it to the list. Finally, we print
# the resulting list.

# newList = []

# num_elements = int(input("Enter the number of elements you want to add to the list: "))

# for i in range(num_elements):
#         element = int(input(f"Enter element {i+1}: "))
#         # int koymazsan str olarak alır
#         newList.append(element)
# print("The final list is:", newList)


# Listenin uzunluğunu bulup ilk elemanı (n-1). elemanla
# değiştir

# swapList diye bir fonksiyon tanımla
# içinde newList diye bir parametre belirle
# kullanıcıdan öğe girişi yapması için bir döngü oluştur
# ilk olarak boş bir liste tanımla
# bu listenin kaç elemanlı olmasını istiyor diye kullanıcıya
# sor
# for döngüsü oluşturup kullanıcıdan öğe girişi al
# int değer çıkarmasını istiyorsa int(input()) diye devam et
# alınan öğeleri boş listeye gir.
# print fonksiyonu ile listeyi yazdır.


# def swapList(newList):
#     size = len(newList)

#     temp = newList[0]
#     newList[0] = newList[size -1]
#     newList[size - 1] = temp

#     return newList

# newList = [12, 35, 9, 56, 24]

# print(swapList(newList))


# def swapList(newList):
#     size = len(newList)

#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size -1] = temp

#     return newList



# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))

# ilk olarak boş bir liste tanımla
# bu listenin kaç elemanlı olmasını istiyor diye kullanıcıya
# sor
# Alınan eleman sayısına göre for döngüsünde dönüşü belirle
# for döngüsü oluşturup kullanıcıdan öğe girişi al
# int değer çıkarmasını istiyorsa int(input()) diye devam et
# alınan öğeleri boş listeye gir.
# print fonksiyonu ile listeyi yazdır.

# newList = []
# num_elements = int(input("Enter the number of elements you want to add to the list: "))

# for i in range(num_elements):
#     element = int(input(f"Enter element {i+1}: "))
#     newList.append(element)
# print("The final list is:", newList)

# print(swapList(newList))
# for i in range(num_elements):
#         element = int(input(f"Enter element {i+1}: "))
#         # int koymazsan str olarak alır
#         newList.append(element)
# print("The final list is:", newList)


# def swapList(newList):
#     size = len(newList)

#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size -1] = temp

#     return newList

# newList = []
# num_elements = int(input("Listeye eklemek istedigin eleman sayısını giriniz: "))

# for i in range(num_elements):
#     element = int(input(f"Enter element {i+1}: "))
#     newList.append(element)
# print("The final list is:", newList)
# print(swapList(newList))


# def listeDegis(yeniListe):
#     boyut = len(yeniListe)
#     temp = yeniListe[0]

#     yeniListe[0] = yeniListe[boyut - 1]
#     yeniListe[boyut - 1] = temp

#     return yeniListe

# # yeniListe = [12, 35, 9, 56, 24]

# # print(listeDegis(yeniListe))

# yeniListe = []
# elemanSayısı = int(input("Listeye eklemek istediginiz eleman sayısını giriniz: "))

# for i in range(elemanSayısı):
#     eleman = int(input(f"Eleman gir {i+1}: "))
#     yeniListe.append(eleman)

# print("Son Liste: ", yeniListe)
# print(listeDegis(yeniListe))

# ##########################################################

# def swapList(newList):
#     size = len(newList)
#     temp = newList[0]

#     newList[0] = newList[size -1]
#     newList[size -1] = temp

#     return newList

# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))

# newList = []

# num_elements = int(input("Enter elements number of the list: "))

# for i in range(num_elements):
#     element = int(input(f"Enter the element {i+1}: "))
#     newList.append(element)

# print("Last elements list: ", newList)

# newList = []
# num_elements = int(input("Enter the number of elements you want to add to the list: "))

# for i in range(num_elements):
#     element = int(input(f"Enter element {i+1}: "))
#     newList.append(element)

# print("The final list is: ", newList)


# newList = []
# num_elements = int(input("liste sayısını giriniz: "))
# for i in range(num_elements):
#     element = int(input("eleman giriniz: "))
#     newList.append(element)
# print(newList)

# def swapList(newList):
#     size = len(newList)
#     temp = newList[0]

#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp

#     return newList
# # newList = [12, 35, 9, 56, 24]
# # print(swapList(newList))

# newList = []
# num_elements = int(input("Enter element number: "))
# for i in range(num_elements):
#     element = int(input("element : "))
#     newList.append(element)

# print("last newList: ", newList)
# print(swapList(newList))


# def swapList(newList):
#     newList[0], newList[-1] = newList[-1], newList[0]

#     return newList

# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))

# def swapList(newList):

#     newList[0], newList[-1] = newList[-1], newList[0]
#     return newList
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))


# def swapList(newList):
#     size = len(newList)
#     temp = newList[0]

#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp

#     return newList

# newList = [35, 12, 9, 24, 56]
# print(swapList(newList))


# def swapList(newList):

#     newList[0], newList[-1] = newList[-1], newList[0]

#     return newList

# newList = []
# num_elements = int(input(f"Enter elements: "))
# for i in range(num_elements):
#     element = int(input(f"element: {i+1}: "))
#     newList.append(element)

# print("final list: ", newList)


# list = [1, 2, 3, 4]

# a, *b, c = list

# print(a)
# print(b)
# print(c)

# def swapList(list):
#     start, *middle, end = list
#     list = [end, *middle, start]

#     return list

# newList = [12, 35, 9, 56, 24]

# print(swapList(newList))


# virgül atamasını kullanarak listedeki iki öğenin yerini
# değiştir
# https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/?ref=lbp


# def swapPositions(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list

# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3

# print(swapPositions(List, pos1-1, pos2-1))


# largest = None

# print("Before:", largest)

# for itervar in [12, 35, 9, 56, 74, 26]:

#     if largest is None or itervar > largest:
#         largest = itervar
#     print("Loop", itervar, largest)

# print("Largest", largest)



# numElements = int(input("Enter numElements: "))
# print(numElements)
# list = []

# for itervar in range(numElements):
#     listNum = (int(input("Enter list element: ")))
#     print(listNum)
#     list.append(listNum)

# largest = None
# print('Before:', largest)

# for iter in list:
#     if largest is None or iter > largest:
#         largest = iter
#     print('Loop:', iter, largest)

# print("Largest:", largest)




# def max():
#     numElements = int(input("Enter numElements: "))
# print(numElements)
# list = []

# for itervar in range(numElements):
#     listNum = (int(input("Enter list element: ")))
#     print(listNum)
#     list.append(listNum)

# largest = None
# print('Before:', largest)

# for iter in list:
#     if largest is None or iter > largest:
#         largest = iter
#     print('Loop:', iter, largest)

# print("Largest:", largest)


# max()



# def get_largest():
#     numElements = int(input("Enter numElements: "))
#     print(numElements)
#     list_num = []

#     for _ in range(numElements):
#         listNum = int(input("Enter list element: "))
#         print(listNum)
#         list_num.append(listNum)

#     largest = None
#     print('Before:', largest)

#     for num in list_num:
#         if largest is None or num > largest:
#             largest = num
#         print('Loop:', num, largest)

#     print("Largest:", largest)

# get_largest()



# # Create an empty list
# my_list = []

# # Get the number of elements to input from the user
# num_elements = int(input("Enter the number of elements you want to add to the list: "))

# # Get the elements from the user
# for i in range(num_elements):
#     element = int(input(f"Enter element {i+1}: "))
#     my_list.append(element)

# # Use the list (for example, print it)
# print("The final list is:", my_list)


# myList = []
# numElements = int(input("Enter the number of elements you want to add to list: "))

# for itervar in range(numElements):
#     element = int(input(f"Enter element {itervar+1}: "))
#     myList.append(element)

# print("The final list is:", myList)

# myList = []
# numElements = int(input("Enter the number of elements you want to add to list: "))

# for itervar in range(numElements):
#     element = int(input(f"Enter element {itervar+1}: "))
#     myList.append(element)

# print("The final list is:", myList)

# myList = []
# numElements = int(input("Enter the number of elements you want to add to list: "))

# for itervar in range(numElements):
#     element = int(input(f"Enter element {itervar+1}: "))
#     myList.append(element)

# print("The final list is:", myList)


# myList = []
# numElements = int(input("Enter the numbers of element you want to add to list: "))

# for itervar in range(numElements):
#     element = int(input(f"Enter element {itervar+1}: "))
#     myList.append(element)

# print("The final list is:", myList)


# myList = []
# numElements = int(input("Enter the number of element you want to add to list: "))

# for itervar in range(numElements):
#     element = int(input(f"Enter element {itervar+1}: "))
#     myList.append(element)

# print("The final list is:", myList)


# largest = None
# print('Before:', largest)

# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest:
#         largest = itervar
#     print('Loop:', itervar, largest)

# print("largest", largest)


######################################3
#########################################
########################################
########################################

# def getLargest():
#     numElements = int(input("Enter the number of element you want to add to list: "))
#     myList = []
#     for itervar in range(numElements):
#         element = int(input(f"Enter element {itervar+1}: "))
#         myList.append(element)
#     print(myList)

#     largest = None
#     print('Before:', largest)
#     for iter in myList:
#         if largest is None or iter > largest:
#             largest = iter
#         print('Loop', iter, largest)

#     print("Largest: ", largest)

# getLargest()

################################################
################################################
#################################################


# def getLargest():
#     myList = []
#     numElements = int(input("Enter the number of list element you want to add to list: "))
#     for itervar in range(numElements):
#         element = int(input(f'Enter element {itervar+1}: '))
#         myList.append(element)
#     print(element)

#     largest = None
#     print('Before:', largest)
#     for iter in myList:
#         if largest is None or iter > largest:
#             largest = iter
#         print('Loop:', iter, largest)
#     print("Largest:", largest)

# getLargest()


# n = int(input("enter a num: "))
# for i in range(n):
#     print("i nin karesi:", i * i)

# n = int(input("enter a num:"))
# while       :
#     print(i * i)
#     n


# n = int(input("Enter a number: "))
# i = 0
# while i < n:
#     print("Square of i:", i * i)
#     i += 1

# def print_squares(n):
#     for i in range(n):
#         print(i**2)

# print_squares(3)

###################
###################


# Python3 program to swap first
# and last element of a list

# Swap function
#def swapList(newlist):
#    size = len(newList)
#
#    # Swapping
#    temp = newList[0]
#    newList[0] = newList[size - 1]
#    newList[size - 1 ] = temp
#
#    return newList
#
## Driver code
#newList = [12, 35, 9, 56, 24]
#
#print(swapList(newList))



#def swapList():
#    newList = []
#    numElement = int(input("Enter the number of list you want to add num: "))
#    for itervar in range(numElement):
#        element = int(input(f"Enter element {itervar+1}: "))
#        newList.append(element)
#    print(newList)
#
#    size = len(newList)
#    
#    #Swapping
#    temp = newList[0]
#    newList[0] = newList[size - 1]
#    newList[size - 1] = temp
#    print(newList)
#
#swapList()

