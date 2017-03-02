class employee:
    raise_amount=1.04   #class varialbe 
    def __init__(self,name,id,pay):
        self.name=name
        self.id=id       #instance variable
        self.pay=pay
    
    def disp(self):
        print('{} {} {}'.format(self.name,self.pay,self.id))  
    
    def applyraise(self):
        self.pay=int(employee.raise_amount*self.pay)
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount


    @classmethod
    def from_string(cls,str):
        name,id,pay=str.split('-')
        return cls(name,id,pay)
        
    @staticmethod
    def workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return false
        else
            return true
            

    
import date    
mydate=datetime.date(2016,7,11)    
print(workday()) 
e=employee.from_string('rahul-2890-40000')    
e.disp()
"""e1=employee('abhishek',1002,60000)
employee.set_raise_amt(1.08)
e1.applyraise()
e1.disp()
employee.disp(e1)
#print(e1.__dict__)
#print(employee.__dict__)"""