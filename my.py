
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


#encrypting and decrypting #
def encrypt():
    print(" md5 hashing encryption")
    import hashlib
    m = hashlib.md5()
    m.update(b"Nobody inspects")
    print("the encrypted text is",m.hexdigest()) 



file_opening()
encrypt()






