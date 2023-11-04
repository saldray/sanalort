# # define strings
# firstname = "Bugs"
# lastname = "Bunny"

#  # define our sequence
# sequence = (firstname,lastname)

#  # join into new string
# name = " ".join(sequence)
# print(name)


# # It can also join a list of words:
# words = ["How", "are", "you", "doing", "?"]
# sentence = ' '.join(words)
# print(sentence)

#### not use join()

# words = ["How", "are", "you", "doing", "?"]
# sentence = ""
# for word in words:
#     sentence += word + " "
# print(sentence.strip()) # use strip() to remove the
# # trailing space


# words = ["How", "are", "you", "doing", "?"]
# sentence = ""
# for word in words:
#     sentence += word + " "

# print(sentence.strip()) # use strip() to remove the
# #print(sentence)
# # trailing space

# words = ["How", "are", "you", "doing", "?"]
# sentence = ""

# for word in words:
#     sentence += word + " "

# # Remove the trailing space
# print(sentence.rstrip())


#### https://holypython.com/intermediate-python-lessons/lesson-2-python-join-method/


# lst = ["Pacific", "Atlantic", "Indian"]
# a = " ".join(lst)
# print(a)


# lst = ["Pacific", "Atlantic", "Indian"]
# a = "+".join(lst)
# print(a)

# print("x".join("Hello"))

# print(" ".join("Hello"))

# string = "Hello"
# separator = " "
# result = ""

# for char in string:
#     result += char + separator

# # Remove the last separator from the result
# result = result[:-1]

# print(result)



# string = "Hello"
# separator = "x"
# result = ""

# for char in string:
#     result += char + separator

# # Remove the last separator from the result
# result = result[:-1]

# print(result)


#### Maybe an email task with your big data:

# email_ = ["michael", "uncla.edu"]
# email_full = "@".join(email_)
# print(email_full)


# a = list(range(10))
# print(a[:-2])


## https://holypython.com/intermediate-python-exercises/exercise-2-join-method/

# lst = ["Hawaii", "Phuket", "Aruba", "Keys"]
# joined = "+++".join(lst)

# print(joined)


# addresses = ("Mr.Hathaway", "amymail.com")
# email = "@".join(addresses)

# print(email)


## join each element in the list with a space character:" "

# lst = ['Everything', 'has', 'beauty,', 'but', 'not', 'everyone', 'can', 'see.']

# str =" ".join(lst)
# print(str)


## Using .join() method join the keys in teh dictionary with a comma: ",".

# economic_growth = {"India": 7.0, "Cambodia": 7, "Tanzania": 6.9, "Bangladesh": 6.6, "Senegal": 6.6}

# str = ",".join(economic_growth)
# print(str)


## Exercise 2-e: Python join method with new line character

# poem_lst = ["Not enjoyment, and not sorrow,", "Is our destined end or way;", "But to act, that each tommorow", "Find us farther than today."]

# poem_str = "\n".join(poem_lst)
# print(poem_str)
