import defs as d
from CustomException import CustomException

while True:
  try:
        
    print('''
    1) Add new Employee\n
    2) Delete employee\n
    3) Modify salary of employee\n
    4) Search employee\n
    5) Calculate Salary of Employee\n
    6) Display All\n
    7) Exit''')
    choice=int(input("enter choice: "))
        
    if choice==1:
      emp_type=int(input('1)Add a salaried employee\n2)Add a contract based worker\nEnter: '))
      if emp_type==1:
        d.add_salariedemp()
      else:
        d.add_contract_emp()
            
    elif choice==2:
      name=input("enter name: ")
      ans=d.delete_emp(name)
      if ans==True:
        print("deleted")
      else:
        print("not found")
                                  
    elif choice==3:
      name=input("enter name: ")
      new_sal=int(input('enter new salary: '))
      d.modify_sal(name, new_sal)
            
    elif choice==4:
      name=input("enter name: ")
      print(d.searchbyname(name))
            
    elif choice==5:
      name=input("enter the name: ")
      d.calculatesal(name)
            
    elif choice==6:
      d.display_all()
            
    elif choice==7:
      break
  except CustomException as e:
    print(e)