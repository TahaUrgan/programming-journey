sifre = input("Şifre: ")

while sifre != "1234":
    print("Yanlış şifre!")
    sifre = input("Tekrar gir: ")

print("Giriş başarılı!")

sayi = int(input("Sayı gir: "))
while sayi != 0:
    print("Girdiğiniz sayı istenilen sayı değil.")
    sayi = int(input("Yeni sayı gir: "))

sayi1 = 3

while sayi1 > 0:
    print(sayi1)
    sayi1 = sayi1 - 1

print("Bitti")

sayi2 = int(input("Sayı gir: "))

while sayi2 > 0:
    print(sayi2)
    sayi2 = sayi2 - 1 

print("Kalkış 🚀")

sayi3 = int(input("Sayı gir: ")) 

while sayi3 < 0:
    print("Negatif sayı olmaz!")
    sayi3 = int(input("Yeni sayı gir: "))
    if sayi3 >= 0:
        print("Teşekkürler.")

sayi = int(input("Bir sayı gir: ")) 
for i in range(sayi):
    print(end= "*") 