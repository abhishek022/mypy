
def file_opening():
    print("enter the path of the file to open")
    path=input("type here")
    fob=open(path,"r+")
    print("the file openend is",fob.name)
    print("Is the file closed ",fob.closed)
    print("In which mode file is opened",fob.mode)
    file_writing(fob)
    file_reading(fob)
    fob.close()
    
def file_writing(fo):
    x=input("enter your text")
    fo.write(x)

def file_reading(fo):
    print("reading")
    read_data=fo.readlines()
    for line in read_data:
        words=line.split(",")
        print(words)

        
        
from simplecrypt import encrypt, decrypt        
def lets_crypt():
    password=input("give your password to crypt")
    plain_text=input("your text")
    ecoded_text  = encrypt(password,plain_text)
    decoded_text = decrypt(password,ecoded_text).decode('utf8')
    print(decoded_text)



file_opening()
lets_crypt()






