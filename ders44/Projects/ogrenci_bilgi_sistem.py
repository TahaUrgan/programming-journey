
import json

try:
    with open("ogrenciler.json", "r") as dosya:
        ogrenciler = json.load(dosya)

except FileNotFoundError:
    create_file = input("ogrenciler.json dosyası bulunamadı. Yeni bir dosya oluşturmak ister misiniz? (E/H): ").strip().upper()
    if create_file == "E":
        ogrenciler = []
        with open("ogrenciler.json", "w") as dosya:
            json.dump(ogrenciler, dosya)
        print("Yeni ogrenciler.json dosyası oluşturuldu.")
    else:
        print("Program sonlandırıldı.")
        exit()
        

        
while True:
    print("===== ÖĞRENCİ SİSTEMİ =====")
    print("1 - Öğrenci Ekle")
    print("2 - Öğrenci Göster")
    print("3 - Öğrenci Ara")
    print("4 - Öğrenci Sil")
    print("5 - Çıkış")

    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        from datetime import datetime
        kayit_zamani = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        while True:
            isim = input("Öğrencinin adı: ").strip()

            if isim == "":
                print("İsim boş bırakılamaz.")
            else:
                break

        while True:
            try:
                yas = int(input("Öğrencinin yaşı: "))

                if yas < 0:
                    print("Yaş negatif olamaz.")
                else:
                    break

            except ValueError:
                print("Lütfen geçerli bir sayı girin.")

        ogrenciler.append({
            "isim": isim,
            "yas": yas,
            "kayit_zamani": kayit_zamani
        })

        with open("ogrenciler.json", "w") as dosya:
            json.dump(ogrenciler, dosya)

        

        print(f"Öğrenci eklendi: {isim} - Yaş: {yas} - Kayıt Zamanı: {kayit_zamani}")

    elif secim == "2":
       print("===== ÖĞRENCİLER =====")
       if not ogrenciler:
            print("Kayıtlı öğrenci yok.")
       else:
            for ogrenci in ogrenciler:
                if "kayit_zamani" in ogrenci:
                    print(f"Öğrenci: {ogrenci['isim']} - Yaş: {ogrenci['yas']} - Kayıt Zamanı: {ogrenci['kayit_zamani']}")
                else:
                    print(f"Öğrenci: {ogrenci['isim']} - Yaş: {ogrenci['yas']} - Kayıt Zamanı: Bilinmiyor")

    elif secim == "3":
        aranan = input("Aramak istediğiniz öğrencinin adı: ").strip()
        bulundu = False
        for ogrenci in ogrenciler:
            if ogrenci["isim"] == aranan:
                print(f"Öğrenci bulundu: {ogrenci['isim']} - Yaş: {ogrenci['yas']}")
                bulundu = True
                break
        if not bulundu:
            print(f"Öğrenci bulunamadı: {aranan}")

    elif secim == "4":
        sil = input("Silmek istediğiniz öğrencinin adı: ").strip()
        for i, ogrenci in enumerate(ogrenciler):
            if ogrenci["isim"] == sil:
                del ogrenciler[i]
                print(f"Öğrenci silindi: {sil}")
                break
        else:
            print(f"Öğrenci bulunamadı: {sil}")

    elif secim == "5":
        print("Çıkış yapıldı.")
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")