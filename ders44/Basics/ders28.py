sayilar = [1, 2, 3, 4, 5]

sonuclar = []

for sayi in sayilar:
    sonuclar.append(sayi * sayi)

print(sonuclar)

#yada --------------------------------------------------------------


sayilar = [1, 2, 3, 4, 5]

sonuclar = []

sonuclar = [sayi * sayi for sayi in sayilar]
print(sonuclar)

ciftler = []

for sayi in sayilar:
    if sayi % 2 == 0:
        ciftler.append(sayi)

print(ciftler)

#yada --------------------------------------------------------------

ciftler = []

ciftler = [sayi for sayi in sayilar if sayi % 2 == 0]

print(ciftler)

sayilar = [1, 2, 3, 4, 5]

sonuclar = [sayi * 2 for sayi in sayilar if sayi > 2]
print(sonuclar)


sayilar = [2, 4, 6]

sonuclar = {sayi: sayi + 1 for sayi in sayilar}
print(sonuclar)