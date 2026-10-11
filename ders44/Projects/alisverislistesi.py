liste = []

print("1 - Ürün ekle")
print("2 - Listeyi göster")
print("3 - Çıkış")

while True: 

 secim = input("Seçiminiz: ")
 if secim != "1" and "2" and "3":
   print("Geçersiz seçim yaptınız! ")
 
 if secim == "1":
    while True: 
        ürün = input("İstediğiniz ürünü ekleyiniz: ")
        


        if ürün == "Bitti": 
    
           break
        liste.append(ürün)
        
 elif secim == "2":
   print(liste)

 if secim == "3":
  print ("Çıkış yaptınız.")
  break 
 
 