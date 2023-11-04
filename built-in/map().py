# print('Selam')

# https://realpython.com/python-map-function/

# numbers = [1, 2, 3, 4, 5]
# squared = []

# for num in numbers:
#     squared.append(num ** 2)

# print(squared)


# def squared(number):
#     return number ** 2

# numbers = [1, 2, 3, 4, 5]

# # map(fun, iter)
# squared = map(squared, numbers)
# print(list(squared))

# str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
# int_nums = map(int, str_nums)
# # print(int_nums)
# # <map object at 0x7fdaea9d2680>
# # özgün dize değiştirilmiyor, listeye çevirmem lazım
# print(list(int_nums))
# print(str_nums)


# Using map() with different kinds of functions

# numbers = [-2, -1, 0, 1, 2]

# abs_values = list(map(abs, numbers))
# print(abs_values)

# print(list(map(float, numbers)))

# words = ["Welcome", "to", "Real", "Python"]
# print(list(map(len, words)))


# numbers = [1, 2, 3, 4, 5]

# squared = map(lambda num: num ** 2, numbers)

# print(list(squared))

###########
# Processing Multiple Input Iterables With map()
# consider the following example that uses pow():

# first_it = [1, 2, 3]
# second_it = [4, 5, 6, 7]

# print(list(map(pow, first_it, second_it)))



# print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))

# print(list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8])))

## Transforming Iterables of Strings With Python's map()

# string_it = ["processing", "strings", "with", "map"]
# print(list(map(str.capitalize, string_it)))

# print(list(map(str.upper, string_it)))

# print(list(map(str.lower, string_it)))


# a = "HellO DunYa"
# print(a.swapcase())


# strip() varsayılan boşluk karakteridir ancak başka şeylerde kaldı
# rabiliriz.

# with_spaces = ["processing", "  strings", "with   ", " map   "]

# print(list(map(str.strip, with_spaces)))


# with_dots = ["processing..", "...strings", "with....", "..map.."]

# print(list(map(lambda s: s.strip("."), with_dots)))





# import re

# def remove_punctuantion(word):
#     return re.sub(r'[!?.:;,"()-]', "", word)

# print(remove_punctuantion("...Python"))


# text = """ Some people, when confronted with a problem, think
# "I know, I'll use regular expressions."
# Now they have two problems. Jamie Zawinski"""

# words = text.split()
# print(words)

# print(list(map(remove_punctuantion, words)))


### Implementing a Caesar Cipher Algorithm


# Original alphabet: abcdefghijklmnopqrstuvwxyz
# Alphabet rotated by three: defghijklmnopqrstuvwxyzabc

# def rotate_chr(c):
#     rot_by = 3
#     c = c.lower()
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     # Keep punctuation and whitespace
#     if c not in alphabet:
#         return c
#     rotated_pos = ord(c) + rot_by
#     # If the rotation is inside the alphabet
#     if rotated_pos <= ord(alphabet[-1]):
#         return chr(rotated_pos)
#     # If the rotation goes beyond the alphabet
#     return chr(rotated_pos - len(alphabet))

# print("".join(map(rotate_chr, "My secret message goes here.")))

## ord("a") #97  ord("b") # 98
## chr(97) 'a', chr(98) 'b'



# def powers(x):
#     return x ** 2, x ** 3

# numbers = [1, 2, 3, 4]

# print(list(map(powers, numbers)))



## the math module like sqrt(), factorial(), sin(), cos(), and so on.

# import math

# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(list(map(math.factorial, numbers)))



## Converting Temperatures

# def to_fahrenheit(c):
#     return 9 / 5 * c + 32

# def to_celsius(f):
#     return (f - 32) * 5 / 9

# celsius_temps = [100, 40, 80]
# #Convert to Fahrenheit
# print(list(map(to_fahrenheit, celsius_temps)))


# fahr_temps = [212, 104, 176]
# #Convert to Celsius
# print(list(map(to_celsius, fahr_temps)))



## Converting Strings to Numbers

# # Convert to floating-point
# print(list(map(float, ["12.3", "3.3", "-15.2"])))

# # Convert to integer
# print(list(map(int, ["12", "3", "-15"])))



# def to_float(number):
#     try:
#         return float(number.replace(",", "."))
#     except ValueError:
#         return float("nan")

# print(list(map(to_float, ["12.3", "3,3", "-15.2", "One"])))


## Combining map() With Other Functional Tools


# import math

# def is_positive(num):
#     return num >= 0


# def sanitized_sqrt(numbers):
#     cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
#     return list(cleaned_iter)

# print(sanitized_sqrt([25, 9, 81, -16, 0]))




## map() and reduce()

# import functools
# import operator
# import os

# files = os.listdir(os.path.expanduser("~"))

# print(functools.reduce(operator.add, map(os.path.getsize, files)))



# import functools
# import operator
# import os

# files = os.listdir(os.path.expanduser("~"))

# print(functools.reduce(operator.add, map(os.path.getsize, files)))



# # Transformation function
# def square(number):
#     return number ** 2

# numbers = [1, 2, 3, 4, 5, 6]

# # Using map()
# print(list(map(square, numbers)))

# # Using a list comprehension
# kare = [square(x) for x in numbers]
# print(kare)



# ## Using Generator Expressions

# # Transformation function
# def square(number):
#     return number ** 2

# numbers = [1, 2, 3, 4, 5, 6]

# # Using map()
# map_obj = map(square, numbers)
# print(map_obj)

# print(list(map_obj))


# # Using a generator expression
# gen_exp = (square(x) for x in numbers)
# print(gen_exp)

# print(list(gen_exp))


# print(list(square(x) for x in numbers))


## https://www.geeksforgeeks.org/python-map-function/
