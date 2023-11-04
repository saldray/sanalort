# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# summation = numbers + letters
# print(summation)
# summation = letters + numbers
# print(summation)
# print(type(summation))

# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# summation = numbers + letters
# print(summation)
# summation = letters + numbers
# summation.append('python')
# print(summation)
# print(numbers, letters)
# print(type(summation))
# # Orijinal listemiz tamamen değişmeden kaldılar
# # summation tamamen yeni bir liste

# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# #multiplyList = 4 * letters
# multiplyList = letters * 4
# print(multiplyList)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # numbers listesinin öğelerinin karesi ile yeni bir
# # liste oluşturalım adı 'squares' olsun.
# # squares = list() aynısını yapar
# squares = []
# for number in numbers:
#     squares.append(number**2)

# print(squares)

# # 2. yöntem

# squares2 = [number for number in numbers]

# print(squares2)

# squares2 = [number**2 for number in numbers]

# print(squares2)

# Aynı sonucu almak için şöyle de yapabiliriz.

# squares = []
# for number in range(1, 11):
#     squares.append(number**2)

# print(squares)

# squares2 = [number**2 for number in range(1, 11)]

# print(squares2)

# Eşkenar üçgenlerin alanlarını hesaplayalım
# kenar uzunluklarının tam sayı olduğunu varsayalım.
# bir range aralığındaki misal range(1,11) gibi

# area = ((side**2)*(3**(1/2)))/4
# areas = [((side**2)*(3**(1/2)))/4 for side in range(1, 11)]
# print(areas)
# kenarının alanı 1 olanın 2 olanın 3 olanın ...
# sırası ile hesaplıyor.


# Yeni bir liste oluşturalım ama bu listede 1 den
# 10000 e kadar olan tüm 3 e bölünen çift sayıları
# listelemiş olalım.

# numbers = [number for number in range(2, 10001, 2)]
# print(numbers)

# 3 e tam bölünenleri istiyoruz

# numbers = [number for number in range(2, 10001, 2) if number % 3 == 0]
# print(numbers)


# names = ['Onur', 'Leyla', "osman", "Lale", "Orçun", 'Jale']

# Bu listeden ilk harfleri 'O' olan adları ayrıştırıp
# yeni bir liste oluşturacağız

# namesStartWithO = [name for name in names]
# print(namesStartWithO)

# names listesinin aynısını oluşturduk şimdi
# listelerde olan bir metod kullanacağız startswith()
# ne verirsek stringlerin başına bakıp bize True ya da
# False verecek

# namesStartWithO = [name for name in names if name.startswith('O')]
# print(namesStartWithO)

# küçük harfle yazılan osman'ı bize vermedi. Düzelmek için
# names = ['Onur', 'Leyla', "osman", "Lale", "Orçun", 'Jale']
# namesStartWithO = [name for name in names if name.startswith('O') or name.startswith('o')]
# print(namesStartWithO)

# ikinci bir yol ise upper() ile çağırırız upper()
# ne yapıyordu büyük harf yapıyordu bir değişkene atıyordu
# biz dönüştürünce zaten sonucu oluşturmuş oluyoruz.
# ilk harflerini kontrol edeceğiz.

# names = ['Onur', 'Leyla', "osman", "Lale", "Orçun", 'Jale']
# namesStartWithO = [name for name in names if name.upper().startswith('O')]
# print(namesStartWithO)


# list1 = [20, 30, 40]
# list2 = [3, 7, 11, 13]

# newList = []
# for x in list1:
#     for y in list2:
#         newList.append(x * y)

# print(newList)

# ### Daha basit bir yöntemle ####

# list1 = [20, 30, 40]
# list2 = [3, 7, 11, 13]

# newList = [x * y for x in list1 for y in list2]

# print(newList)


# 400 den büyük sayıları listemizde görmek
# istemiyorsak

# list1 = [20, 30, 40]
# list2 = [3, 7, 11, 13]

# newList = [x * y for x in list1 for y in list2 if x * y <= 400]

# print(newList)

# 300 den büyük sayıları istemiyorsak


# list1 = [20, 30, 40]
# list2 = [3, 7, 11, 13]

# newList = [x * y for x in list1 for y in list2 if x * y <= 300]

# print(newList)


# list1 = [20, 30, 40]
# list2 = [3, 7, 11, 13]

# newList = [x * y for x in list1 for y in list2 if x * y <= 200]

# print(newList)

# Eğer bu listede 120 varsa ona göre bir print yazalım


# list1 = [20, 30, 40]
# list2 = [3, 7, 11, 13]

# if 120 in [x * y for x in list1 for y in list2 if x * y <= 200]: # : iki noktayı unutma
#     print("120 is in the list")


# list1 = [20, 30, 40]
# list2 = [3, 7, 11, 13]

# number = 120 # eğer 100 olsaydı bir şey yapmazdı

# if 120 in [x * y for x in list1 for y in list2 if x * y <= 200]: # : iki noktayı unutma
#     print("120 is in the list")

# koordinatlardan oluşan bir liste yazalım

# coordinates = [5, 3, 3]
# multiply = coordinates[0] * coordinates[1] * coordinates[2]
# print(multiply)

# Böyle yazmak yerine

# coordinates = [5, 3, 3]
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# multiply = x * y * z
# print(multiply)

# Python'da unpacking diye bir özellik var.


# coordinates = [5, 3, 3]
# x, y, z = coordinates # items sayısı ile değişken sayısı aynı olmalı
# multiply = x * y * z
# print(multiply)


# coordinates = [5, 3, 3, 4, 2, 6]
# x, y, z = coordinates[0:3] # listemizi dilimledik
# multiply = x * y * z
# print(multiply)


# coordinates = [5, 3, 3, 4, 2, 6]

# for index in range(int(len(coordinates)/3)):
#                    x, y, z = coordinates[index * 3:3 + index * 3]
#                    print(x * y * z)
# range her zaman integer bir değer alır.
# Bölme işlemi ise float bir değer verir.


# Ödev 15:

# Kullanıcıdan en az 5 farklı isim girmesini ve eğer
# girdiği isim daha önce girilmişse hata vermesini
# girilmemişse listeye eklenmesini istiyorum.
# Program çıkışında oluşan listeyi terminale bastırsın

# Ödev 14:

# Kullanıcıdan en az 10 adet tam sayı almanı ve bu
# sayıların arasında mükerrer girilenler varsa
# silmeni istiyorum.


# Çözüm 14:
# Sonsuz bir döngü yaratıyorum çünkü ne kadar dönece-
# ğimi bilmiyorum. Döngünün içinde buna karar verece-
# ğim için uygun bir yerde break komutunu koyacağım.

# numbers = []
# uniques = []
# index = 1
# while True:
#     number = input("Enter an integer number: ")
#     if number == "" and index > 10:
#         break
#     elif number == "":
#         continue
#     numbers.append(int(number))
#     if int(number) not in uniques:
#         uniques.append(int(number))
#     index += 1

# print(numbers)
# print(uniques)


# index numarasını görmüyorum görmek için

numbers = []
uniques = []
index = 1
while True:
    number = input(f"Enter an integer number({index}): ")
    if number == "" and index > 10:
        break
    elif number == "":
        continue
    numbers.append(int(number))
    if int(number) not in uniques:
        uniques.append(int(number))
    index += 1

print(numbers)
print(uniques)
