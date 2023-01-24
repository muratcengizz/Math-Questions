import os
import random
import time
import math

class temelBilgilerr():
    def __init__(self):
        pass
    
    def control(self):
        os.system('cls')
        for self.element in range(1, 20+1):
            print(f"Temel Bilgiler - {self.element}. Soru Tipi")
            print("--------------------------------------------")
        print(f"|Çıkış [q]|\t|Sayfa Seçimi [1-{self.element}]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            pass
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        
        
        if self.user_input == "1":
            while True:
                os.system('cls')
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.random_number = random.randint(10,200)
                    self.sayi1 = random.randint(1,200)
                    self.sayi2 = random.randint(1, 200)
                    self.result = self.random_number + self.sayi1 + self.sayi2
                    print("Aşağıdaki işlemin sonucunu bulunuz.")
                    print(f"{self.random_number} + {self.sayi1} + {self.sayi2}")
                    self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                    if self.user_input1 == self.result:
                        print("Tebrikler, Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1 != self.result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.random_number + self.sayi1 + self.sayi2}")
                        time.sleep(2)
                        os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
                            
        
        
        elif self.user_input == "2":
            while True:
                os.system('cls')
                self.user_input = input("Soru üretmek istiyormusunuz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.number1 = random.randint(-200, -10)
                    self.number2 = random.randint(-200, -10)
                    self.number3 = random.randint(-200, -10)
                    self.result = self.number1 + self.number2 + self.number3
                    print("Aşağıdaki işlemin sonucunu bulunuz.")
                    print(f"({self.number1}) + ({self.number2}) + ({self.number3})")
                    self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                    if self.user_input == self.result:
                        print("Tebrikler, Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input != self.result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(2)
                        os.system("cls")
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
                    

        
        elif self.user_input == "3":
            while True:
                os.system('cls')
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.number1 = random.randint(-200, -20)
                    self.number2 = random.randint(20, 200)
                    self.number3 = random.randint(-200, -20)
                    self.result = self.number1 + self.number2 + self.number3
                    print("\nAşağıdaki işlemin sonucunu bulunuz.")
                    print(f"({self.number1}) + {self.number2} + ({self.number3})")
                    self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                    if self.user_input1 == self.result:
                        print("Tebrikler, Doğru Cevap!")
                        time.sleep(2)
                        os.system('cls')
                    elif self.user_input1 != self.result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(2)
                        os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
        
        
        
        elif self.user_input == "4":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.number1 = random.randint(1, 100)
                    self.number2 = random.randint(1, 100)
                    self.result = self.number1 * self.number2
                    print("Aşağıdaki işlemin sonucu bulunuz.")
                    print(f"{self.number1} * {self.number2}")
                    self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                    if self.user_input1 == self.result:
                        print("Tebrikler, Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1 != self.result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(2)
                        os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
        
        
        
        
        elif self.user_input == "5":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    while True:
                        self.number1 = random.randint(1, 800)
                        self.number2 = random.randint(1, 50)
                        self.result = self.number1 / self.number2
                        if self.result == int(self.result):
                            print("Aşağıdaki işlemin sonucunu giriniz.")
                            print(f"{self.number1} / {self.number2}")
                            self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                            if self.user_input1 == self.result:
                                print("Tebrikler, Doğru Cevap!")
                                time.sleep(3)
                                os.system('cls')
                            elif self.user_input1 != self.result:
                                print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                                time.sleep(2)
                                os.system('cls')
                        else:
                            continue
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
        
        
        
        
        elif self.user_input == "6":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.number1 = random.randint(1, 200)
                    self.number2 = random.randint(-200, -20)
                    self.number3 = random.randint(-10, -1)
                    self.result = (self.number1 + self.number2) * self.number3
                    print("Aşağıdaki işlemin cevabını bulunuz.")
                    print(f"[{self.number1} + ({self.number2})] * ({self.number3})")
                    self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                    if self.user_input1 == self.result:
                        print("Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1 != self.result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(2)
                        os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
                    
                    
                    
                    
        elif self.user_input == "7":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    while True:
                        os.system('cls')
                        self.A = random.randint(0, 10)
                        self.B = random.randint(0, 10)
                        self.number1 = random.randint(1, 60)
                        self.number2 = random.randint(-80, -10)
                        self.result = self.A - self.B
                        if self.A * self.number1 == self.A:
                            if self.B * self.number2 == self.number2:
                                print(f"\n{self.A} * {self.number1} = {self.A}\n({self.number2}) * {self.B} = {self.number2}")
                                print(f"Olduğuna göre, A - B kaçtır ?\n")
                                self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                                if self.user_input1 == self.result:
                                    print("Doğru Cevap!")
                                    time.sleep(3)
                                    os.system('cls')
                                elif self.user_input1 != self.result:
                                    print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                                    time.sleep(2)
                                    os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
                    
                    
                    
        elif self.user_input == "8":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.number1 = random.randint(1, 20)
                    self.number2 = random.randint(1, 30)
                    self.number3 = random.randint(1, 20)
                    self.number4 = random.randint(1, 20)
                    self.number5 = random.randint(1,30)
                    self.number6 = random.randint(1, 15)
                    self.result1 = self.number2 * self.number3
                    self.result2 = self.number4 * self.number6
                    self.main_result = self.result1 + self.result2
                    print(f"{self.number1}/{self.number2} kesrinin paydasının {self.number3} katı ile {self.number4}/{self.number5} kesrinin payının {self.number6} katı toplanırsa sonuç kaç olur ?")
                    self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                    if self.user_input1 == self.main_result:
                        print("Tebrikler, Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1 != self.main_result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.main_result}")
                        time.sleep(2)
                        os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
                    
                    
                    
        elif self.user_input == "9":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    while True:
                        self.number1 = random.randint(1, 20)
                        self.number2 = random.randint(1, 15)
                        self.number3 = random.randint(1, 20)
                        self.result = (self.number1 * self.number3) + self.number2
                        if self.number3 > self.number2:
                            print(f"\n   {self.number2}")
                            print(f"{self.number1} ---  kesrini bileşik kesre çevirelim.")
                            print(f"   {self.number3}")
                            self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                            if self.user_input1 == self.result:
                                print("Doğru Cevap!")
                                time.sleep(3)
                                os.system('cls')
                            elif self.user_input1 == self.result:
                                print(f"Yanlış Cevap!\n Sorunun doğru cevabı: {self.result}")
                                time.sleep(2)
                                os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
                    
                    
                    
        elif self.user_input == "10":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    while True:
                        self.number1 = random.randint(1, 70)
                        self.number2 = random.randint(1, 20)
                        self.number3 = random.randint(1, 20)
                        self.number4 = random.randint(1, 50)
                        self.result1 = self.number1 - self.number3
                        self.result2 = self.number1 + self.number2
                        if self.result1 == self.number4:
                            if self.number2 != self.number3:
                                print(f"x + {self.number2}")
                                print(f"-------  kesrinin paydası {self.number4} olduğuna göre, payı kaçtır ?")
                                print(f"x - {self.number3}")
                                self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                                if self.user_input1 == self.result2:
                                    print("Doğru Cevap!")
                                    time.sleep(3)
                                    os.system('cls')
                                elif self.user_input1 != self.result2:
                                    print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result2}")
                                    time.sleep(2)
                                    os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
                    exit()
        
        
        
        elif self.user_input == "11":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    while True:
                        self.number1 = random.randint(1, 30)
                        self.number2 = random.randint(1, 30)
                        self.number3 = random.randint(1, 30)
                        self.number4 = random.randint(1, 30)
                        self.number5 = random.randint(1, 30)
                        self.number6 = random.randint(1, 30)
                        self.number7 = random.randint(1, 30)
                        self.result = (self.number1 - self.number2) * self.number4
                        self.result1 = (self.number1 + self.number3) * self.number5
                        self.result2 = self.result + self.result1
                        self.mainResult = (self.number1 + self.number3) * self.number7
                        if self.result2 == self.number6:
                            print(f"x - {self.number2}")
                            print(f"------   kesrinin payının {self.number4} katı ile paydasının {self.number5} katının toplamı {self.result2}'dir. Buna göre, kesrin paydasının {self.number7} katı kaçtır ?")
                            print(f"x + {self.number3}")
                            self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                            if self.user_input1 == self.mainResult:
                                print("Doğru Cevap!")
                                time.sleep(3)
                                os.system('cls')
                            elif self.user_input1 != self.mainResult:
                                print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.mainResult}")
                                time.sleep(2)
                                os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen Bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control(self)
        
        
        
        elif self.user_input == "12":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    while True:
                        self.my_list = []
                        self.number1 = random.randint(5, 80)
                        self.number2 = random.randint(5, 50)
                        self.number3 = random.randint(5, 50)
                        self.number4 = random.randint(5, 50)
                        self.number5 = random.randint(5, 50)
                        try:
                            self.result1 = self.number1 / self.number2 - self.number3 + self.number4 * self.number5
                            self.result2 = self.number1 / (self.number2 - self.number3) + self.number4 * self.number5
                            self.result3 = self.number1 / (self.number2 - self.number3 + self.number4) * self.number5
                            self.result4 = self.number1 / self.number2 - (self.number3 + self.number4 * self.number5)
                            self.result5 = self.number1 / self.number2 - ((self.number3 + self.number4) * self.number5)
                        except:
                            continue
                        if self.result1 == int(self.result1):
                            if self.result2 == int(self.result2):
                                if self.result3 == int(self.result3):
                                    if self.result4 == int(self.result4):
                                        if self.result5 == int(self.result5):
                                            self.my_list.append(self.result1), self.my_list.append(self.result2), self.my_list.append(self.result3), self.my_list.append(self.result4), self.my_list.append(self.result5)
                                            self.my_list.sort()
                                            print(f"I.   {self.number1}: {self.number2} - {self.number3} + {self.number4} * {self.number5}")
                                            print(f"II.  {self.number1}: ({self.number2 - self.number3}) + {self.number4} * {self.number5}")
                                            print(f"III. {self.number1}: ({self.number2} - {self.number3} + {self.number4}) * {self.number5}")
                                            print(f"IV.  {self.number1}: {self.number2} - ({self.number3} + {self.number4} * {self.number5})")
                                            print(f"V.   {self.number1}: {self.number2} - (({self.number3} + {self.number4}) * {self.number5})")
                                            print("Sayıların toplamlarının küçükten büyüğe sıralanışını bulunuz. ")
                                            self.result_input1 = int(input("Lütfen en küçük 1. sayıyı giriniz: "))
                                            if self.result_input1 == self.my_list[0]:
                                                self.result_input2 = int(input("Lütfen en küçük 2. sayıyı giriniz: "))
                                                if self.result_input2 == self.my_list[1]:
                                                    self.result_input3 = int(input("Lütfen en küçük 3. sayıyı giriniz: "))
                                                    if self.result_input3 == self.my_list[2]:
                                                        self.result_input4 = int(input("Lütfen en küçük 4. sayıyı giriniz: "))
                                                        if self.result_input4 == self.my_list[3]:
                                                            self.result_input5 = int(input("Lütfen en küçük 5. sayıyı giriniz: "))
                                                            if self.result_input5 == self.my_list[4]:
                                                                print("Doğru Cevap!")
                                                                time.sleep(3)
                                                                os.system('cls')
                                                            elif self.result_input5 != self.my_list[4]:
                                                                print(f"Yanlış Cevap!\nEn küçük 5. sayı: {self.my_list[4]}")
                                                                time.sleep(3)
                                                                os.system('cls')
                                                        elif self.result_input4 != self.my_list[3]:
                                                            print(f"Yanlış Cevap!\nEn küçük 4. sayı: {self.my_list[3]}")
                                                            time.sleep(3)
                                                            os.system('cls')
                                                    elif self.result_input3 != self.my_list[2]:
                                                        print(f"Yanlış Cevap!\nEn küçük 3. sayı: {self.my_list[2]}")
                                                        time.sleep(3)
                                                        os.system('cls')
                                                elif self.result_input2 != self.my_list[1]:
                                                    print(f"Yanlış Cevap!\nEn küçük 2. sayı: {self.my_list[1]}")
                                                    time.sleep(3)
                                                    os.system('cls')
                                            elif self.result_input1 != self.my_list[0]:
                                                print(f"Yanlış Cevap!\nEn küçük 1. sayı: {self.my_list[0]}")
                                                time.sleep(3)
                                                os.system('cls')
                elif self.user_input == "n":
                    print("Bir önceki sayfaya yönlendiriliyorsunuz. Lütfen bekleyiniz!")
                    time.sleep(2)
                    temelBilgilerr.control()
                
        elif self.user_input == "13":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    while True:
                        self.number1 = random.randint(1, 10)
                        self.number2 = random.randint(1, 10)
                        self.number3 = random.randint(1, 10)
                        self.number4 = random.randint(1, 15)
                        self.number5 = random.randint(1, 15)
                        self.number6 = random.randint(1, 15)
                        self.ortakCarpan1 = random.randint(1, 10)
                        self.ortakCarpan2 = random.randint(1, 10)
                        self.ortakCarpan3 = random.randint(1, 10)
                        
                        if self.number4 != self.number5 != self.number6:
                            if (self.number4 * self.ortakCarpan1) == (self.number5 * self.ortakCarpan2) == (self.number6 * self.ortakCarpan3):
                                self.result1 = ((self.number1 * self.ortakCarpan1) + (self.number2 * self.ortakCarpan2)) - (self.number3 * self.ortakCarpan3)
                                self.result2 = (self.number4 * self.ortakCarpan1)
                                
                                print(f"  {self.number1}     {self.number2}     {self.number3}")
                                print(f"---- + ---- - ---- işleminin sonucu kaçtır ?")
                                print(f"  {self.number4}     {self.number5}     {self.number6}\n")
                                
                                self.user_input1 = input("Kontrol etmek için lütfen bulduğunuz sonucun payını giriniz: ")
                                if self.result1 == int(self.user_input1):
                                    print("Doğru cevap!")
                                elif self.result1 != int(self.user_input1):
                                    print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result1}")
                                
                                self.user_input2 = input("Kontrol etmek için lütfen bulduğunuz sonucun paydasını giriniz: ")
                                if self.result2 == int(self.user_input2):
                                    print("Doğru Cevap!")
                                elif self.result2 != int(self.user_input2):
                                    print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result2}")
                                    time.sleep(3)
                            else:
                                continue
                        else:
                            continue
                        print("Lütfen Bekleyiniz!")
                        time.sleep(3)
                        os.system('cls')
                        
                elif self.user_input == "n":
                    print("İyi günler!")
                    temelBilgilerr.control(self)
        
        elif self.user_input == "14":
            os.system('cls')
            self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
            if self.user_input == "y":
                while True:
                    self.number1 = random.randint(1, 200)
                    self.number2 = random.randint(50, 1000)
                    self.number3 = random.randint(1, 1000)
                    self.number4 = random.randint(1, 1000)
                    self.number5 = random.randint(1, 500)
                    self.sayac = 0
                    for self.element1 in range(1, 100):
                        if math.pow(self.element1, 2) == self.number1:
                            self.sayac += 1
                        elif math.pow(self.element1, 2) == self.number2:
                            self.sayac += 1
                        elif math.pow(self.element1, 2) == self.number3:
                            self.sayac += 1
                        elif math.pow(self.element1, 2) == self.number4:
                            self.sayac += 1
                        elif math.pow(self.element1, 2) == self.number5:
                            self.sayac += 1
                    if self.sayac >= 0:
                        print(f"{self.number1}, {self.number2}, {self.number3}, {self.number4}, {self.number5}")
                        print(f"Yukarıda verilen sayılardan kaç tanesi tam kare sayıdır ?")
                        self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                        if self.user_input1 == self.sayac:
                            print("Doğru Cevap!")
                        elif self.user_input1 != self.sayac:
                            print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.sayac}")
                    else:
                        continue
                    time.sleep(3)
                    os.system('cls')
                    self.sayac = 0
            elif self.user_input == "n":
                print("İyi günler!")
                temelBilgilerr.control(self)
                        
        
        elif self.user_input == "15":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    while True:
                        self.number1 = random.randint(1, 8)
                        self.number2 = random.randint(-5, 5)
                        self.result = math.pow(self.number1, self.number2)
                        if int(self.result):
                            print(f"{self.number1} sayısının {self.number2} üssü kaçtır ?")
                            
                            print(self.result)
                            
                            self.user_input1 = input("Kontrol etmek için lütfen bulduğunuz sonucu ondalıklı sayı cinsinden giriniz: ")
                            if int(self.user_input1) == self.result:
                                print("Doğru Cevap!")
                                time.sleep(3)
                                os.system('cls')
                            elif int(self.user_input) != self.result:
                                print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                                time.sleep(3)
                                os.system('cls')       
                        else:
                            continue
                elif self.user_input == "n":
                    print("İyi günler!")
                    temelBilgilerr.control(self)
                
        
        elif self.user_input == "16":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    while True:
                        self.number1 = random.randint(-10, 10)
                        self.number2 = random.randint(1, 20)
                        self.number3 = random.randint(1, 10)
                        self.number4 = random.randint(1, 30)
                        self.number5 = random.randint(1, 30)
                        self.result1 = math.pow(self.number1, 2) + self.number2 - math.pow(1/self.number3, -1)
                        self.result2 = self.number4 - self.number5
                        self.result3 = self.result1 / self.result2
                        if self.result3 == int(self.result3):
                            print(f"(({self.number1}) üssü 2), + {self.number2} - ((1/{self.number3}) üssü -1)")
                            print(f"---------------------------------------   işleminin sonucu kaçtır ?")
                            print(f"                {self.number4} - {self.number5}")
                            self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                            if self.user_input1 == self.result3:
                                print("Doğru Cevap!")
                                time.sleep(3)
                                os.system('cls')
                            elif self.user_input1 != self.result3:
                                print(f"Yanlış Cevap\nSorunun doğru cevabı: {self.result3}")
                                time.sleep(3)
                                os.system('cls')
                        else:
                            continue
                elif self.user_input == "n":
                    print("İyi Günler!")
                    temelBilgilerr.control(self)
        
        elif self.user_input == "17":
            print("√   ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁰  ")
            os.system('cls')
            self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
            if self.user_input == "y":
                while True:
                    os.system('cls')
                    self.number1 = random.randint(1, 10)
                    self.number2 = random.randint(1, 10)
                    self.number3 = random.randint(1, 10)
                    self.kok1 = random.randint(1, 10)
                    self.kok2 = random.randint(1, 10)
                    self.kok3 = random.randint(1, 10)
                    self.result = self.kok1 + self.kok2 + self.kok3
                    print(f"{self.kok1}√{self.number1}\n{self.kok2}√{self.number2}\n{self.kok3}√{self.number3}\nSayılarının kök dereceleri toplamı kaçtır ?")
                    self.user_input1 = input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: ")
                    if int(self.user_input1) == self.result:
                        print("Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif int(self.user_input1) != self.result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(3)
                        os.system('cls')
                    
                    
            elif self.user_input == "n":
                print("İyi Günler!")
                temelBilgilerr.control(self)
        
        
        elif self.user_input == "18":
            print("√   ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁰  ")
            os.system('cls')
            self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
            if self.user_input == "y":
                os.system('cls')
                while True:
                    for self.kok1 in range(1, 50):
                        for self.kok2 in range(1, 50):
                            for self.kok3 in range(1, 50):
                                for self.number1 in range(1, 150):
                                    for self.number2 in range(2, 150):
                                        for self.number3 in range(1, 100):
                                            self.result = self.kok1 + self.kok2 + self.kok3
                                            if math.pow(self.kok1, 2) == self.number1:
                                                if math.pow(self.kok2, 3) == self.number2:
                                                    if math.pow(self.kok3, 3) == self.number3:
                                                        print(f"²√{self.number1} + ³√{self.number2} + ³√{self.number3}  işleminin sonucu kaçtır ?")
                                                        self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                                                        if self.user_input1 == self.result:
                                                            print("Doğru Cevap!")
                                                            time.sleep(3)
                                                            os.system('cls')
                                                        elif self.user_input1 != self.result:
                                                            print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                                                            time.sleep(3)
                                                            os.system('cls')            
            elif self.user_input == "n":
                print("İyi Günler!")
                temelBilgilerr.control(self)
        
        elif self.user_input == "19":
            print("√   ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁰  ")
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    for self.number1 in range(40, 100):
                        for self.kok1 in range(1, 50):
                            if math.pow(self.kok1, 2) == self.number1:
                                for self.number2 in range(40, 100):
                                    for self.kok2 in range(1, 50):
                                        if math.pow(self.kok2, 2) == self.number2:
                                            self.result = math.pow(self.kok1, 3) - math.pow(self.kok2, 2)
                                            print(f"a = √{self.number1}\nb = √{self.number2}\nolduğuna göre, a³ - b² toplamı kaçtır ?")
                                            self.user_input1 = int(input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: "))
                                            if self.user_input1 == self.result:
                                                print("Doğru Cevap!")
                                                time.sleep(3)
                                                os.system('cls')
                                            elif self.user_input1 != self.result:
                                                print("Yanlış Cevap!")
                                                time.sleep(3)
                                                os.system('cls')
                elif self.user_input == "n":
                    print("İyi Günler!")
                    temelBilgilerr.control(self)
                
        
        elif self.user_input == "20":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    self.number1 = random.randint(1, 10)
                    self.number2 = random.randint(10, 30)
                    self.number3 = random.randint(1, 30)
                    self.number4 = random.randint(1, 30)
                    self.number5 = random.randint(1, 30)
                    print(f"Bir sayının {self.number1} eksiğinin çeyreğinin {self.number2} fazlası ifadesinin x değişkeni ile cebirsel gösterimi aşağıdakilerden hangisidir ?")
                    print(f"A) {self.number3}(x - {self.number1}) + {self.number2}")
                    print(f"B) (x/4) + {self.number5}")
                    print(f"C) (x/2) + {self.number2}")
                    print(f"D) (x-{self.number4}/4) - {self.number2}")
                    print(f"E) (x - {self.number1}/4) + {self.number2}")
                    
                    self.user_input1 = input("Kontrol etmek için lütfen bulduğunuz şıkkı giriniz: ")
                    if self.user_input1.casefold() == "a":
                        print("Yanlış Cevap\nSorunun doğru cevabı E şıkkı!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1.casefold() == "b":
                        print("Yanlış Cevap\nSorunun doğru cevabı E şıkkı!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1.casefold() == "c":
                        print("Yanlış Cevap\nSorunun doğru cevabı E şıkkı!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1.casefold() == "d":
                        print("Yanlış Cevap\nSorunun doğru cevabı E şıkkı!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1.casefold() == "e":
                        print("Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    
                elif self.user_input == "n":
                    print("İyi Günler!")
                    temelBilgilerr.control(self)
        
        elif self.user_input == "21":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    self.number1 = random.randint(1, 20)
                    self.number2 = random.randint(1, 20)
                    self.number3 = random.randint(1, 30)
                    self.result = f"{self.number1 + self.number2}xy - {self.number3}"
                    self.user_input1 = input(f"{self.number1}xy + {self.number2}xy - {self.number3}  işleminin sonucu kaçtır ?\nSonuç: ")
                    self.user_input1 = self.user_input1.replace(" ", "")
                    self.result = self.result.replace(" ", "")
                    if self.user_input1 == self.result:
                        print("Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1 != self.result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(3)
                        os.system('cls')
                elif self.user_input == "n":
                    print("İyi Günler!")
                    temelBilgilerr.control(self)
        
        elif self.user_input == "22":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    self.number1 = random.randint(1, 10)
                    self.number2 = random.randint(1, 10)
                    self.number3 = random.randint(1, 10)
                    self.number4 = random.randint(1, 10)
                    self.number5 = random.randint(1, 50)
                    self.result = f"{self.number1 * self.number2}ab + {self.number3 * self.number4}xy - {self.number5}"
                    self.result = self.result.replace(" ", "")
                    
                    self.user_input1 = input(f"{self.number1}.{self.number2}ab + {self.number3}.{self.number4}xy - {self.number5} işleminin sonucu kaçtır ?\nSonuç: ")
                    self.user_input1 = self.user_input1.replace(" ", "")
                    
                    if self.user_input1 == self.result:
                        print("Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1 != self.result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(3)
                        os.system('cls')
                elif self.user_input == "n":
                    print("İyi Günler!")
                    temelBilgilerr.control(self)
        
        
        elif self.user_input == "23":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    self.number1 = random.randint(-10, 10)
                    self.number2 = random.randint(-10, 10)
                    self.number3 = random.randint(-10, 10)
                    self.result = f"{self.number1 * self.number2 * self.number3}abc"
                    self.user_input1 = input(f"{self.number1}a.{self.number2}b.{self.number3}c   işleminin sonucu kaçtır ?\nSonuç: ")
                    self.result = self.result.replace(" ", "")
                    self.user_input1.replace(" ", "")
                    if self.user_input1 == self.result:
                        print("Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.user_input1 != self.result:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(3)
                        os.system('cls')
                elif self.user_input == "n":
                    print("İyi Günler!")
                    temelBilgilerr.control(self)
        
        elif self.user_input == "24":
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    os.system('cls')
                    self.number1 = random.randint(1, 15)
                    self.number2 = random.randint(1, 10)
                    self.result = f"{self.number1}xy - {self.number2}x"
                    self.result = self.result.replace(" ", "")
                    self.user_input1 = input(f"x.({self.number1}y - {self.number2})  işleminin sonucunu bulunuz.\nSonuç: ")
                    self.user_input1 = self.user_input1.replace(" ", "")
                    if self.result == self.user_input:
                        print("Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.result != self.user_input1:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(3)
                        os.system('cls')
                elif self.user_input == "n":
                    print("İyi Günler!")
                    temelBilgilerr.control(self)
        
        elif self.user_input == "25":
            print("√   ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁰  ")
            os.system('cls')
            while True:
                self.user_input = input("Soru üretmek istermisiniz ?\n(y/n): ")
                if self.user_input == "y":
                    self.number1 = random.randint(1, 10)
                    self.number2 = random.randint(1, 10)
                    self.number3 = random.randint(1, 10)
                    self.result = f"{self.number1}x üssü 2 + {self.number3}x - {self.number1 * self.number2}x - {self.number1 * self.number3}"
                    self.result1 = self.result.replace(" ", "")
                    print(f"Uzun kenarı (x - {self.number1}) cm, kısa kenarı ({self.number2}x + {self.number3}) cm olan bir dikdörtgenin alanının x cinsinden en sade hali nedir ?")
                    self.user_input1 = input("Kontrol etmek için lütfen bulduğunuz sonucu giriniz: ")
                    self.user_input2 = self.user_input1.replace(" ", "")
                    
                    if self.result1 == self.user_input2:
                        print("Doğru Cevap!")
                        time.sleep(3)
                        os.system('cls')
                    elif self.result1 != self.user_input2:
                        print(f"Yanlış Cevap!\nSorunun doğru cevabı: {self.result}")
                        time.sleep(3)
                        os.system('cls')
                elif self.user_input == "n":
                    print("İyi Günler!")
                    temelBilgilerr.control(self)
        
        elif self.user_input == "26":
            pass
        
        elif self.user_input == "27":
            pass
        
        elif self.user_input == "28":
            pass
        
        elif self.user_input == "29":
            pass
        
        elif self.user_input == "30":
            pass
        
        elif self.user_input == "31":
            pass
                
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
                
                #fisher, rollercoaster
                #joger fit
