for muz in range(5):
    print("muz")

for muz in range(5):
    print(muz)

for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(3, 8):
    print(i)

for i in range(2, 12, 2): 
    print(i)

number = int(input("Bir sayı gir: ")) 
for i in range(1,number + 1): 
    print(i) 
 

for i in range(5, 0, -1):
    print(i)

    for i in range(3):
     print(i)
    print("Merhaba")

  
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, 6):
    print(i)

    if i == 3:
        break

print("Bitti")

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(1,11):
    if i == 2 or i == 4 or i == 6 or i == 8 or i == 10:
        continue
    print(i)


sayi = int(input("Bir sayı gir: "))
for i in range(sayi, 0, -1):
    print(i)