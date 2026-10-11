dosya = open("notlar.txt", "w")
#print("Dosya oluşturuldu ve yazıldı.")
dosya.write("Ali")
dosya.close()   
#print("Dosya kapatıldı.")

dosya = open("notlar.txt", "a")
#dosyaya sondan ekledi 
dosya.write("Ali")
dosya.close()

dosya = open("notlar.txt", "w")
dosya.write("Taha\n")
dosya.write("Ahmet\n")
dosya.write("Mehmet")
dosya.close()
dosya = open("notlar.txt", "r")
icerik = dosya.read()
dosya.close()   
print(icerik)

dosya = open("notlar.txt", "w")
dosya.write("Taha\n")
dosya.write("Ahmet\n")
dosya.write("Mehmet\n")
dosya.close()
dosya = open("notlar.txt", "r")

icerik = dosya.read()

print(icerik)

dosya.close()

dosya = open("notlar.txt", "r")

for satir in dosya:
    print(satir.strip())

dosya.close()

#satirlar = dosya.readlines()
# satirlar listesini yazdır
#read (string) aksine list olarak çıkartır


with open("notlar.txt", "r") as dosya:
    icerik = dosya.read()
    print(icerik)

bilgi = "Taha,20"
parcalar = bilgi.split(",")
print(parcalar)


with open("test.txt", "w") as dosya:
    dosya.write("Merhaba")