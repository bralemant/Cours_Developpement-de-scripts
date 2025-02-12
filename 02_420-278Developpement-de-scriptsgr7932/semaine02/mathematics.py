# from math import *
# from collections import Counter

# # print(ceil(4.5))
# # print(floor(4.5))


# c = Counter(['eggs', 'ham'])
# print(c['eggs'] )

a = 'sandwich "Joe"'
b = "omelette's"
c = '''soda's cool "Joe" '''
d = """frites' Ol"Mama!" """

print(type(a), len(a))
print(type(b), len(b))
print(type(c), len(c))
print(type(d), len(d))
print(8*"*")
# print(c.capitalize())

# f = b + " " +  a[-5:]
# print(f)

# c[7:11] = "chil"
print(c)
print()
c2 = c[:7] + "chill" + c[11:]
print(c2)

print(8*"*")
print("Les listes")

l1 = ["a", "prof", 23, True]
print("Liste l1 :", l1)
print("len(l1) =", len(l1))
print("l1[1::2] =", l1[1::2])

l1.append("BYE BYE!")
print(l1)
print("len(l1) =", len(l1))