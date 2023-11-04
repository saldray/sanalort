# https://pythonlobby.com/python-string-exercises-with-solution/
# Write a program to reverse a string in python.
# Hint
# Input: python
# Expected output
# Result is: nohtyp

# WAP to reverse a string

#str = input("Input a word to reverse: ")
#
#for i in range(len(str) -1, -1, -1):
#    print(str[i], end="")
#print("\n")



## Method 1: Using String Slicing


#def reverse_string(string):
#    reversed_string = string[::-1]
#    return reversed_string
#
## Example usage
#
#input_string = "python"
#reversed_string = reverse_string(input_string)
#print("Result is:", reversed_string)
#
#string = input("input a word the reverse:")
##reverse_string(string)
#print(reverse_string(string))


## Method 2: Using the reversed() Function


#def reverse_string(string):
#    reversed_string = ''.join(reversed(string))
#    return reversed_string
#
## Example usage
#
#input_string = "python"
#reversed_string = reverse_string(input_string)
#print("Result is:", reversed_string)



## Method 3: Using a Loop


#def reverse_string(string):
#    reversed_string = ""
#    for char in string:
#        reversed_string = char + reversed_string
#    return reversed_string
#
## Example usage
#
#input_string = "python"
#reversed_string = reverse_string(input_string)
#print("Result is:", reversed_string)


## Method 4: Using the join() and reversed() Functions


#def reverse_string(string):
#    reversed_string = ''.join(reversed(string))
#    return reversed_string
#
## Example usage
#
#input_string = "python"
#reversed_string = reverse_string(input_string)
#print("Result is:", reversed_string)

## Exercise 2: Write a program to count vowels and
# consonants in a string.
# Hint
# Input: python
# Expected output
# Vowels count is: 1
# Consonant count is: 5

# WAP to cout vowels and consonant
#n = input("Enter a Word ")
#vow = 0
#con = 0
#for i in range(len(n)):
#    if n[i] in ['a', 'e', 'i', 'o', 'u']:
#        vow = vow + 1
#    else:
#        con = con + 1
#print("Total vowels are:", vow)
#print("Total conconants are:", con)


## Exercise 3: Write a program to remove duplicates in a
# string
# Hint
# Input: pythonlobby
# Expected output
# Result is: p y t h o n l b


# WAP to remove duplicates in a string
#n = input("Enter a Word ")
#x = []
#for i in range(len(n)):
#    if n[i] not in x:
#        x.append(n[i])
#    else:
#        pass
#for i in range(len(x)):
#    print(x[i], end=" ")

#set()
#
#set() fonksiyonu list() fonksiyonuna çok benzer.
#Bu fonksiyon da tıpkı list() fonksiyonu gibi, veri 
#tipleri arasında dönüştürme işlemleri gerçekleştirmek 
#için kullanılabilir. set() fonksiyonunun görevi farklı 
#veri tiplerini kümeye dönüştürmektir:
#
#k = set()
#
#Burada boş bir küme oluşturduk. Şimdi de mesela bir 
#karakter dizisini kümeye dönüştürelim:
#
#i = 'istihza'
#
#set(i)

#{'t', 's', 'z', 'a', 'i', 'h'}


# kümeler aynı öğeyi birden fazla tekrar etmez.

#def remove_duplicates(string):
#    # Convert the string into a set to remove duplicates
#    unique_chars = set(string)
#
#    # Convert the set back to a string
#    result = ''.join(unique_chars)
#
#    return result
#
## Test the function
#input_string = "pythonlobby"
#output_string = remove_duplicates(input_string)
#print("Result is:", output_string)


# Exercise 4: Write a program to count the number of letters
# in a word.
# Hint
# Input: pythonlobby
# Expected output
# Result is: 11

# WAP to remove duplicates in a string
#n = input("Enter a string ")
#count = 0
#for i in range(len(n)):
#    count = count + 1
#print(count)


# Exercise 5: Python program to count the occurrence of each# character in a word.
# Hint
# Given x = programm
# Expected output
# Occurrence of each characters is:
# {‘P’: 1, ‘r’: 2, ‘o’: 1, ‘g’: 1, ‘a’: 1, ‘m’: 2}

#strr = "Programm"
#
## empty dictionary
#dic = {}
#
#for ele in strr:
#    if ele in dic:
#        dic[ele] += 1
#    else:
#        dic[ele] = 1
#
## result
#print("occurrence of each characters is :\n" + str(dic))



#def count_characters(word):
#    # Create an empty dictionary to store the character counts
#    char_counts = {}
#
#    # Iterate through each character in the word
#    for char in word:
#        # Check if the character is already in the dictionary
#        if char in char_counts:
#            # If it is, increment the count by 1
#            char_counts[char] += 1
#        else:
#            # If it is not, add the character to the dictionary with a count of 1
#            char_counts[char] = 1
#
#    # Print the occurrence of each character
#    print("Occurrence of each character is:")
#    print(char_counts)
#
## Test the function with the given word
#word = "programm"
#count_characters(word)



# Exercise 6: Python program to convert lower lettter to 
# upper and upper letter to lower in a string
# Hint
# Input: PrOgRaMM
# Expected output
# Result is: pRoGrAmm


#num = input("Enter a String ")
#x = []
#for i in range(len(num)):
#    if num[i].isupper():
#        x.append(num[i].lower())
#    elif num[i].islower():
#        x.append(num[i].upper())
#
## printing result
#for i in range(len(x)):
#    print(x[i], end=' ')



#def convert_case(string):
#    converted_string = ""
#    for char in string:
#        if char.islower():
#            converted_string += char.upper()
#        elif char.isupper():
#            converted_string += char.lower()
#        else:
#            converted_string += char
#    return converted_string
#
## Example usage
#input_string = "PrOgRaMM"
#result = convert_case(input_string)
#print("Result is:", result)



#Exercise 7: Python program to search a specific word in a string.
#
#Hint
#Input:
#Enter a String:  I am a boy
#Enter a word to search: boy
#
#Expected output
#boy exists in string
#
#Hint
#Input:
#Enter a String:  I am a boy
#Enter a word to search: girl
#
#Expected output
#girl not exists in string
#
#


#num = input("Enter a string ").split()
#search = input("Enter a word to search ")
#if search in num:
#    print(f"{search} exist in String")
#else:
#    print(f"{search} not exist in String")
#
#Explanation
#
#    The user is prompted to enter a string using the 
#    input() function. The split() function is used to 
#    split the string into individual words and store 
#    them in the num
#    variable.
#    The user is then prompted to enter a word to search 
#    for, which is stored in the search variable.
#    The code checks if the search word exists in the 
#    num list using the in operator.
#    If the word is found, the code prints a message 
#    indicating that the word exists in the string.
#    If the word is not found, the code prints a 
#    message indicating that the word does not exist in 
#    the string.
#

## Prompt the user to enter a string
#string = input("Enter a String: ")
#
## Prompt the user to enter a word to search
#word = input("Enter a word to search: ")
#
## Check if the word exists in the string
#if word in string:
#    print(word, "exists in the string")
#else:
#    print(word, "does not exist in the string")

