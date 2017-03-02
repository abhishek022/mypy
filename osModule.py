import os

curdir=os.getcwd()  #current working dir
print(curdir) 

os.mkdir('newDir')

import time  # import time
time.sleep(2)
os.rename('newDir','newDir2')  #rename
time.sleep(2)

os.rmdir('newDir2')  #delete directry