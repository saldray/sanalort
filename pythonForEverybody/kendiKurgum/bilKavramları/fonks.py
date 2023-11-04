# def fib(n):
#     a,b = 0,1
#     while a<n:
#         print(a)
#         a,b = b,a+b

# fib(20)


# def fact(n):
#     a = 1
#     sonuc = 1
#     while a <= n:
#         sonuc = sonuc * a
#         a = a + 1
#     return sonuc

# print(fact(5))

# n! = n*(n-1)!

# def facto(n):
#     return n * facto(n-1)
# # sonsuza kadar gidiyor bir yerde durmasını
# # söylemem lazım bunu nasıl yapacağım

# def facto(n):
#     if(n==0):
#         return 1 # bitiş durumunu belirttim
#     return n * facto(n-1)

# print(facto(5))


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))  # Output: 120

# fibonacci serisini recursive yazalım

# 0,1,1,2,3,5,8,13 fibo
# 0,1,2,3,4,5,6,7  terim

# fibo(7) = fibo(6) + fibo(5)

# def fibo(n):
#     return fibo(n-1) + fibo(n-2)
# # ancak burada kontrol şartı koymam gerekiyor
# # yoksa sonsuza kadar gidecek

# def fibo(n):
#     if(n==0): return 0
#     if(n==1): return 1
#     return fibo(n-1) + fibo(n-2)

# print(fibo(7)
