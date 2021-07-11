from person import person as p

class employee(p):
    def __init__(self,id,name,department,designation):
        super().__init__(id,name)
        self.__department=department
        self.__designation=designation
        
    def __str__(self):
        return f"{super().__str__()} \ndepartment:  {self.__department} \ndesignation:  {self.__designation}"
    
    def set_department(self,department):
        self.__department=department
        
    def set_designation(self,designation):
        self.__designation=designation
                
    def get_department(self):
        return self.__department
    
    def get_designation(self):
        return self.__designation
        
    