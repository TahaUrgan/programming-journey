dersler = ["Matematik", "Fizik", "Matematik"] #set yok 
print(dersler)

dersler = {"Matematik", "Fizik", "Matematik"} # set var
print(dersler)

sayilar = {10, 20, 30}

sayilar.add(20)
sayilar.add(40)

print(sayilar)

sayilar = {10, 20, 30}

sayilar.remove(20)

print(sayilar)

sayilar = {10, 20, 30}

sayilar.discard(50)

print(sayilar)

#add()      # ekle
#remove()   # sil, yoksa hata
#discard()  # sil, yoksa sorun yok

matematik = {"Ali", "Taha", "Mehmet"}
fizik = {"Taha", "Mehmet", "Ayşe"}

ortak = matematik & fizik
print(ortak)

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)

A = {1, 2, 3, 4}
B = {3, 4, 5}

print(A - B)
A = {1, 2, 3}
B = {3, 4, 5}

print(A ^ B)


futbol = {"Ali", "Taha", "Mehmet", "Can"}
basketbol = {"Taha", "Can", "Ayşe", "Zeynep"}

ortak_oyuncular = futbol & basketbol

print("Ortak oyuncular:", ortak_oyuncular)