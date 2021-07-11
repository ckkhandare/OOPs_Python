from employee import employee as e

class contract(e):
    def __init__(self,id,name,department,designation,hours_worked,hourly_rate):
        super().__init__(id,name,department,designation)
        self.__hours_worked=hours_worked
        self.__hourly_rate=hourly_rate
        
    def __str__(self):
        return f"{super().__str__()} \nhours_worked:  {self.__hours_worked} \nhourly_rate:  {self.__hourly_rate}"
    
    def set_hourly_rate(self,hourly_rate):
        self.__hourly_rate=hourly_rate
        
    def set_hours_worked(self,hours_worked):
        self.__hours_worked=hours_worked
        
    def get_hourly_rate(self):
        return self.__hourly_rate
        
    def get_hours_worked(self):
        return self.__hours_worked
    
    def calculateSal(self):
        contractEmp= self.__hours_worked * self.__hourly_rate
        print(contractEmp)
    
    
    
    
    
