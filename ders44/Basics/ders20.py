ogrenciler = [
    {"isim": "Taha", "yas": 20},
    {"isim": "Ahmet", "yas": 21},
    {"isim": "Mehmet", "yas": 19}
]

for ogrenci in ogrenciler:
    print(ogrenci["isim"])

    ogrenciler = [
    {"isim": "Taha", "yas": 20},
    {"isim": "Ahmet", "yas": 21},
    {"isim": "Mehmet", "yas": 19}
]

for ogrenci in ogrenciler:
    if ogrenci["yas"] >= 20:
        print(ogrenci["isim"])

        ogrenciler = []

for i in range(3):
    isim = input("Öğrencinin adı: ")
    yas = int(input("Öğrencinin yaşı: "))

    ogrenciler.append({
        "isim": isim,
        "yas": yas
    })
    print(f"Öğrenci: {ogrenci['isim']} - Yaş: {ogrenci['yas']}")