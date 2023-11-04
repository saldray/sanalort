# def selamlama(isim):
#     """
#     Bu fonksiyon, parametre olarak girilen kişiye selam verir
#     """
#     print("Merhaba, " + isim + ". Günaydın!")

# isim = input("Lütfen isminizi(adınızı) giriniz:")
# selamlama(isim)


# Return İfadesi
# Return ifadesi, bir fonksiyondan çıkmak ve
# fonksiyonun çağırıldığı yere geri dönmek için
# kullanılır.

# def  mutlak_deger(sayı):
#     """ Bu fonksiyon girilen sayının mutlak
#     değerini döndürür """
#     if sayı >= 0 :
#         return sayı
#     else:
#         return -sayı

# print(mutlak_deger(11))
# print(mutlak_deger(-26))

# Değişkenlerin Kapsamı ve Ömrü

# def deneme_fonk():
#     x = 26
#     print("Fonksiyon içindeki x değeri:",x)

# x = 34
# deneme_fonk()
# print("Fonksiyon dışındaki x değeri:",x)

# Fonksiyon Argümanları/Parametreleri

# def selamlama(isim, mesaj):
#     """
#     Bu fonksiyona, parametre olarak girilen isme,
#     yine parametre olarak verilen mesajı verir
#     """
#     print("Merhaba " + isim + ", " + mesaj)

# isim = input("Lütfen isminizi giriniz: ")
# mesaj = input("Lütfen mesajı giriniz: ")
# selamlama(isim, mesaj)

# Python Varsayılan Argümanlar

# Python'da parametreler varsayılan değerlere sahip olabilir.
# Atama operatörü (=) kullanılarak bir argümana varayılan bir değer sağlanabilir.

# def selamlama(isim, mesaj = "Sitemizi ziyaret ettiğiniz için teşekkür ederiz" ):
#     """
#     Bu fonksiyon, parametre olarak girilen isme, yine parametre
#     verilen mesajı verir
#     """
#     print("Merhaba " + isim + ", " + mesaj)

# isim = input("Lütfen isminizi giriniz: ")
# selamlama(isim)
# selamlama(isim, "Herkese benden çay!" )


# !!! Bir tane varsayılan argüman olduğunda, sağındaki
# tüm argümanların da varsayılan değerlere sahip
# olması gerekmektedir.

# selamlama(mesaj = "Merhaba, isim") hata verir.

# Python Anahtar Kelime Argümanları

#def selamlama(isim, mesaj = "Sitemizi ziyaret ettiğiniz için teşekkür ederiz" ):
#    """
#    Bu fonksiyon, parametre olarak girilen isme, yine parametre
#    verilen mesajı verir
#    """
#    print("Merhaba " + isim + ", " + mesaj)


# # 2 anahtar kelime argümanlı
# selamlama(isim="Fatih", mesaj="Okumak bir yaşam felsefesidir...")

# # 2 anahtar kelime argümanlı (sırasız)
# selamlama(mesaj="Okumak bir yaşam felsefesidir...", isim="Fatih")

# # 1 doğru konumda, 1 anahtar kelime argümanlı
# selamlama("Fatih", mesaj="Okumak bir yaşam felsefesidir...")


# anahtar kelime argümanlarının konumsal argümanl-
# ları takip etmesi gerektiği unutulmamalıdır.
# Anahtar kelime argümanlardan sonra konumsal
# bir argüman çağırmak hatalara neden olacaktır.

## selamlama(isim = "Fatih", "Okumak bir yaşam felsefesidir...")

# def selamlama(isim, mesaj = "Sitemizi ziyaret ettiğiniz için teşekkür ederiz" ):
#     """
#     Bu fonksiyon, parametre olarak girilen isme, yine parametre
#     verilen mesajı verir
#     """
#     print("Merhaba " + isim + ", " + mesaj)

# # selamlama(isim = "Fatih", "Okumak bir yaşam felsefesidir...")
# # selamlama("Okumak bir yaşam felsefesidir...", isim="Fatih")

# Python isteğe bağlı argümanlar

# def selamlama(*isimler):
#     """
#     Bu fonksiyon, parametre olarak verilen isimlerdeki tüm kişileri selamlar
#     """
#     for isim in isimler:
#         print("Merhaba " + isim)

# selamlama("Harun", "Kerem", "Nurullah", "Mustafa", "Orkun")


# Özyinelemeli Fonksiyonlar(Recursive)

#def faktoriyel(x):
#    """ Bu özyinelemeli fonksiyon, verilen bir tamsayının faktöriyel değerini bulmak için hazırlanmıstır    """
#    if x == 1:
#        return 1
#    else:
#        return(x * faktoriyel(x-1))
#
#sayi = 5
#print(sayi, "sayısının faktöriyel değeri: ", faktoriyel(sayi))
#


# Lambda/Anonim Fonksiyonlar

# lambda fonksiyon kullanım örneği
#kareAl = lambda x : x * x
#print("7 sayısının karesi:", kareAl(7))


# filter() fonksiyonu Örneği

# Bir listedeki elemanların sadece çift olanları filtreleyen program

#sayı_listesi = [1, 5, 4, 6, 8, 11, 3, 12]
#yeni_liste = list(filter(lambda x: (x % 2 == 0), sayı_listesi))
#
#print(yeni_liste)


# map() fonksiyonu kullanarak bir listedeki her bir
# öğenin iki katını bulan program.

#sayı_listesi = [7, 13, 51, 4, 9, 3, 11, 2, 19]
#yeni_liste = list(map(lambda x: x * 2, sayı_listesi))
#
#print(yeni_liste)

# global, local ve nonlocal Anahtar Kelimeleri


