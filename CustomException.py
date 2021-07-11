class CustomException(Exception):
    def __init__(self,msg="this is my custom exception, you have given invalid input"):
        self.__msg=msg
    def __str__(self):
        return self.__msg
    
    
    
# def addfg(x,y):
#     try:
#         print(x/y)
#     except:
#         raise CustomException()
    

# try:
#     x=3434
#     y=0
#     addfg(x,y)
# except CustomException as e:
#     print(e)