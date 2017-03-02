def marks(student):
    print(max(student.values()))
    



def find(student):
    print("Enter roll no of student to show his details")
    roll=input(":")
    if roll in student:
        print(student.get(roll))
        

def menu(student):
    choice =0
    while choice!="quit":
        print("Enter your choice")
        print("1. TO SHOW ALL STUDENTS DETAILS")
        print("2. TO FIND A RECORD")
        print("3. TO SHOW HIGHEST MARKS")
        print("4. TYPE quit TO QUIT")
        choice=input(":")
        if choice =="1":
            print(student)
        elif choice =="2":
            find(student)
            break
        elif choice =="3":
            marks(student)
            


#Taking user input to create records
student={}
i=int(input("Enter no of records:"))
for ele in range(i):
    student[input("roll:")]=[input("name:"),input("marks")]
menu(student)

