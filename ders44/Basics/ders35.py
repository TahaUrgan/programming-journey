#yas = -5

#if yas < 0:
    #raise ValueError("Yaş negatif olamaz.") #Bilerek hata oluşturduk 


def yas_kontrol(yas):
  

  if yas < 0:
        raise ValueError("Yaş negatif olamaz.")

  print("Yaş geçerli.")

yas = int(input("Yaşınızı giriniz: "))
yas_kontrol(yas)

def yas_kontrol(yas):
    if yas < 18:
        raise ValueError("Yaş 18'den küçük olamaz.")

    print("Giriş başarılı.")

try:
    yas_kontrol(15)
except ValueError:
    print("Yaş uygun değil.")


def test():
    print("çalıştı")

try:
    test()
except:
    print("hata")