def merhaba():
    print("Selam!")

x = merhaba

x()

def dekorator(fonksiyon):
    def sarmalayan():
        print("Fonksiyon çalışmadan önce")
        fonksiyon()
        print("Fonksiyon çalıştı")

    return sarmalayan

@dekorator
def merhaba():
    print("Selam!")

def logla(fonksiyon):
    def sarmalayan(*args, **kwargs):
        print("Fonksiyon çalıştırılıyor...")
        sonuc = fonksiyon(*args, **kwargs)
        print("Fonksiyon tamamlandı.")
        return sonuc

    return sarmalayan

@logla
def topla(a, b):
    return a + b

sonuc = topla(10, 20)
print(sonuc)