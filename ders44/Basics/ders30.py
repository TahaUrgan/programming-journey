class Araba:
    def korna(self):
        print("Düt!")

class ElektrikliAraba(Araba):
    pass

tesla = ElektrikliAraba()

tesla.korna()


class Araba:
    def korna(self):
        print("Düt!")

class ElektrikliAraba(Araba):
    def sarj_et(self):
        print("Şarj oluyor.")

tesla = ElektrikliAraba()
tesla.korna()
tesla.sarj_et()


class Araba:
    def bilgi(self):
        print("Ben bir arabayım.")

class ElektrikliAraba(Araba):
    def bilgi(self):
        print("Ben elektrikli bir arabayım.")

araba = ElektrikliAraba()
araba.bilgi()

class Araba:
    def bilgi(self):
        print("Ben bir arabayım.")

class ElektrikliAraba(Araba):
    def bilgi(self):
        super().bilgi()
        print("Aynı zamanda elektrikliyim.")

araba = ElektrikliAraba()
araba.bilgi()

class Araba:
    def __init__(self, marka):
        self.marka = marka


#---------------------------------------------------------------------------------------------------------
class ElektrikliAraba(Araba):
    def __init__(self, marka, batarya):
        super().__init__(marka)
        self.batarya = batarya

    #Araba sınıfındaki __init__ metodunu çalıştırıyor.

#---------------------------------------------------------------------------------------------------------

class Hayvan:
    def __init__(self, isim):
        self.isim = isim

class Kopek(Hayvan):
    def __init__(self, isim, cins):
        super().__init__(isim)
        self.cins = cins

kopek = Kopek("Karabaş", "Golden")
print(kopek.isim)  # Karabaş
print(kopek.cins)  # Golden


class Hayvan:
    def ses(self):
        print("Hayvan sesi")

class Kedi(Hayvan):
    def ses(self):
        super().ses()
        print("Miyav")

kedi = Kedi()
kedi.ses()