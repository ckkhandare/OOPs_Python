from contract import contract as con
from salariedemp import salariedemp as sal
from CustomException import CustomException


lst=[]
def add_contract_emp():
    try:
        cid=int(input("enter id: "))
        name=input("enter name: ")
        department=input("enter department: ")
        designation=input("enter designation: ")
        hours_worked=int(input("enter hours worked: "))
        hourly_rate=int(input("enter hourly rate: "))
        c=con(cid,name,department,designation,hours_worked,hourly_rate)
        lst.append(c)
    except:
        raise CustomException('You have entered invalid details for contract based employee, please try again')
    
def add_salariedemp():
    try:
        sid=int(input("enter id: "))
        name=input("enter name: ")
        department=input("enter department: ")
        designation=input("enter designation: ")
        salary=int(input('enter salary: '))
        s=sal(sid,name,department,designation,salary)
        lst.append(s)
    except:
        raise CustomException('You have entered invalid details for salaried employee, please try again')

def searchbyname(name):
    for f in lst:
        if f.get_name() == name:
            return f
    return None

    
def delete_emp(name):
    f= searchbyname(name)
    if f!=None:
        lst.remove(f)
        return True
    return False
    
def modify_sal(name,new_sal):
    try:
        f= searchbyname(name)
        for f in lst:
            if f.get_name() == name:
                f.set_salary(new_sal)
                print('salary modified')
    except:
        raise CustomException("you entered name of a contract worker not a salaried employee ")
            
    
def calculatesal(name):
    for f in lst:
        if f.get_name() == name:
            f.calculateSal()
    return None

    
    
def display_all():
    for emp in lst:
        print(emp)







