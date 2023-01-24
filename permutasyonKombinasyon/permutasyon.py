import os

class permutasyon():
    def __init__(self):
        pass
    
    def control(self):
        os.system('cls')
        for self.element in range(1, 10+1):
            print(f"PERMÜTASYON - {self.element}. soru tipi")
            print("-----------------------------------------")
        print(f"|Çıkış [q]|\t|Sayfa Seçimi [1-{self.element}]|")
        self.user_input = input("Lütfen yapmak istediğiniz işlemi seçin: ")
        if self.user_input == "r":
            pass
        elif self.user_input == "q":
            os.system('cls')
            exit()
        
        if self.user_input == "1":
            self.question1()
        elif self.user_input == "2":
            self.question2()
        elif self.user_input == "3":
            self.question3()
        elif self.user_input == "4":
            self.question4()
        elif self.user_input == "5":
            self.question5()
        elif self.user_input == "6":
            self.question6()
        elif self.user_input == "7":
            self.question7()
        elif self.user_input == "8":
            self.question8()
        elif self.user_input == "9":
            self.question9()
        elif self.user_input == "10":
            self.question10()
        
    
    def question1(self):
        pass
    
    def question2(self):
        pass
    
    def question3(self):
        pass
    
    def question4(self):
        pass
    
    def question5(self):
        pass
    
    def question6(self):
        pass
    
    def question7(self):
        pass
    
    def question8(self):
        pass
    
    def question9(self):
        pass
    
    def question10(self):
        pass