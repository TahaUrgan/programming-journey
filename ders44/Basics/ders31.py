class Ogrenci:
    def __init__(self, isim):
        self.__isim = isim  #isim değişkenininin dışarıdan erişilmesini engelledik. (private değişken)

ogrenci = Ogrenci("Taha")

#print(ogrenci.__isim)  # Bu satır hata verecektir çünkü __isim private bir değişkendir ve dışarıdan erişilemez.

#-------------------------------------------------------------------------------------------------------------------------------------------

class Ogrenci:
    def __init__(self, isim):
        self.__isim = isim

    def isim_goster(self):
        print(self.__isim)

ogrenci = Ogrenci("Taha")
ogrenci.isim_goster()


class Ogrencu:
    def __init__(self, isim):
        self.__isim = isim

    def isim_degistir(self, yeni_isim):
        self.__isim = yeni_isim


ogrencu = Ogrencu("Taha")
ogrencu.isim_degistir("Ahmet")

class BankaHesabi:
    def __init__(self, bakiye):
        self.__bakiye = bakiye

    def bakiye_getir(self):
        return self.__bakiye
hesap = BankaHesabi(1000)

print(hesap.bakiye_getir())


class BankaHesabi:
    def __init__(self, bakiye):
        self.__bakiye = bakiye

    # Getter
    def bakiye_getir(self):
        return self.__bakiye

    # Setter
    def bakiye_ayarla(self, yeni_bakiye):
        if yeni_bakiye >= 0:
            self.__bakiye = yeni_bakiye
        else:
            print("Bakiye negatif olamaz.")

        hesap = BankaHesabi(1000)

        print(hesap.bakiye_getir())

        hesap.bakiye_ayarla(2500)

        print(hesap.bakiye_getir())