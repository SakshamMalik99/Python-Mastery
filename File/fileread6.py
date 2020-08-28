file_name="" #d.txt
file_name=input("Enter File Name: ")#d
file_ext=input("File extention : ")#.txt
file=file_name+"."+file_ext;
f1=open(file,"w")
data=input("Enter Info: ")
f1.write(data);
f1.close()
