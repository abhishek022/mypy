import sys

sys.stderr.write('this is stderr text\n')
sys.stderr.flush()
sys.stdout.write("this is stdout text\n")
print(sys.argv)

if len(sys.argv)>1:
    print(sys.argv[1])