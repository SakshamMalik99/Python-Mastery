import os
file_name=input("Enter File Name: ")
extension=input("Enter Extension: ")
print(file_name)
print(extension)
FN=file_name+"."+extension
f=open(FN,'w')
f.write("Hi..this is my file.")
f.close()
