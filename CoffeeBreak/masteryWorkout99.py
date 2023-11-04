#n, count = 5, 0
#for _ in range(n):
#    n -= 1
#    count +=1
#print(count)

# n = 5
# count 0
# range(5) [0, 1, 2, 3, 4]
# n = n - 1
# count = count + 1

# _  n  count
# 0  4  1
# 1  3  2
# 2  2  3
# 3  1  4
# 4  0  5
# print(count) # 


#def swap(a, b):
#    return b, a
#
#a, b = 1, 2
#a, b = swap(a, b)
#print(a - b)

# fonksiyon swap() tuple değer döner. swap() fonksiyonuna gelen
# a = 1, b = 2  return ile  2, 1 döner
# print(2 - 1) yazdırılır.


# Boolean Conversion

#x = 0
#if False or [False] or (False):
#    x += 1
#print(x)

# (False) doesn't create a tuple but is the same as just False.
# (False) bir tanımlama grubu oluşturmaz ancak False ile aynıdır.


# Tuple Constructor : Tuple Oluşturucu

#s = 'abc'
#for _ in range(10):
#    s = tuple(s)
#print(len(s))

# Popping List Elements

#The pop() method in Python removes the item at the given index 
#from the list and returns the removed item. By default, 
#it removes the last item. So, t.pop() will first remove 
#and return 4, then 3, and then 2.
#
#This line: x = t.pop() > t.pop() > t.pop() is evaluated 
#as x = 4 > 3 > 2. This comparison is evaluated from left to right
#, so it first checks if 4 > 3 (which is True), and then checks 
#if True > 2. However, in Python, True is equivalent to 1 when 
#used in a numerical context. So, it essentially checks 
#if 1 > 2, which is False. So, x is False.


# Extending Lists

#t = [1, 2, 3, 4]
#x = (t.pop() < t.pop()), t.pop()
#t.extend(x)
#print(len(t)) # [1, 2, False] 
#


#    t = [1, 2, 3, 4]: This initializes a list t with four elements.
#
#    x = (t.pop() < t.pop()), t.pop(): This line does a couple of
#    things. The pop() function removes the last item in the list
#    and returns it. So, t.pop() removes 4 from list t and returns it. The second t.pop()
#    removes 3 and returns it. The comparison 4 < 3 results in False. The third t.pop() 
#    removes 2 and returns it. So, x becomes a tuple: (False, 2).
#
#    t.extend(x): The extend() method in Python adds elements from a list (or any iterable) 
#    to the end of the current list. Here, it adds each element of the tuple x 
#    (False and 2) to the list t. Now t is [1, False, 2].
#
#    print(len(t)): This prints the length of t to the console, which is 3 
#    since t has three elements (1, False, and 2).


# 4.2 list.extend() vs. list.append()

#t = [0, 1, 2]
#t.extend([])
#t.append([])
#print(len(t))

#t = [0, 1, 2]: Creates a list t with three elements.
#
#t.extend([]): The extend() function is used to add elements from an iterable (like list, tuple, etc.) to the end of a list. In this case, an empty list is provided, so it does not add any elements to t.
#
#t.append([]): The append() function adds its argument as a single element to the end of a list. Here, the argument is an empty list [], so the list t becomes [0, 1, 2, []] after this step. The empty list is considered as one element in the list t.
#
#print(len(t)): Finally, this statement prints the length of t, which is 4, because t now has four elements: 0, 1, 2, and [].

# Yazbelden append() ve extend() metodu
# append()

# append kelimesi ingilizcede 'eklemek, ilave etmek
# iliştirmek' gibi anlamlara gelir.

# liste = ["elma", "armut", "çilek"]
# liste.append("erik")
# print(liste)

# yeni öğeyi(elemanı) listenin sonuna ekler.
# Yukarıdaki kodu şöyle de yapabiliriz

# liste = ["elma", "armut", "çilek"]
# liste = liste + ["erik"]
# print(liste)

# Bu iki yöntem işleyiş bakımından da birbirinden
# ayrılıyor. Zira + işlecini kullandığımızda
# listeye yeni bir öğe eklerken aslında liste
# adlı başka bir liste daha oluşturmuş oluyoruz.

# istelerin değiştirilebilir (mutable) veri tipleri
# olduğunu söylemiştik. İşte append() metodu
# sayesinde listelerin bu özelliğinden sonuna
# kadar yararlanabiliyoruz. + işlecini
# kullandığımızda ise, orijinal listeyi değiştirmek
# yerine yeni bir liste oluşturduğumuz için,
# sanki listelere karakter dizisi muamelesi yapmış
# gibi oluyoruz.


# işletim_sistemleri = ["Windows", "GNU/Linux", "Mac Os X"]
# platformlar = ["IPhone", "Anroid", "S60"]
# hepsi = işletim_sistemleri + platformlar
# print(hepsi)

# işletim_sistemleri = ["Windows", "GNU/Linux", "Mac Os X"]
# platformlar = ["IPhone", "Android", "S60"]
# for i in platformlar:
#     işletim_sistemleri.append(i)

# print(işletim_sistemleri)

# # append tek bir parametre aldığı için for döngüsü
# # kurduk

# liste = [1, 2, 3]
# liste.append(4, 5, 6)
# Bir argüman aldığı için hata verir.

# liste = [1, 2, 3]
# for i in [4, 5, 6]:
#     liste.append(i)

# print(liste)


# liste = [1, 2, 3]
# liste.append([4, 5, 6])
# print(liste) # tek bir öğe gibi ekler

# Diyelim ki kullanıcının girdiği bütün sayıları
# birbiriyle çarpan bir uygulama yazmak istiyoruz.

# sonuc = 1

# while True:
#     sayı = input("sayı (hesaplamak için q): ")
#     if sayı == "q":
#         break

#     sonuc *= int(sayı)

# print(sonuc)


# kontrol = []
# sonuc = 1

# while True:
#     sayı = input("sayı (hesaplamak için q): ")
#     if sayı == "q":
#         break
#     kontrol.append(sayı)
#     sonuc *= int(sayı)

# if len(kontrol) < 2:
#     print("Yeterli sayı girilmedi!")
# else:
#     print(sonuc)

# extend()

# extend kelimesi ingilizce 'genişletmek, yaymak'

# li1 = [1, 3, 4]
# li2 = [10, 11, 12]
# li1.append(li2)

# print(li1)


# li1 = [1, 3, 4]
# li2 = [10, 11, 12]
# li1.extend(li2)

# print(li1)

# isletim_sistemleri = ["Windows", "GNU/Linux", "Mac Os X"]
# platformlar = ["IPhone", "Android", "S60"]
# isletim_sistemleri.extend(platformlar)
# print(isletim_sistemleri)




