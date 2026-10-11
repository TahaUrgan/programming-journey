class Ogrenci:
    def __init__(self, notu):
        self._notu = notu

    def not_ayarla(self, yeni_not):
        if 0 <= yeni_not <= 100:
            self._notu = yeni_not
            print("Not güncellendi.")
        else:
            print("Not 0 ile 100 arasında olmalı.")

    def not_goster(self):
        return self._notu