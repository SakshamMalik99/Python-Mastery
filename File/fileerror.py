try:
    f1=open("data1.txt","r")
    s=f1.read()
    print(s)
except IOError:
    print("File Not Found")
#f1.close()
