import pickle
file_name="" #d.txt
file_name=input("Enter File Name: ")#d
file_ext=input("File extention (dat): ")#dat
file=file_name+"."+file_ext;
f1=open(file,"rb")
data=pickle.load(f1)
f1.close()
print(data)
