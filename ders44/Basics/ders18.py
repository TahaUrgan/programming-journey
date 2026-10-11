for i in range(2, 7):
    print(i)

for i in range(0, 10, 2):
    print(i)


for i in range(10, 0, -2):
    print(i)


meyveler = ["Elma", "Muz", "Kiraz"]

for meyve in meyveler:
    print(meyve)

sayilar = [10, 20, 30]

for x in sayilar:
    print(x + 5)

    
sayilar = [2, 4, 6]

for x in sayilar:
    print(x * 2)

    sayilar = [3, 8, 11, 14, 20]

for x in sayilar:
    if x > 10:
        print(x)

        sayilar = [3, 8, 11, 14, 20]

for x in sayilar:
    if x > 10:
        print(x * 2)


sayilar = [3, 8, 11, 14, 20]

toplam = 0

for x in sayilar:
    if x > 10:
        toplam += x

print(toplam)

sayilar = [3, 8, 11, 14, 20]

sayac = 0

for x in sayilar:
    if x > 10:
        sayac += 1

print(sayac)

for i in range(1, 6):
    if i == 2:
        continue
    print(i)

sayilar = [5, -2, 8, -7, 10]

for x in sayilar:
    if x < 0:
        continue
    print(x)

sayilar = [1, 2, 3, 4, 5, 6]

for x in sayilar:
    if x % 2 == 0:
        continue
    print(x)