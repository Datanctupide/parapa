# a = int(input())
# if a % 2:
#     print("нечетное")
# else:
#     print("четное")


# b = int(input())
# if b > 0:
#     print("Polozhitelnoe")
# elif b == 0:
#     print("Nolь")
# else:
#     print("Otrizatelno")


# c = int(input())
# if c >= 18:
#     print("Dostup razreshen")
# else:
#     print("Dostup zapreshen")


# d = int(input())
# e = int(input())
# if d > e:
#     print(d)
# elif d < e:
#     print(e)
# else:
#     print("odinakovo")


# f = input()
# password = "python123"
# if f == password:
#     print("Pravilno")
# else:
#     print("ploxo")


# g = int(input())
# h = int(input())
# i = int(input())
# if g > h and g > i:
#     print(g)
# elif h > g and h > i:
#     print(h)
# else:
#     print(i)


# j = int(input())
# if j > 89:
#     print("A")
# elif j > 69:
#     print("B")
# elif j > 49:
#     print("C")
# elif j < 50:
#     print("F")
# else:
#     print("lol")


# k = int(input())
# if k / 3 and k / 5:
#     print("FizzBuzz")
# elif k / 3:
#     print("Fizz")
# elif k / 5:
#     print("Buzz")
# else:
#     print(k)


# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print("first")
# elif x < 0 and y > 0:
#     print("second")
# elif x < 0 and y < 0:
#     print("third")
# elif x > 0 and y < 0:
#     print("fourth")
# else:
#     print("none")


l = int(input())
n = int(input())
o = int(input())
if l == n and l == o and n == o:
    print("ravnostoroniy")
elif (l == n and l == o) or (n == l and n == o) or (o == l and o == n):
    print("ravnostoroniy")
elif l != n and l != o and n != o:
    print("rasnostoroniy")