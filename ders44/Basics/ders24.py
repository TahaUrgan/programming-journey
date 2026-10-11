isimler = ["Taha", "Ahmet", "Mehmet"]
yaslar = [20, 21, 19]

for isim, yas in zip(isimler, yaslar):
    print(isim, yas)

sayilar = [2, 4, 4, 6, 8, 8, 10, 11]

benzersiz = set(sayilar)

sonuclar = list(filter(lambda x: x % 2 == 0, benzersiz))
print(sonuclar)

isimler = ["Taha", "Ahmet", "Mehmet"]
puanlar = [80, 60, 90]

sonuclar = list(
    map(lambda x: x + 5, puanlar)
)

for isim, puan in zip(isimler, sonuclar):
    print(isim, puan)