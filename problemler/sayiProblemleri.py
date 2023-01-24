import os
import random


class sayiProblemleri():
    def __init__(self):
        pass
    
    def control(self):
        for self.element in range(1, 25+1):
            print(f"SAYILARIN SINIFLANDIRILMASI - {self.element}. soru tipi")
            print("---------------------------------------------------------")
        
        print(f"|Çıkış [q]|\t|Sayfa Seçimi [1-{self.element}]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            #anaSayfa.anaSayfa()
            pass
        elif self.user_input == "q":
            os.system('cls')
            exit()
        

        if self.user_input == "1":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.random_number = random.randint(1, 100)
                    for self.element in range(self.random_number):
                        for self.element1 in range(2, self.element):
                            if self.element1 * self.element == (self.random_number - self.element):
                                print(
                                    f"İki farklı sayıdan biri diğerinin {self.element1} katıdır. Sayıların toplamı {self.random_number} olduğuna göre büyük sayı kaçtır ?")
                                self.number1 = self.element
                                self.number2 = self.random_number - self.element
                                if self.number1 > self.number2:
                                    print(
                                        f"Büyük sayı: {self.number1}\nKüçük sayı: {self.number2}\nSorunun cevabı: {self.number1}\n\n")
                                elif self.number2 > self.number1:
                                    print(
                                        f"Büyük sayı: {self.number2}\nKüçük sayı: {self.number1}\nSorunun cevabı: {self.number2}\n\n")
                                else:
                                    continue
                elif self.user_input == "n":
                    print("Good days!")
                    exit()
                    
        elif self.user_input == "2":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.random_number = random.randint(1, 100)
                    for self.element in range(self.random_number):
                        for self.element1 in range(2, self.element):
                            if self.element1 * self.element == (self.random_number - self.element):
                                print(
                                    f"İki farklı sayıdan biri diğerinin {self.element1} katıdır. Sayıların toplamı {self.random_number} olduğuna göre küçük sayı kaçtır ?")
                                self.number1 = self.element
                                self.number2 = self.random_number - self.element
                                if self.number1 < self.number2:
                                    print(
                                        f"Büyük sayı: {self.number2}\nKüçük sayı: {self.number1}\nSorunun cevabı: {self.number1}\n\n")
                                elif self.number2 < self.number1:
                                    print(
                                        f"Büyük sayı: {self.number1}\nKüçük sayı: {self.number2}\nSorunun cevabı: {self.number2}\n\n")
                            else:
                                continue
                elif self.user_input == "n":
                    print("Good days!")
                    exit()
                    
        elif self.user_input == "3":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.random_number = random.randint(1, 100)
                    for self.element in range(2, self.random_number):
                        for self.element1 in range(1, self.element):
                            if (self.element1 * self.element + 5) + ((self.element - 5) * 5) == self.random_number:
                                print(
                                    f"Bir sayının {self.element1} katının 5 fazlası ile aynı sayının 5 eksiğinin 5 katının toplamı {self.random_number} oluyor.Buna göre, bu sayı kaçtır ?")
                                print(f"Sorunun cevabı: {self.element}\n\n")
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
                    
        elif self.user_input == "4":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.random_number = random.randint(3, 20)
                    for self.element in range(2, self.random_number):
                        for self.element1 in range(2, self.random_number):
                            for self.element2 in range(2, self.random_number):
                                for self.element3 in range(2, self.random_number):
                                    for self.element4 in range(2, self.random_number):
                                        for self.element5 in range(2, self.random_number):
                                            if (self.element4 * (self.random_number - self.element5)) + (self.element2 * (self.random_number + self.element3)) == (self.element1 * self.random_number) + self.element:
                                                print(f"Bir sayının {self.element5} eksiğinin {self.element4} katı ile aynı sayının {self.element3} fazlasının {self.element2} katının toplamı, aynı sayının {self.element1} katının {self.element} fazlasına eşittir. Buna göre, bu sayı kaçtır ?")
                                                print(f"Sorunun cevabı: {self.random_number}\n\n")
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
        elif self.user_input == "5":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.random_number = random.randint(1, 50)
                    for self.element in range(1, self.random_number):
                        for self.element1 in range(1, self.random_number):
                            if (self.random_number - self.element1) == (self.random_number / self.element) - 8:
                                print(f"İkinci sayıdan {self.element1} çıkarıldığında, ilk sayı ikinci sayının yarısından {self.element} eksik oluyor. Sayıların birbiri cinsinden yazılışı nedir ?")
                                print(f"İkinci sayı: x\nBirinci sayı: ((x - {self.element1}) / 2) - {self.element}")

                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
                    
        elif self.user_input == "6":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.random_number = random.randint(1, 20)
                    for self.element in range(1, self.random_number * 2):
                        for self.element1 in range(1, self.random_number):
                            for self.element2 in range(1, self.random_number):
                                for self.element3 in range(1, self.random_number):
                                    for self.element4 in range(1, self.random_number):
                                        if self.element4 + self.element3 == self.random_number:
                                            if (self.element4 * self.element2) + (self.element3 - self.element1) == self.element:
                                                print(f"Toplamları {self.random_number} olan iki sayıdan ilkinin {self.element2} katıyla ikincisinin {self.element1} eksiğinin toplamı {self.element} olduğuna göre, büyük sayı kaçtır ?")
                                                if self.element4 > self.element3:
                                                    print(f"Sorunun cevabı {self.element4}\n\n")
                                                elif self.element3 > self.element4:
                                                    print(f"Sorunun cevabı: {self.element3}\n\n")
                                        else:
                                            continue
                elif self.user_input == "n":
                    print("Good days!")
                    exit()
                    
        elif self.user_input == "7":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 30)
                    for self.element in range(-50, self.random_number):
                        for self.element1 in range(1, self.random_number):
                            for self.element2 in range(1, self.random_number):
                                for self.element3 in range(1, self.random_number):
                                    for self.element4 in range(1, self.random_number):
                                        if self.element4 + self.element3 == self.random_number:
                                            if (self.element4 * self.element2) + (((self.element3) * 1/3) + self.element1) == self.element:
                                                print(f"Toplamları {self.random_number} olan iki sayıdan ilkinin {self.element2} katıyla ikincisinin üçte birinin {self.element1} fazlasının toplamı {self.element} olduğuna göre, küçük sayı kaçtır ?")
                                                if self.element4 < self.element3:
                                                    print(f"Sorunun cevabı: {self.element4}")
                                                elif self.element3 < self.element4:
                                                    print(f"Sorunun cevabı: {self.element3}")
                                        else:
                                            continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
        elif self.user_input == "8":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 60)
                    for self.element in range(1, self.random_number-20):
                        for self.element1 in range(1, self.random_number):
                            for self.element2 in range(1, self.random_number):
                                for self.element3 in range(1, self.random_number):
                                    if self.element3 + self.element2 == self.random_number:
                                        if self.element3 > self.element2:
                                            if self.element3 == (self.element2 * self.element1) + self.element:
                                                print(
                                                    f"Toplamları {self.random_number} olan iki sayıdan büyük sayı küçüğüne bölündüğünde, bölüm {self.element1}, kalan {self.element} oluyor. Buna göre, küçük sayı kaçtır ?")
                                                print(
                                                    f"Sorunun cevabı: {self.element2}\n\n")
                                        elif self.element2 > self.element3:
                                            if self.element2 == (self.element3 * self.element1) + self.element:
                                                print(
                                                    f"Toplamları {self.random_number} olan iki sayıdan büyük sayı küçüğüne bölündüğünde, bölüm {self.element1}, kalan {self.element} oluyor. Buna göre, küçük sayı kaçtır ?")
                                                print(
                                                    f"Sorunun cevabı: {self.element3}\n\n")
                                    else:
                                        continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
                    
        elif self.user_input == "9":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 20)
                    for self.element in range(1, self.random_number):
                        for self.element1 in range(1, self.random_number):
                            for self.element2 in range(1, self.random_number):
                                for self.element3 in range(1, self.random_number):
                                    if self.element3 + self.element2 == self.random_number:
                                        if (self.element3 - self.element2) == (self.random_number - self.element1) * self.element:
                                            print(
                                                f"Ali 'nin ceviz sayısının {self.element2} eksiği, Ceyda 'nın ceviz sayısının {self.element} katına eşittir. İkisinin toplamda {self.random_number} cevizi olduğuna göre, Ceyda 'nın kaç cevizi vardır ?")
                                            print(
                                                f"Sorunun cevabı: {self.random_number - self.element2}\n\n")
                                    else:
                                        continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
                    
        elif self.user_input == "10":
            self.sayac = 0
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(50, 300)
                    for self.element in range(2, self.random_number):
                        for self.element1 in range(1, self.random_number):
                            for self.element2 in range(1, self.random_number * 2):
                                for self.element3 in range(1, self.random_number * 2):
                                    if self.random_number == (self.element3 * self.element2):
                                        if (self.random_number - self.element1) == (self.element3 * self.element):
                                            print(
                                                f"Ali 'nin parası Serap 'ın parasının {self.element2} katıdır. Ali, Serap 'a {self.element1} lira borç verdiğinde son durumda Ali 'nin Serap 'tan {self.element} kat fazla parası oluyor. Buna göre, Ali 'nin başlangıçta kaç lirası vardır ?")
                                            print(
                                                f"Sorunun cevabı: {self.random_number}")
                                            self.sayac += 1
                                            if self.sayac == 5:
                                                print(
                                                    f"{self.sayac} tane soru üretildi!")
                                                exit()
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
        elif self.user_input == "11":
            self.sayac = 0
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 30)
                    for self.element in range(1, self.random_number):
                        for self.element1 in range(1, self.random_number):
                            for self.element2 in range(1, self.random_number):
                                for self.element3 in range(1, self.random_number):
                                    for self.element4 in range(1, self.random_number):
                                        for self.element5 in range(1, self.random_number):
                                            if self.random_number == (self.random_number - self.element5) * self.element4:
                                                if ((self.random_number - self.element5) * self.element4) + self.element3 == (self.random_number - self.element2) * self.element1:
                                                    print(
                                                        f"Bir sınıftaki kız öğrencilerin sayısı, erkek öğrencilerin sayısının {self.element5} eksiğinin {self.element4} katıdır.\nSınıfa {self.element3} kız öğrenci gelip sınıftan {self.element2} erkek öğrenci gittiğinde, son durumda kız öğrencilerin sayısı erkek öğrencilerinkinin {self.element1} katı oluyor.\nBuna göre, ilk durumda sınıftaki kız öğrencilerin sayısı kaçtır?")
                                                    print(
                                                        f"Sorunun cevabı: {(self.random_number - self.element5) * self.element4}\n\n")
                                                    self.sayac += 1
                                                    if self.sayac == 5:
                                                        print(
                                                            f"{self.sayac} tane soru üretildi!")
                                                        exit()
                                            else:
                                                continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
        elif self.user_input == "12":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 60)
                    for self.element in range(1, self.random_number):
                        for self.element1 in range(1, self.random_number):
                            for self.element2 in range(1, self.random_number):
                                for self.element3 in range(1, self.random_number):
                                    if self.element3 == self.element2 - self.element1:
                                        self.kadin_toplam = self.element3 + self.element
                                        self.erkek_toplam = self.element2 + self.element
                                        if self.kadin_toplam + self.erkek_toplam == self.random_number:
                                            print(
                                                f"Bir otobüsteki erkek yolcuların sayısı kadın yolcuların sayısının {self.element1} eksiğidir.\nOtobüse {self.element} evli çift bindiğinde, son durumda otobüste toplam {self.random_number} yolcu olduğuna göre, ilk durumdaki erkek yolcu sayısı kaçtır?")
                                            print(
                                                f"Doğru cevap: {self.element3}\n\n")
                                    else:
                                        continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
        elif self.user_input == "13":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 50)
                    for self.element in range(1, self.random_number-20):
                        self.kadin = self.element
                        self.erkek = self.random_number - self.kadin
                        for self.element1 in range(1, self.random_number-20):
                            self.evli_cift = self.element1
                            self.yeni_kadin = self.kadin + self.evli_cift
                            for self.element2 in range(1, self.random_number-20):
                                self.yeni_erkek = self.erkek + self.evli_cift - self.element2
                                for self.element3 in range(1, self.random_number-20):
                                    if self.yeni_kadin == self.yeni_erkek * self.element3:
                                        print(f"{self.random_number} yolcusu olan bir otobüse {self.evli_cift} evli çift binip {self.element2} erkek iniyor.\nSon durumda kadın yolcuların sayısı, erkek yolcuların {self.element3} katına eşit olduğuna göre, başlangıçta otobüste kaç kadın yolcu vardır ?")
                                        print(
                                            f"Sorunun cevabı: {self.kadin}\n\n")
                                    else:
                                        continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
        
        elif self.user_input == "14":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 50)
                    for self.element in range(1, self.random_number):
                        self.inek = self.element
                        self.tavuk = self.random_number - self.inek
                        for self.element1 in range(1, self.random_number * 3):
                            if self.inek + self.tavuk == self.random_number:
                                if (self.inek * 4) + (self.tavuk * 2) == self.element1:
                                    print(
                                        f"İneklerin ve tavukların olduğ bir çiftlikte toplam {self.random_number} hayvan vardır.\nÇiftlikteki hayvanların ayak sayısı {self.element1} olduğuna göre, çiftlikte kaç tavuk vardır ?")
                                    print(f"Sorunun cevabı: {self.tavuk}")
                            else:
                                continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()


        elif self.user_input == "15":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 150)
                    for self.element in range(1, self.random_number):
                        for self.element1 in range(1, self.random_number):
                            self.iki_yatakli_oda_sayisi = self.element
                            self.uc_yatakli_oda_sayisi = self.iki_yatakli_oda_sayisi * self.element1
                            if (self.iki_yatakli_oda_sayisi * 2) + (self.uc_yatakli_oda_sayisi * 3) == self.random_number:
                                print(
                                    f"Bir otelde iki ve üç yataklı odalar bulunmaktadır.\nÜç yataklı oda sayısı, iki yataklı oda sayısının {self.element1} katı ve odalardaki toplam yatak sayısı {self.random_number} olduğuna göre, bu otelde kaç oda vardır ?")
                                print(
                                    f"Sorunun cevabı: {self.iki_yatakli_oda_sayisi + self.uc_yatakli_oda_sayisi}")
                            else:
                                continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
            
        elif self.user_input == "16":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 100)
                    for self.element in range(1, self.random_number):
                        self.bes_kurus = self.element
                        self.on_kurus = self.random_number - self.bes_kurus
                        for self.element1 in range(1, 1000):
                            if (self.bes_kurus * 5) + (self.on_kurus * 10) == self.element1:
                                print(
                                    f"5 kuruş ve 10 kuruşların olduğu bir bozuk para cüzdanında toplam {self.random_number} tane madeni para vardır.\nCüzdandaki paraların toplamı {self.element1} kuruş olduğuna göre, bu paralardan kaç tanesi 5 kuruştur ?")
                                print(f"Sorunun cevabı: {self.bes_kurus}")
                            else:
                                continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
            

        elif self.user_input == "17":
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 50)
                    for self.element in range(1, self.random_number):
                        self.yeditl_verenler = self.element
                        self.sekiztl_verenler = self.random_number - self.yeditl_verenler
                        for self.element1 in range(1, 1000):
                            if (self.yeditl_verenler * 7) + (self.sekiztl_verenler * 8) == self.element1:
                                print(f"{self.random_number} kişilik bir sınıfta para toplanırken bazı öğrenciler 7'şer lira bazı öğrenciler ise 8'er lira vermiştir. Toplanan para sayıldığında {self.element1} lira olduğu görülmüştür. Buna göre, kaç kişi 7 lira vermiştir ?")
                                print(
                                    f"Sorunun cevabı: {self.yeditl_verenler}")
                            else:
                                continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()

        elif self.user_input == "18":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 50)
                    if self.random_number % 2 == 0 and self.random_number % 3 == 0:
                        for self.element in range(1, self.random_number):
                            self.cikis = self.random_number / 2
                            self.inis = self.random_number / 3
                            if self.cikis == self.inis + self.element:
                                print(
                                    f"Ayşe bir merdivenin basamaklarını ikişer ikişer çıkıp üçer üçer iniyor. Çıkarken attığı adım sayısı, inerken attığından {self.element} fazla ise, merdivenin basamak sayısı kaçtır ?")
                                print(f"Sorunun cevabı: {self.random_number}")
                    else:
                        continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
        elif self.user_input == "19":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 40)
                    for self.element in range(1, self.random_number):
                        for self.element1 in range(1, self.random_number):
                            if self.random_number % self.element == 0:
                                if self.random_number % self.element1 == 0:
                                    self.inis_adim_sayisi = self.random_number / self.element
                                    self.cikis_adim_sayisi = self.random_number / self.element1
                                    for self.element2 in range(1, self.random_number):
                                        for self.element3 in range(1, self.random_number):
                                            if self.inis_adim_sayisi == (self.element3 * self.cikis_adim_sayisi) - self.element2:
                                                print(
                                                    f"Burak, bir merdivenin basamaklarını {self.element1} {self.element1} çıkıp, {self.element} {self.element} iniyor. İnerken attığı adım sayısı, çıkarken attığının {self.element3} katından {self.element2} eksik ise, çıkarken kaç adım atmıştır ?")
                                                print(
                                                    f"Sorunun cevabı: {self.cikis_adim_sayisi }")
                                        else:
                                            continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()

        
        elif self.user_input == "20":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 100)
                    for self.element in range(1, 8):
                        for self.element1 in range(1, 8):
                            if self.random_number % self.element == 0:
                                if self.random_number & self.element1 == 0:
                                    self.ilk_yari = self.random_number / self.element
                                    self.ikinci_yari = self.random_number / self.element1
                                    for self.element2 in range(1, self.random_number):
                                        if self.ilk_yari - self.ikinci_yari == self.element2:
                                            print(
                                                f"Bir miktar paranın yarısı {self.element} kişiye eşit olarak, diğer yarısı {self.element1} kişiye eşit olarak paylaştırılıyor.\nParanın ilk yarısını alan her bir kişi, diğer yarısını alanlardan {self.element2} TL fazla aldığına göre, dağıtılan para kaç TL 'dir ?")
                                            print(
                                                f"Sorunun cevabı: {self.random_number}\n\n")
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()


        elif self.user_input == "21":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 30)
                    for self.element in range(2, self.random_number):
                        for self.element1 in range(2, self.random_number):
                            for self.element2 in range(2, self.random_number):
                                if self.random_number % self.element2 == 0:
                                    if self.random_number % self.element == 0:
                                        if self.element != self.element2:
                                            if (self.random_number / self.element2) - self.element1 == (self.random_number / self.element):
                                                print(
                                                    f"Bir miktar şeker, {self.element2} çocuğa eşit olarak paylaştırılıyor. Her çocuğa {self.element1} şeker eksik verilseydi, bütün şekerler {self.element} çocuğa eşit olarak paylaştırılabilecekti.\nBuna göre, ilk durumda her bir çocuğun aldığı şeker sayısı kaçtır ?")
                                                print(
                                                    f"Sorunun cevabı: {self.random_number / self.element2}")
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
        
        elif self.user_input == "22":
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 50)
                    for self.element in range(1, self.random_number*2):
                        for self.element2 in range(1, self.random_number*2):
                            for self.element3 in range(1, self.random_number*2):
                                for self.element4 in range(1, self.random_number*2):
                                    if (self.random_number * self.element4) + self.element3 == (self.random_number * self.element2) - self.element:
                                        print(f"Bir işyerinde çalışanlar bir iş arkadaşlarına doğum günü hediyesi alacaklardır. Her bir çalışan {self.element4} TL verirse {self.element3} lira eksik, {self.element2} TL verirse {self.element} TL fazla toplanıyor.\nBuna göre;\na) Şirkette toplam kaç çalışan vardır ?\nb) Kaç para toplanmak istenmektedir ?")
                                        print(f"a şıkkının cevabı: {self.random_number}\nb şıkkının cevabı: {(self.random_number * self.element4) + self.element3}")
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
        
        
        
        elif self.user_input == "23":
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 25)
                    for self.element in range(1, 5):
                        for self.element1 in range(1, self.random_number-20):
                            for self.element2 in range(1, self.random_number):
                                for self.element3 in range(1, 5):
                                    if (self.random_number * self.element3) + self.element2 == (self.random_number - self.element1) * self.element:
                                        print(f"Bir sınıftaki öğrenciler sıralara {self.element3}'şerli oturduğunda {self.element2} kişi ayakta kalıyor; {self.element}'erli oturduklarında {self.element1} sıra boşta kalıyor. Buna göre, sınıf mevcudu kaç kişidir ?")
                                        print(f"Sorunun cevabı: {(self.random_number * self.element3) + self.element2}\n\n")
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()

        
        elif self.user_input == "24":
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 13)
                    for self.element in range(1, self.random_number*2):
                        for self.element1 in range(1, self.random_number*2):
                            for self.element2 in range(1, self.random_number*2):
                                if (self.random_number * self.element2) == (self.random_number + self.element1) * self.element:
                                    print(f"Bir tel {self.element2} eşit parçaya bölünüyor. Parçalardan her biri {self.element1} cm uzun olsaydı tel {self.element} eşit parçaya bölünebilecekti.\nBuna göre, telin uzunluğu kaç cm'dir ?")
                                    print(f"Sorunun cevabı: {self.random_number * self.element2}")
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()
                    
                    
        elif self.user_input == "25":
            while True:
                self.user_input = input("Soru üretmek isterminizi?\n(y/n): ")
                if self.user_input == "y":
                    self.random_number = random.randint(1, 10)
                    for self.element in range(1, self.random_number*3):
                        for self.element1 in range(1, self.random_number*3):
                            for self.element2 in range(1, self.random_number*3):
                                for self.element3 in range(16, self.random_number*5):
                                    if (self.random_number * self.element3) + self.element2 == (self.random_number - self.element1) * self.element:
                                        print(f"Bir grup arkadaş birlikte bir restoranta yemek yemeye gidiyorlar.\nÇıkışta gelen hesap için herkes {self.element3}TL öderse {self.element2}TL eksik kalıyor, gruptan {self.element1} kişi hesaba katılmazsa kalanlar {self.element}TL ödüyor.\Buna göre;\na) Grupta kaç kişi vardır ?\nb) Kaç TL hesap gelmiştir ?")
                                        print(f"a şıkkının cevabı: {self.random_number}")
                                        print(f"b şıkkının cevabı: {(self.random_number * self.element3) + self.element2}")
                                    else:
                                        continue
                elif self.user_input == "n":
                    print("Good Days!")
                    exit()