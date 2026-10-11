araba = {
    "marka": "BMW",
    "model": "M3",
    "yil": 2024
}
print(araba["model"])

araba = {
    "marka": "BMW",
    "model": "M3",
    "yil": 2024
}

araba["yil"] = 2025

print(araba["yil"])

kisi = {
    "isim": "Taha",
    "yas": 20
}

kisi["sehir"] = "İstanbul"

print(kisi["sehir"])

kisi = {
    "isim": "Taha",
    "yas": 20,
    "sehir": "İstanbul"
}

del kisi["yas"]
print(kisi)

kisi = {
    "isim": "Taha",
    "yas": 20
}

if "yas" in kisi:
    print("Yaş bilgisi var.")

    kisi = {
    "isim": "Taha",
    "yas": 20
}

if "sehir" in kisi:
    print(kisi["sehir"])
else:
    print("Şehir bilgisi yok.")


kisi = {
    "isim": "Taha",
    "yas": 20,
    "sehir": "İstanbul"
}

for key in kisi:
    print(key)

kisi = {
    "isim": "Taha",
    "yas": 20,
    "sehir": "İstanbul"
} 

for value in kisi.values():
    print(value)

kisi = {
    "isim": "Taha",
    "yas": 20,
    "sehir": "İstanbul"
} 
for key, value in kisi.items():
    print(key, value)

kisi = {}

isim = input("İsminiz: ")
yas = int(input("Yaşınız: "))
bolum = input("Bölümünüz: ")


kisi["isim"] = isim
kisi["yas"] = yas
kisi["bolum"] = bolum

for key, value in kisi.items():
    print(key, ":", value)