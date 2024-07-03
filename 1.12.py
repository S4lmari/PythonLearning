# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c)/2
# s = (p * (p-a) * (p- b) * (p-c)) ** 0.5
# print (s)

# x = int(input())
# print((-15 < x <= 12) or (14<x<17) or (19<=x))

# a = float(input())
# b = float(input())
# c = input()
# if c == '+':
#     print (a+b)
# elif c == '-':
#     print(a-b)
# elif c == '/':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a/b)
# elif c == '*':
#     print(a*b)
# elif c == 'mod':
#     if b == 0:
#         print("Деление на 0!")
#     else:
#         print(a%b)
# elif c == 'pow':
#     print(a**b)
# elif c == 'div':
#     if b == 0:
#         print("Деление на 0!")
#     else:
#         print(a//b)
# else:
#     print("неверный ввод")

# forma = input()
# if forma == "треугольник":
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = (a + b + c)/2
#     s = (p * (p-a) * (p- b) * (p-c)) ** 0.5
#     print (s)
# elif forma == "прямоугольник":
#     a = float(input())
#     b = float(input())
#     print(a*b)
# elif forma == "круг":
#     a = float(input())
#     print(3.14*a**2)
# else:
#     print("ошибка")

# a = int(input())
# b = int(input())
# c = int(input())
# if (a>=b) and (a>=c):
#     if (b>=c):
#         print(a)
#         print(c)
#         print(b)
#     else:
#         print(a)
#         print(b)
#         print(c)
# elif (b>=a) and (b>=c):
#     if a>=c:
#         print(b)
#         print(c)
#         print(a)
#     else:
#         print(b)
#         print(a)
#         print(c)
# elif (c>=a) and (c>=b):
#     if b>=a:
#         print(c)
#         print(a)
#         print(b)
#     else:
#         print(c)
#         print(b)
#         print(a)

# n = int(input())       Ошибка в логике работы кода
# if 1000>=n>=0:    
#     if (n + 100)%10 == 0 or n == 0 or (5<=((n+100)%100)<=19):
#         print(str(n) + ' программистов')
#     elif (n+100)%10 == 1:
#         print (str(n) + ' программист')
#     elif (2<= (n+100)%10 <=4):
#         print (str(n) + ' программиста')
# n = int(input())
# if 0 <= n <= 1000:
#     if (n % 100) in [11, 12, 13, 14]:
#         print(str(n) + ' программистов')
#     elif n % 10 == 1:
#         print(str(n) + ' программист')
#     elif 2 <= n % 10 <= 4:
#         print(str(n) + ' программиста')
#     else:
#         print(str(n) + ' программистов')
# else:
#     print("Ошибка: введите число в диапазоне от 0 до 1000.")

bilet =input()
if int(bilet[0])+int(bilet[1])+int(bilet[2]) == int(bilet[3])+int(bilet[4])+int(bilet[5]):
    print("Счастливый")
else:
    print('Обычный')