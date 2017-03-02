class student:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    
    def __str__(self):
        return 'Student name -{} age -{} marks -{}'.format(self.name,self.age,self.mark)
        
    def __add__(self,other):
        return (self.mark+other.mark)
        
    def __mul__(self,other):
        return (self.age*other.age)
        
    def __eq__(self,other):
        if self.name==other.name and self.age==other.age:
            return True
        else:
            return False
            
            
    
s1=student('abhishek',23,34)
s2=student('abhishek',2,32)
s3=student('saswati',23,92)
s4=student('pourab',23,44)


print(s1)
print(s1+s3)
print(s1*s2)
print(s1==s2)

