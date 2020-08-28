file_name="" #d.txt
file_name=input("Enter File Name: ")#d
file_ext=input("File extention : ")#.txt
file=file_name+"."+file_ext;
f1=open(file,"r")
data=f1.read()
print(data)
f1.close()
