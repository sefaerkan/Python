import time

class araba():
    galeriAdi = "Tekinler Galeri"
    aracSayisi = 0
    aracID = 2500

    def __init__(self,marka,model,yıl,renk):
        self.marka = marka
        self.model = model
        self.yıl = yıl
        self.renk = renk
        araba.aracSayisi +=1
        araba.aracID += 10
        self.aracID = araba.aracID
        self.index = -1


    def zamanHesapla(fonk):
        def wrapper(*args,**kwargs):
            baslangıc = time.time()
            fonk(*args,*kwargs)
            bitis = time.time()
        print("Bu işlem toplam {} saniye sürdü".format(bitis-baslangıc))
        return wrapper


    def __str__(self):
        return f"Arabanın markası: {self.marka}\nArabanın modeli: {self.model}\nArabanın yılı: {self.yıl}\nArabanın Rengi: {self.renk}"

    def __len__(self):
        return self.yıl

    def __add__(self,other):
        return self.yıl + other.yıl


    def aracSayisiniSoyle():
        return araba.aracSayisi


    def galeriAdiniSoyle():
        return araba.galeriAdi

arac1 = araba("Reno","Megane",2015,"Beyaz")
arac2 = araba("Fiat","Linea",2017,"Kırmızı")

print(arac1)
print("------")
print(arac2)
print("------")

print(araba.aracSayisiniSoyle())
print(araba.galeriAdiniSoyle())
