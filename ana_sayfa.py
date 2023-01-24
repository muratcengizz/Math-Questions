import os
from temelKavramlar.temelbilgiler import temelBilgilerr
from temelKavramlar.sayıların_sınıflandırılması import sayilarinSiniflandirilmasi
from temelKavramlar.tamsayilardaislemler import tamSayilardaIslemler
from temelKavramlar.sayıların_incelenmesi import sayilarinIncelenmesi
from basamakKavramı.basamakKavrami import basamaKavrami
from bolmeBolunebilme.bolme import bolme
from bolmeBolunebilme.bolunebilme import bolunebilme
from asalSayılar.asalSayılar import asalSayilar
from asalSayılar.asalCarpanBolen import asalCarpanBolen
from faktoriyel.faktoriyel import faktoriyel
from faktoriyel.faktoriyelliIfadelerinCarpanlarıKatlarıVeBolenleri import faktoriyelliIfadeler
from ebob_ekok.ebob_ekok import ebobEkok
from ebob_ekok.ebobEkokProblemleri import ebobEkokProblemleri
from rasyonel_sayilar.kesirlerVeİslemler import kesirlerVeİslemler
from rasyonel_sayilar.ondalıkVeDevirliSayilar import ondalikVeDevirliSayilar
from üslüSayilar.üslüIfadelerinTanımıVeOzellikleri import üslüIfadelerinTanımı
from üslüSayilar.üslüİfadelerdeDörtİslem import usluIfadelerdeDortIslem
from köklüSayilar.kokluIfadelerTanimiVeOzellikleri import kokluIfadelerTanimiVeOzellikleri
from köklüSayilar.kokluIfadelerdeDortIslemVeKokluDenklemler import kokluIfadelerdeDortIslemVeDenklemler
from denklemCozme.denklemcozme import denklemCozme
from basitEsitsizlikler.basitEsitsizliklerTanimi import basitEsitsizliklerTanimi
from basitEsitsizlikler.basitEsitsizliklerIslemlerVeSıralama import basitEsitsizliklerIslemlerVeSıralama
from mutlakDeger.mutlakDegertanimi import mutlakDegerTanimiVeOzellikleri
from mutlakDeger.dortIslemVeMutlakDegerliDenklemler import dortIslemVeMutlakDegerliDenklemler
from mutlakDeger.mutlakDegerliEsitsizlikler import mutlakDegerliEsitsizlikler
from carpanlaraAyirma.carpanlaraAyirmaYöntemleri import carpanlaraAyirmaYöntemleri
from carpanlaraAyirma.ikinciDerecedenOzdeslikler import ikinciDerecedenOzdeslikler
from carpanlaraAyirma.ucuncuDerecedenVeDahaBuyukKuvvetliDenklemler import ucuncuDerecedenVeDahaBüyükKuvvetliDenklemler
from oranOranti.oranOrantiTurleriVeOrtalamalar import oranOrantiTurleriVeOrtalamalar
from oranOranti.oranOrantıVeOrtalamaProblemleri import oranOrantiVeOrtalamaProblemleri
from problemler.sayiProblemleri import sayiProblemleri
from kumeler.kumelerTanimiVeOzellikleri import kumelerTanimiVeOzellikleri
from kumeler.kumeProblemleri import kumeProblemleri
from fonksiyonlar.fonksiyonlar import fonksiyonlar
from modülerAritmetik.modulerAritmetikTanimi import modulerAritmetikTanimi
from permutasyonKombinasyon.permutasyon import permutasyon
from permutasyonKombinasyon.kombinasyon import kombinasyon
from permutasyonKombinasyon.permutasyonKombinasyonKarsilastirma import permutasyonKombinasyon
from olasilik.olasilikTanimi import olasilikTanimi
class anaSayfa():
    def __init__(self):
        pass
    def anaSayfa(self):
        os.system('cls')
        print("----------------------------ANA SAYFA----------------------------")
        
        print("| 1) Temel Kavramlar            |")
        print("|-------------------------------|")
        print("| 2) Basamak Kavramı            |")
        print("|-------------------------------|")
        print("| 3) Bölme ve Bölünebilme       |")
        print("|-------------------------------|")
        print("| 4) Asal Sayılar               |")
        print("|-------------------------------|")
        print("| 5) Faktoriyel                 |")
        print("|-------------------------------|")
        print("| 6) EBOB-EKOK                  |")
        print("|-------------------------------|")
        print("| 7) Rasyonel Sayılar           |")
        print("|-------------------------------|")
        print("| 8) Üslü İfadeler              |")
        print("|-------------------------------|")
        print("| 9) Köklü İfadeler             |")
        print("|-------------------------------|")
        print("| 10) Denklem Çözme             |")
        print("|-------------------------------|")
        print("| 11) Basit Eşitsizlikler       |")
        print("|-------------------------------|")
        print("| 12) Mutlak Değer              |")
        print("|-------------------------------|")
        print("| 13) Çarpanlara ayırma         |")
        print("|-------------------------------|")
        print("| 14) Oran Orantı               |")
        print("|-------------------------------|")
        print("| 15) Problemler                |")
        print("|-------------------------------|")
        print("| 16) Kümeler                   |")
        print("|-------------------------------|")
        print("| 17) Fonksiyonlar              |")
        print("|-------------------------------|")
        print("| 18) Modüler Aritmetik         |")
        print("|-------------------------------|")
        print("| 19) Permütasyon-Kombinasyon   |")
        print("|-------------------------------|")
        print("| 20) Olasılık                  |")
        print("|-------------------------------|")
        print("| 21) İşlem                     |")
        print("|-------------------------------|")
        print("| 22) Sayısal Mantık            |")
        print("|-------------------------------|")
        print(f"\n\n|Çıkış [q]|\t|Sayfa Seçimi [1-22]|")
        
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if self.user_input == "1":
            os.system('cls')
            self.birinci_sayfa()
        elif self.user_input == "2":
            os.system('cls')
            self.ikinci_sayfa()
        elif self.user_input == "3":
            os.system('cls')
            self.ucuncu_sayfa()
        elif self.user_input == "4":
            os.system('cls')
            self.dorduncu_sayfa()
        elif self.user_input == "5":
            os.system('cls')
            self.besinci_sayfa()
        elif self.user_input == "6":
            os.system('cls')
            self.altinci_sayfa()
        elif self.user_input == "7":
            os.system('cls')
            self.yedinci_sayfa()
        elif self.user_input == "8":
            os.system('cls')
            self.sekizinci_sayfa()
        elif self.user_input == "9":
            os.system('cls')
            self.dokuzuncu_sayfa()
        elif self.user_input == "10":
            os.system('cls')
            self.onuncu_sayfa()
        elif self.user_input == "11":
            os.system('cls')
            self.onbirinci_sayfa()
        elif self.user_input == "12":
            os.system('cls')
            self.onikinci_sayfa()
        elif self.user_input == "13":
            os.system('cls')
            self.onucuncu_sayfa()
        elif self.user_input == "14":
            os.system('cls')
            self.ondorduncu_sayfa()
        elif self.user_input == "15":
            os.system('cls')
            self.onbesinci_sayfa()
        elif self.user_input == "16":
            os.system('cls')
            self.onaltinci_sayfa()
        elif self.user_input == "17":
            os.system('cls')
            self.onyedinci_sayfa()
        elif self.user_input == "18":
            os.system('cls')
            self.onsekizinci_sayfa()
        elif self.user_input == "19":
            os.system('cls')
            self.ondokuzuncu_sayfa()
        elif self.user_input == "20":
            os.system('cls')
            self.yirminci_sayfa()
        elif self.user_input == "21":
            os.system('cls')
            self.yirmibirinci_sayfa()
        elif self.user_input == "22":
            os.system('cls')
            self.yirmiikinci_sayfa()
        
    
    def birinci_sayfa(self):
        os.system('cls')
        print("-------------------------Temel Kavramlar-------------------------")
        print("1) Temel Bilgiler")
        print("2) Sayıların Sınıflandırılması")
        print("3) Tam Sayılarda İşlemler")
        print("4) Sayıların İncelenmesi")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-4]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        elif self.user_input == "1":
            temelBilgilerr.control(self)
        elif self.user_input == "2":
            sayilarinSiniflandirilmasi.control(self)
        elif self.user_input == "3":
            tamSayilardaIslemler.control(self)
        elif self.user_input == "4":
            sayilarinIncelenmesi.control(self)
        else:
            print("Lütfen Tekrar Deneyin!")
        
    
    def ikinci_sayfa(self):
        print("-------------------------Basamak Kavramı-------------------------")
        print("1) Basamak Kavramı")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        if self.user_input == "1":
            basamaKavrami.control(self)
    
    def ucuncu_sayfa(self):
        print("----------------------Bölme ve Bölünebilme-----------------------")
        print("1) Bölme")
        print("2) Bölünebilme")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            bolme.control(self)
        elif self.user_input == "2":
            bolunebilme.control(self)
    
    def dorduncu_sayfa(self):
        print("--------------------------Asal Sayılar---------------------------")
        print("1) Asal Sayılar")
        print("2) Asal Çarpan/Bölen")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            asalSayilar.control(self)
        elif self.user_input == "2":
            asalCarpanBolen.control(self)
        
    def besinci_sayfa(self):
        print("----------------------------Faktoriyel---------------------------")
        print("Faktoriyel")
        print("Faktoriyelli İfadelerin Çarpınları, Katları ve Bölenleri")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            faktoriyel.control(self)
        elif self.user_input == "2":
            faktoriyelliIfadeler.control(self)
    
    def altinci_sayfa(self):
        print("-----------------------------EBOB-EKOK---------------------------")
        print("Ebob-Ekok")
        print("Ebob-Ekok Problemleri")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            ebobEkok.control(self)
        elif self.user_input == "2":
            ebobEkokProblemleri.control(self)
    
    def yedinci_sayfa(self):
        print("------------------------Rasyonel Sayılar-------------------------")
        print("Kesirler ve Kesirler ile İşlemler")
        print("Ondalık ve Devirli Ondalık Sayılar")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            kesirlerVeİslemler.control(self)
        elif self.user_input == "2":
            ondalikVeDevirliSayilar.control(self)
        
    
    def sekizinci_sayfa(self):
        print("--------------------------Üslü İfadeler--------------------------")
        print("Üslü İfadelerin Tanımı Ve Özellikleri")
        print("Üslü İfadelerde Dört İşlem")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            üslüIfadelerinTanımı.control(self)
        elif self.user_input == "2":
            usluIfadelerdeDortIslem.control(self)
    
    def dokuzuncu_sayfa(self):
        print("-------------------------Köklü İfadeler--------------------------")
        print("Köklü İfadelerin Tanım ve Özellikleri")
        print("Köklü İfadelerde Dört İşlem ve Köklü Denklemler")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            kokluIfadelerTanimiVeOzellikleri.control(self)
        elif self.user_input == "2":
            kokluIfadelerdeDortIslemVeDenklemler.control(self)
    
    def onuncu_sayfa(self):
        print("---------------------------Denklem Çözme-------------------------")
        print("Denklem Çözme (Birinci Dereceden Denklemler)")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            denklemCozme.control(self)
            
            
    def onbirinci_sayfa(self):
        print("-----------------------Basit Eşitsizlikler-----------------------")
        print("Basit Eşitsizlikler Tanımı ve Özellikleri")
        print("Basit Eşitsizlikler İşlemler Ve Sıralama")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            basitEsitsizliklerTanimi.control(self)
        elif self.user_input == "2":
            basitEsitsizliklerIslemlerVeSıralama.control(self)
    
    def onikinci_sayfa(self):
        print("---------------------------Mutlak Değer--------------------------")
        print("1) Mutlak Değer Tanımı ve Özellikleri")
        print("2) Dört İşlem ve Mutlak Değerli Denklemler")
        print("3) Mutlak Değerli Eşitsizlikler")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-3]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            mutlakDegerTanimiVeOzellikleri.control(self)
        elif self.user_input == "2":
            dortIslemVeMutlakDegerliDenklemler.control(self)
        elif self.user_input == "3":
            mutlakDegerliEsitsizlikler.control(self)
    
    def onucuncu_sayfa(self):
        print("------------------------Çarpanlara Ayırma------------------------")
        print("1) Çarpanlara Ayırma Yöntemleri")
        print("2) İkinci Dereceden Özdeşlikler")
        print("3) Üçüncü Dereceden ve Daha Büyük Kuvvetli Özdeşlikler")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-3]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            carpanlaraAyirmaYöntemleri.control(self)
        elif self.user_input == "2":
            ikinciDerecedenOzdeslikler.control(self)
        elif self.user_input == "3":
            ucuncuDerecedenVeDahaBüyükKuvvetliDenklemler.control(self)
    
    def ondorduncu_sayfa(self):
        print("----------------------------Oran Orantı--------------------------")
        print("1) Oran Orantı Türleri ve Ortalamalar")
        print("2) Oran Orantı ve Ortalama Problemleri")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-2]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            os.system('cls')
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            oranOrantiTurleriVeOrtalamalar.control(self)
        elif self.user_input == "2":
            oranOrantiVeOrtalamaProblemleri.control(self)
    
    def onbesinci_sayfa(self):
        print("----------------------------Problemler---------------------------")
        print("1) Sayı Problemleri")
        print("2) Kesir Problemleri")
        print("3) Yaş Problemleri")
        print("4) Yüzde Problemleri")
        print("5) Kar Zarar Problemleri")
        print("6) Faiz Problemleri")
        print("7) Karışım Problemleri")
        print("8) İşçi Problemleri")
        print("9) Havuz Problemleri")
        print("10) Hareket Problemleri")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-10]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if self.user_input == "r":
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        elif self.user_input == "1":
            os.system('cls')
            sayiProblemleri.control(self)
            
    def onaltinci_sayfa(self):
        print("-----------------------------Kümeler-----------------------------")
        print("Kümeler Tanımı ve Özellikleri")
        print("Küme Problemleri")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-10]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if self.user_input == "r":
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            kumelerTanimiVeOzellikleri.control(self)
        elif self.user_input == "2":
            kumeProblemleri.control(self)
        
    def onyedinci_sayfa(self):
        print("--------------------------Fonksiyonlar---------------------------")
        print("1) Fonksiyonlar")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-10]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if self.user_input == "r":
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            fonksiyonlar.control(self)
    
    def onsekizinci_sayfa(self):
        print("------------------------Modüler Aritmetik------------------------")
        print("1) Moduler Aritmetik Tanımı ve Özellikleri")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-10]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if self.user_input == "r":
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        if self.user_input == "1":
            modulerAritmetikTanimi.control(self)
            
            
    def ondokuzuncu_sayfa(self):
        print("---------------------Permütasyon-Kombinasyon---------------------")
        print("1) Permütasyon")
        print("2) Kombinasyon")
        print("3) Permütasyon-Kombinasyon Karşılaştırması")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-10]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if self.user_input == "r":
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
            
        if self.user_input == "1":
            permutasyon.control(self)
        elif self.user_input == "2":
            kombinasyon.control(self)
        elif self.user_input == "3":
            permutasyonKombinasyon.control(self)
    
    def yirminci_sayfa(self):
        print("----------------------------Olasılık-----------------------------")
        print("1) Olasılık Tanımı ve Özellikleri")
        print(f"\n\n|Çıkış [q]|\t|Önceki Sayfaya Dön [r]|\t|Sayfa Seçimi [1-10]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if self.user_input == "r":
            self.anaSayfa()
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            olasilikTanimi.control(self)
    
    def yirmibirinci_sayfa(self):
        print("------------------------------İşlem------------------------------")
    
    def yirmiikinci_sayfa(self):
        print("-------------------------Sayısal Mantık--------------------------")

my_instance = anaSayfa()
my_instance.anaSayfa()