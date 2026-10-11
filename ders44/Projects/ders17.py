import random

print(random.randint(1, 10))


import random

sayi = random.randint(1, 10)

tahmin = int(input("1 ile 10 arasında bir sayı tahmin et: "))

if tahmin == sayi:
    print("Tebrikler! Doğru tahmin ettiniz.")

else:
    print(f"Üzgünüm, doğru sayı {sayi} idi. Tekrar deneyin.")





print("1 = Kolay (1-10)")
print("2 = Orta (1-50)")
print("3 = Zor (1-100)")

while True:
 try:
 
  zorluk = int(input("Zorluk seviyesini seçin: "))
  
  if zorluk == 1:
    ust_sinir = 10
    break
  elif zorluk == 2:
    ust_sinir = 50
    break
  elif zorluk == 3:
    ust_sinir = 100
    break
  else:
    print("Geçersiz seçim. Lütfen 1, 2 veya 3'ü seçin.")

 except: 
     print("Lütfen geçerli bir sayı girin.")

 import random 

sayi = random.randint(1, ust_sinir)

sayac = 0 

while True: 

   try: 
    tahmin = int(input(f"1 ile {ust_sinir} arasında bir sayı tahmin et: "))
    sayac += 1

    if tahmin == sayi:
        print(f"{sayac} tahminde bildiniz!")
        break
    elif tahmin < sayi:
        print("Daha büyük bir sayı tahmin edin.")
    else:
        print("Daha küçük bir sayı tahmin edin.")
   except:
    print("Lütfen geçerli bir sayı girin.")

try:
    sayi = int(input("Bir sayı gir: "))
    print("Giriş Başarılı!")
except:
    print("Bu bir sayı değil!")

    