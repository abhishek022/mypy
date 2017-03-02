class employee:
    raise_amount=1.4
    def __init__(self,name,id,pay):
        self.name=name
        self.id=id
        self.pay=pay
        
    def apply_raise(self):
        self.pay= int(self.raise_amount * self.pay)


class developer(employee):
    raise_amount=1.4
    def __init__(self,name,id,pay,progLang):
        super().__init__(name,id,pay)
        self.progLang=progLang
        
class manager(employee):
    def __init__(self,name,id,pay,employees=None):
        super().__init__(name,id,pay)
        if employee is None:
            self.employees=[]
        else:
            self.employees=employees
            
    def addEmp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
     
    def delEmp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def show(self):
        for emp in self.employees:
            print(emp.name)

        
d1=developer('abhishek',234,60000,'python')
d2=developer('abhi',224,67000,'ruby')          
m1=manager('sue',123,80000,[d1])
m1.addEmp(d2)
m1.show()
m1.delEmp(d1)
m1.show()

print(isinstance(d1,manager))
print(issubclass(manager,employee))    

"""e1=developer('abhishek','234',60000,'python')
e2=developer('RAVI','234',60000,'java')
#print(e1.__dict__)
print(e1.progLang)
print(e2.progLang)
e1.apply_raise()
print(e1.pay)"""