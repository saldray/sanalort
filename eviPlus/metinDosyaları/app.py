# fileObject = open("deneme.txt", "w")
# fileObject.write("Merhaba\n")
# fileObject.close()

# fileObject = open("deneme.txt", "w", encoding="utf-8")
# fileObject.write("Bu\n")
# fileObject.write("bir\n")
# fileObject.write("örnek\n")
# fileObject.write("metindir\n")
# fileObject.close()

# Satırlarımızı dosyaya yazmak için liste de kullanabiliriz.

# fileObject = open("deneme.txt", "w", encoding="utf-8")
# lines = ["Bu\n", "bir\n", "örnek\n", "metindir.\n"]
# fileObject.writelines(lines)
# fileObject.close()


# Dosyamızı kapatmak için close() komutunu kullandık ancak
# Bunun yerine 'with' komutunu kullanabiliriz

# with open("deneme.txt", "w", encoding="utf-8") as fileObject:
#     lines = ["Bu\n", "bir\n", "örnek\n", "metindir.\n"]
#     fileObject.writelines(lines)
# # with komutu kendisi açtığı komutu kapatıyor
# # bu nedenle fileObject.close() komutuna gerek kalmıyor.

# with open("deneme.txt", "w") as fileObject:
#     fileObject.write("Pyton")

# Okuma modunda açalım ama bunun için dosyamızın olması
# gerekiyor. Biz daha önceden deneme.txt adlı bir dosya
# oluşturmuştuk. r (read) komudu ile dosyanın içine bir şey
# yazamayız sadece dosyayı okumamıza yarıyor.

# with open("deneme.txt", "w") as fileObject:
#     fileObject.write("Python")

# with open("deneme.txt", "r") as fileObject:
#     #fileObject.read() okuyor ve str olarak geri döndürüyor
#     # bunu bir değişkene atayalım ve ekrana yazdıralım.
#     text = fileObject.read()
#     print(text)


# open fonksiyonunda "r" modunda açmazsak python yorumlayıcı
# bunu read "r" modunda açtığımızı varsayıyor.


################ ########## #########
# read metoduna arguman verebiliriz ve kaç byte okuması
# gerektiğini söyleyebiliriz

# with open("deneme.txt") as fileObject:
#     text = fileObject.read(6)
#     print(text)

# with open("deneme.txt") as fileObject:
#     text = fileObject.readline()
#     print(text)
#     text = fileObject.readline()
#     print(text)

# varsa readline fonksiyonunun metnimizde okuduğu EOL (ends
# of line) ve \n newline karakterlerini okuyor
# ve print fonksiyonunun içindeki \n newline boşluk bırakıl
# masına neden oluyor.

# with open("deneme.txt") as fileObject:
#     text = fileObject.readline()
#     print(text, end="")
#     text = fileObject.readline()
#     print(text, end="")


# with open("deneme.txt") as fileObject:
#     for lineText in fileObject.readlines():
#         print(lineText, end="")

# python da for döngüsünü kullandığımızda readlines metodunu
# kullanmamız mecburi değil. Yani doğrudan dosyamızın değiş
# kenini kullanmamız yeterli olur.


# with open("deneme.txt") as fileObject:
#     for lineText in fileObject:
#         print(lineText, end="")

########### hem okuyup hem yazabilmek için "r+" ############

# with open("deneme.txt", "r+") as fileObject:
#     for lineText in fileObject:
#         print(lineText, end="")
#     fileObject.write(".")
# ilk başta önce okuyup sonra yazdığı için yorumlayıcıda
# nokta işareti gözükmeyecek ikiciye çalıştırırsak ilk
# basılan görülecek ikici basılan görülmeyecek


# ########### "a", append modu ##################

# with open("deneme.txt", "a") as fileObject:
#     fileObject.write("Python is awesome.")


# with open("deneme.txt", "a") as fileObject:
#     fileObject.write("Python is awesome.\n")

# with open("deneme.txt", "a+") as fileObject:
#     fileObject.write("Python is awesome.\n")
#     text = fileObject.read()
#     print(text)

# "a" modunda açılan bir dosyanın işaretçisi (pointer)ı
# satırın sonu olur. Okumaya kalktığımızda işaretçe en sonda
# olduğu için bir şey kalmadığından bir şey okuyamıyor
# Bunları okumak için seek metodunu kullanırız.


# with open("deneme.txt", "a+") as fileObject:
#     fileObject.write("Python is awesome.\n")
#     fileObject.seek(0)
#     text = fileObject.read()
#     print(text)
# seek(0) sıfır verirsek dosyamızın en başından başlatırız.

# with open("deneme.txt", "a+") as fileObject:
#     fileObject.write("Python is awesome.\n")
#     fileObject.seek(0)
#     text = fileObject.read()
#     print(text)
#     fileObject.seek(0)
#     text = fileObject.read()
#     print(text)
# # boşluk print fonksiyonunun \n sinden kaynaklanıyor.


# program bir dosyamızın içeriğini alsın ve karakterlerin
# yerini ters çevirsin yani en sonuncu karakter başa gelsin
# en baştaki karakter en sona gelsin ve yeni bir dosya
# oluştursun.

# Read modunda açacağım hiçbir şey yazmasamda olur.

# with open("deneme.txt") as fileObject:
#     text = fileObject.read()
#     print(f"Dosya: {fileObject.name}")
#     print(text)

# with open("deneme_ters.txt", "w") as fileObject:
#     # yukarıda fileObjectle işim bitti tekrar kullanabilirim
#     print(f"Dosya: {fileObject.name}")
#     text = text[::-1]
#     # yukarıda aldığımız text'i dosyaya yazalım.
#     fileObject.write(text)
#     print(text) # buraya kadar eski dosyamızım içeriğinin
#     #yeni dosyamıza yazıyoruz. Dosyayı yazdırmadan önce ters
#     # çevirelim text = text[::-1]

# Ödev 19:

 # Programın kullanıcının ismini girdiği metin dosyasının
 # satır sayısı, kelime sayısı ve en uzun kelimenin
 # uzunluğunu bulmanı istiyorum.

 # Ödev 18:
 # Ödevimiz bizden bir program yazmamızı ve
 # programın kullanıcının girdiği cümlede bulunan yasaklı
 # kelimelerin yerine nokta işareti koymamızı istiyordu
 # ve terminale bu şekilde bastımamızı istiyordu.


#  bannedWords = ["amk", "aq"]

#  string = input("Bir cümle giriniz: ")

#  words = string.split()
#  # split bir liste dönüyordu.

#  string = ""

#  for word in words:
#      if word in bannedWords:
#          string += ' . ' # string'i baştan oluşturmak için
#          # üste gidip string = ""
#      else:
#          string += f"{word}"
# print(string)

# liste yerine sözlük yaratırsak . (nokta) yerine istediğimiz
# kelimeyi koyabiliriz



#  bannedWords = {
#      "amk": "lanet olsun",
#      "aq": "*"
#                }

#  string = input("Bir cümle giriniz: ")

#  words = string.split()
#  # split bir liste dönüyordu.

#  string = ""

#  for word in words:
#      if word in bannedWords:
#          string += f" {bannedWords[word]} "
#      else:
#          string += f"{word}"
# print(string)



# okuma modunda 'r' bir boşluk bırakıyor \n yapıyor bunu engellemek
# için rstrip kullanabilirsin.
