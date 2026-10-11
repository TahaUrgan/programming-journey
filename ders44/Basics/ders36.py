import json

ogrenci = {
    "isim": "Taha",
    "yas": 20
}

json_verisi = json.dumps(ogrenci)

print(json_verisi)  # Çıktı: {"isim": "Taha", "yas": 20}
print(type(json_verisi))  # Çıktı: <class 'str'>
#print(json_verisi["isim"])  # Bu satır hata verecektir çünkü json_verisi artık bir string'dir ve dictionary gibi davranamaz.
#print(json_verisi["yas"])  # Bu satır da hata verecektir.
#print(json_verisi.get("isim"))  # Bu satır da hata verecektir.
#print(json_verisi.get("yas"))  # Bu satır da hata verecektir.

import json # JSON veri işleme için gerekli modül
ogrenci_json = json.loads(json_verisi)  # JSON verisini Python dictionary'ye dönüştür
json.dumps # JSON verisini string formatına dönüştürmek için kullanılır.


import json

veri = '{"isim": "Taha", "yas": 20}'

ogrenci = json.loads(veri)

print(type(ogrenci))
print(ogrenci["isim"])
print(ogrenci["yas"])


json.dump # JSON verisini dosyaya yazmak için kullanılır.

import json

veri = '{"isim": "Ali", "yas": 21}'

ogrenci = json.loads(veri)

print(ogrenci["isim"])

with open("ogrenci.json", "r") as dosya:
    ogrenci = json.load(dosya)

print(ogrenci["isim"])