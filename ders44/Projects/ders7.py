giris_yapti = True

print(not giris_yapti)

yas = int(input("Yaşın: ")) 
sifre_dogru = True 

if yas >= 18 and sifre_dogru: 
    print("Giriş yapabilirsin.")
else: 
    print("Giriş yapamazsın.")

age = int(input("Yaşın: ")) 
password_correct = input("Şifren: ") == "1234"

if age >= 18 and password_correct:
    print("Giriş yapabilirsin.")
else:
    print("Giriş yapamazsın.")

print(not (10 > 5))

age = int(input("Yaşın: "))
city = input("Şehrin: ") 

if age >= 18 or city == "İstanbul": 
    print("Giriş yapabilirsin.")
else:
    print("Giriş yapamazsın.")

