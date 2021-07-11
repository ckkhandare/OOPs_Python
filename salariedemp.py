from employee import employee as e

class salariedemp(e):
    def __init__(self,id,name,department,designation,salary):
        super().__init__(id,name,department,designation)
        self.__salary=salary
        self.__bonus=(20*self.__salary)/100
        
    def __str__(self):
        return f"{super().__str__()} \nsalary:  {self.__salary} \nbonus:  {self.__bonus}"
    
    def set_salary(self,salary):
        self.__salary=salary
        self.__bonus=(20*self.__salary)/100
        
    def get_bonus(self):
        return self.__bonus
    
    def get_salary(self):
        return self.__salary
        
    def calculateSal(self):
        x=self.__salary
        Da=(10*x)/100
        Hra=(15*x)/100
        Pf=(8*x)/100
        Net= x + Da + Hra + Pf
        print(Net)
        
    
