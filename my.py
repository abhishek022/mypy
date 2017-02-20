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

def salt_encrypt():
    import hashlib, binascii
    dk = hashlib.pbkdf2_hmac('sha256', b'my password is too strong to crack', b'salt', 100000)
    print("hashing with salt",binascii.hexlify(dk))
    
def encoding():
    import base64
    user_data=input("Enter your text to encode")
    b = bytes(user_data, 'utf-8')
    code=base64.b64encode(b)
    print(code)
    data=base64.b64decode(code)
    print(data)

    
    
file_opening()
encrypt()
salt_encrypt()
encoding()







