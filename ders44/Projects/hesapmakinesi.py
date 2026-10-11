

while True:

 print("1 - Toplama")
 print("2 - Çıkarma")
 print("3 - Çarpma")
 print ("4 - Bölme")

 secim = input("Seçiminiz: ")

 a = int(input("Birinci sayı:"))
 b = int(input("İkinci sayı:"))

 if secim == "1":

  def topla(a,b):
     return a + b 
  print(topla(a,b))

  break 
 elif secim == "2":
  
  def cıkar(a,b):
    return a - b
  print(cıkar(a,b))

  break
 elif secim == "3": 
  

  def carp(a,b):
    return a * b 
  print(carp(a,b))

  break 
 elif secim == "4": 
  
  def bölme(a,b):
     return a / b 
  print(bölme(a,b))

  break
 elif secim != "1" and secim != "2" and secim != "3" and secim != "4":
    print ("Lütfen geçerli bir sayı giriniz")
    secim = input("Seçiminiz: ")


     