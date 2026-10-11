yas = 20

def deneme():
    print(yas)

deneme()

yas = 20

def deneme():
    yas = 30
    print(yas)

deneme()

print(yas)

#yas = 20
#def deneme():
    #print(yas)
    #yas = 30

#deneme()
#dışarıdaki yaş değişkeni içerideki yaş değişkeni ile çakışıyor. Bu yüzden hata alıyoruz.


yas = 20

def deneme():
    print(yas)
    yas = 30
   
print(yas)

puan = 50

def degistir():
    puan = 100

degistir()
print(puan)

try:
    sayi = int("25")

except ValueError:
    print("Hata!")

else:
    print("Başarılı!")

try:
    sayi = int(input("Sayı: "))

except ValueError:
    print("Geçersiz sayı.")

finally:
    print("Bu kısım her durumda çalışır.")

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Hata yakalandı.")

finally:
    print("Program devam ediyor.")