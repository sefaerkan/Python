class Okul():
    def __init__(self,okulAd="Atatürk",sınıf="10",ogretmen="Kevser",ders="İngilizce",calısanAd="Mükremin Abi"):
        self.okulAd= okulAd
        self.sınıf= sınıf
        self.ogretmen= ogretmen
        self.ders= ders
        self.calısanAd= calısanAd

okul1 = Okul("Gap Anadolu Lisesi","11","Ali Hoca","Matematik","Hademe Mehmet Abi")
print(okul1.okulAd)
print(okul1.sınıf)
print(okul1.ogretmen)
print(okul1.ders)
print(okul1.calısanAd)
print("\n")
okul2 = Okul("TOOB Fen Lisesi","9","Kerem Hoca","Türkçe","Güvenlik Uğur Abi")
print(okul2.okulAd)
print(okul2.sınıf)
print(okul2.ogretmen)
print(okul2.ders)
print(okul2.calısanAd)
print("\n")
okul3 = Okul("Cumhuriyet Ortaokulu","6","Ayfer Hoca","Resim","Servisci Ekrem Abi")
print(okul3.okulAd)
print(okul3.sınıf)
print(okul3.ogretmen)
print(okul3.ders)
print(okul3.calısanAd)