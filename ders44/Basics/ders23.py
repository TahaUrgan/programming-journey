isimler = {"Taha", "Ahmet", "Taha", "Mehmet", "Ahmet"}
print(isimler)

a = {"Taha", "Ahmet", "Mehmet"}
b = {"Ahmet", "Ali"}

a & b
print(a & b)  # Kesişim
print(a | b)  # Birleşim

isimler = ["Taha", "Ahmet", "Mehmet"]
notlar = [80, 65, 90]

for isim, notu in zip(isimler, notlar):
    print(isim, notu)

topla = lambda a, b: a + b
sonuc = topla(4, 7)
print(sonuc)

carp = lambda a, b: a * b

sonuc = carp(6, 4)
print(sonuc)

sayilar = [1, 2, 3, 4]

sonuclar = []
for sayi in sayilar:
    sonuclar.append(sayi * sayi)
print(sonuclar)


sayilar = [1, 2, 3, 4]

sonuclar = []
sonuclar = list(map(lambda x: x * x, sayilar))
print(sonuclar)

sayilar = [2, 4, 6]

sonuclar = list(map(lambda x: x + 10, sayilar))
print(sonuclar)

sayilar = [2, 5, 8, 11, 14]

sonuclar = list(filter(lambda x: x % 2 == 0, sayilar))
print(sonuclar)

sayilar = [1, 2, 3, 4, 5, 6]

sonuclar = list(
    map(lambda x: x * 10,
        filter(lambda x: x % 2 == 0, sayilar))
)
print(sonuclar)