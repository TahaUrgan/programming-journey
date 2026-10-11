meyveler = ["Elma", "Muz", "Kiraz", "Çilek"]
print (meyveler)

meyveler = ["Elma", "Muz", "Kiraz", "Çilek"]

print(meyveler[2])

meyveler = ["Elma", "Muz", "Kiraz", "Çilek"]

for meyve in meyveler:
    print(meyve)
    
notlar = [85, 70, 95, 40, 60]
for notes in notlar:
   if notes >= 50:
    print(notes)

notlar = [85, 70, 95, 40, 60]

gecen = 0

for notu in notlar:
    if notu >= 50:
        gecen = gecen + 1

print("Geçen kişi sayısı:", gecen)

meyveler = ["Elma", "Muz"]

meyveler.append("Kiraz")

print(meyveler)

oyunlar = ["Minecraft", "Valorant"]

oyunlar.append("CS2")

print(oyunlar)

oyunlar = ["Minecraft", "Valorant", "CS2"]

oyunlar.remove("Valorant")

print(oyunlar)

oyunlar = ["Minecraft", "Valorant"]

if "Minecraft" in oyunlar:
    print("Var")
else:
    print("Yok")

meyveler = ["Elma", "Muz", "Kiraz", "Çilek"]

print(len(meyveler))

meyveler = ["Elma", "Muz", "Kiraz", "Çilek"]

print(len(meyveler[0]))

print(type(5))

print(type("5"))   

