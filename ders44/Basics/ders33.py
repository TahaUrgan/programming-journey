isimler = ["Taha", "Ahmet", "Taha", "Mehmet", "Ahmet"]
benzersiz = set(isimler)
print(benzersiz)  # Çıktı: {'Taha', 'Ahmet', 'Mehmet'}

sayilar = [1, 2, 2, 3, 4, 4, 4, 5]
sonuc = set(sayilar)
print(sonuc)  # Çıktı: {1, 2, 3, 4, 5}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)  # Çıktı: {3, 4}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Çıktı: {1, 2, 3, 4, 5, 6}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a - b)  # Çıktı: {1, 2}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a ^ b) # Çıktı: {1, 2, 5, 6}

isimler = ["Taha", "Ahmet", "Taha"]

if len(isimler) != len(set(isimler)):
    print("Tekrar var!") 