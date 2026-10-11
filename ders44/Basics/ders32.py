class BankaHesabi:
    def __init__(self, bakiye):
        self.__bakiye = bakiye

    @property
    def bakiye(self):
        return self.__bakiye

    @bakiye.setter
    def bakiye(self, yeni_bakiye):
        if yeni_bakiye >= 0:
            self.__bakiye = yeni_bakiye
        else:
            print("Bakiye negatif olamaz.")