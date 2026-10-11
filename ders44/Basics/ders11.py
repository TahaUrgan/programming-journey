def yemek():
    print("Pizza")

yemek()
yemek()

def hosgeldin(): 
    print("Python Ders 11'e hoş geldin!")
    
 
 
hosgeldin()
hosgeldin()
hosgeldin() 

def yemek():
    print("Pizza")

print("Başla")

yemek()

print("Bitti")

def selam(isim):
    print("Merhaba", isim)

selam("Taha")

def topla(a, b):
    print(a + b)

topla(10, 20)

def yaz(metin):
    print(metin)
    print(metin)

yaz("Python")

def topla(a, b):
    return(a + b)

x = topla(10, 20)

print(x + 5)


c = int(input("İlk sayıyı giriniz: "))
d = int(input("İkinci sayıyı giriniz: "))

def carp(c, d):
    return (c * d)

sonuc = carp(c, d)

print(sonuc)

sayi1 = int(input("İlk sayı: "))
sayi2 = int(input("İkinci sayı: "))

def carp(c, d):
    return c * d

sonuc = carp(sayi1, sayi2)

print(sonuc)

def hesapla(a, b):
    return a + b

x = hesapla(3, 7)

print(x)

print(x * 2)


number1 = int(input("İlk sayıyı giriniz: "))
number2 = int(input("İkinci sayıyı giriniz: "))

def topla(f, g):
    return f + g

answer = topla(number1, number2)

print(answer)