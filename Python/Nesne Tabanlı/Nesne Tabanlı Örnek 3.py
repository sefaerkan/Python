class kitap():
    kitapSayisi= 0
    def __init__(self,ad,yazar,raf,sayfa,yayinevi):
        self.ad= ad
        self.yazar= yazar
        self.raf= raf
        self.sayfa= sayfa
        self.yayinevi= yayinevi
        kitap.kitapSayisi +=1 #Kitap Sayısı artırıyoruz


    def bilgileriGoster(self):
        return print("Kitabin Adi: {} \nKitabin Yazari: {} \nKitabin Rafi: {} \nKitabin Sayfasi: {} \nKitabin Yayinevi: {} \n".format(self.ad, self.yazar, self.raf, self.sayfa, self.yayinevi))


kitap1 = kitap("Simyacı","Paulo","b23",184,"Can Yayinevi")
kitap2 = kitap("Leon","Sefa","b24",185,"Sefa")

print(kitap.kitapSayisi)


kitap1.bilgileriGoster()
kitap2.bilgileriGoster()
















