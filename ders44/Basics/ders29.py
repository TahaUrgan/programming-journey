class Ogrenci:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

ogrenci = Ogrenci("Ahmet", 21)

print(ogrenci.isim)

class Ogrenci:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def selamla(self):
        print(f"Merhaba, ben {self.isim}!")

ogrenci = Ogrenci("Taha", 20)

ogrenci.selamla()


class Ogrenci: 

    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def selamla(self):
        print(f"Merhaba, ben {self.isim}!")

ogrenci1 = Ogrenci("Ahmet", 21)
ogrenci2 = Ogrenci("Mehmet", 22)

ogrenci2.selamla()


class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

araba1 = Araba("BMW", "320")
araba2 = Araba("Mercedes", "C200")

print(araba1.marka)
print(araba1.model)

class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgi(self):
        print(f"{self.marka} {self.model}")

araba1 = Araba("BMW", "320")    
araba1.bilgi()


class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def hizlan(self, miktar):
        print(f"{self.marka} {miktar} km/h hızlandı.")

araba1 = Araba("BMW", "320")

araba1.hizlan(20)

#----------------------------------------------------------------------------------------------------------------
#class → şablon
#object → şablondan oluşturulan nesne
#__init__ → nesne oluşturulunca otomatik çalışır
#self → o an üzerinde çalıştığımız nesne
#self.isim gibi → nesnenin kendi bilgileri
#method → class'ın içindeki fonksiyon
#method parametreleri → hizlan(50) gibi dışarıdan bilgi alma


class Araba:
    def __init__(self, marka, hiz):
        self.marka = marka
        self.hiz = hiz

    def hizlan(self, miktar):
        self.hiz += miktar

araba = Araba("BMW", 50)

araba.hizlan(20)

print(araba.hiz)
#--------------------------------------------------------------------------------------------------------
class Araba:
    def __init__(self, marka, hiz):
        self.marka = marka
        self.hiz = hiz

    def hizlan(self, miktar):
        self.hiz += miktar

araba = Araba("BMW", 60)

araba.hizlan(15)
araba.hizlan(25)

print(araba.hiz)