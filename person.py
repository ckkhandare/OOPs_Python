class person:
    def __init__(self,id,name):
        self.__id = id
        self.__name=name
        
    def __str__(self):
        return f"Id: {str(self.__id)} \nName:  {self.__name}"
    
    def set_id(self,id):
        self.__id = id
        
    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id