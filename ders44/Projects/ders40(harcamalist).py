from datetime import datetime

import json 

try: 
    with open("harcamalar.json", "r") as dosya:
        harcamalar = json.load(dosya)
except FileNotFoundError:
    harcamalar = []

while True:

 print("===== HARCAMA TAKİP =====")
 print("1. Harcamaları Göster")
 print("2. Toplam Harcama")
 print("3. Harcama Ekle")
 print("4. Kategoriye Göre Harcamaları Göster")
 print("5. Çıkış")

 secim = input("Seçiminiz: ").strip()
 if secim == "1":
    if not harcamalar:
        print("Henüz harcama eklenmedi.")
    else:
        for harcama in harcamalar:
            print(f"Harcama Adı: {harcama['ad']}, Tutar: {harcama['tutar']}, Kategori: {harcama['kategori']}, Tarih: {harcama['tarih']}")

 elif secim == "2":
    toplam = 0

    for harcama in harcamalar:
       toplam = toplam + harcama["tutar"]

    print(f"Toplam Harcama: {toplam}")

 elif secim == "4":
    kategori_toplamlari = {}
    print("Kategoriye Göre Harcamalar:")

    for harcama in harcamalar:
         kategori = harcama["kategori"]
         tutar = harcama["tutar"]
   
         if kategori in kategori_toplamlari:
               kategori_toplamlari[kategori] += tutar
         else:
               kategori_toplamlari[kategori] = tutar
         
         for kategori, toplam in kategori_toplamlari.items():
               
               print(f"{kategori}: {toplam}")


    

 elif secim == "3":
     ad = input("Harcama adı: ")
     tutar = float(input("Harcama tutarı: "))
     kategori = input("Harcama kategorisi: ")
     tarih = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

     harcama = {
          "ad": ad,
          "tutar": tutar,
          "kategori": kategori,
          "tarih": tarih
       }
     
     harcamalar.append(harcama)

     with open("harcamalar.json", "w") as dosya:
         json.dump(harcamalar, dosya)

     
 elif secim == "5":
   print("Çıkış yapılıyor...")
   break
 
 