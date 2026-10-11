def yazdir(*args):
    print(args)

yazdir("Python", "Java", "C++")

def topla(*args):
    print(args)
topla(5, 10, 20, 30)

def yazdir(*args):
    print("Gelen değerler:", args)

yazdir("elma", "armut", "muz", "çilek")

def yazdir(*args):
    
    for deger in args:
        print(deger)

    print(type(args))    
yazdir("Python", "Java", "C++")



def yazdir(*args):
    for deger in args:
        print(deger)

yazdir(10, 20, 30)

#--------------------------------------------------------------------------------------------------

def bilgi(**kwargs):
    print(type(kwargs))

bilgi(isim="Taha", yas=20)

def bilgi(*args, **kwargs):
    print(args)
    print(kwargs)

bilgi("Python", "C++", isim="Taha", yas=20)

def bilgi(*args, **kwargs):
    print(args)
    print(kwargs)

bilgi(10, 20, ad="Ali", yas=25)

def bilgi(**kwargs):
    print(kwargs["isim"])
    print(kwargs["yas"])

bilgi(isim="Taha", yas=20)

def ogrenci(**kwargs):
    print(kwargs["bolum"])

ogrenci(isim="Ahmet", yas=21, bolum="Bilgisayar")


#--------------------------------------------------------------------------------------------------

def topla(a, b, c):
    return a + b + c

sayilar = (10, 20, 30)

print(topla(*sayilar))  # Çıktı: 60


#--------------------------------------------------------------------------------------------------
sayilar = (10, 20, 30)

topla(sayilar)    # paketi komple gönder
topla(*sayilar)   # paketi aç, içindekileri ayrı ayrı gönder