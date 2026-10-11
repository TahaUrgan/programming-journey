def topla(a, b):
    print(a + b)

sonuc = topla(10, 5)

def kare(x):
    return x * x

sayi = kare(4)
print(sayi)


def buyuk_sayi(a, b):
    if a > b:
        return a
    else:
        return b

sonuc = buyuk_sayi(15, 22)
print(sonuc)


def topla(*sayilar):
    toplam = 0

    for sayi in sayilar:
        toplam += sayi

    return toplam
sonuc = topla(2, 4, 6, 8)
print(sonuc)

def bilgiler(**bilgiler):
    print(bilgiler)

bilgiler(isim="Taha", yas=20, sehir="İstanbul")
print(bilgiler)

def bilgiler(**veriler):
    for key, value in veriler.items():
        print(key, ":", value)

bilgiler(isim="Taha", yas=20, bolum="Bilgisayar Mühendisliği")