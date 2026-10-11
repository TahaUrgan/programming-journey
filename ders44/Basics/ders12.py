def mesaj():
    print("Merhaba")

print("1")

mesaj()

print("2")

mesaj()

def topla(a, b):
    print(a + b)

def carp(a, b):
    print(a * b)

topla(5, 3)
carp(5, 3)

def topla(a, b):
    return a + b

def carp(a, b):
    return a * b

x = topla(5, 3)
y = carp(x, 2)

print(y)

def topla(a, b):
    return a + b

def carp(a, b):
    return a * b

x = carp(2, 3)
y = topla(x, 4)
z = carp(y, x)

print(z)