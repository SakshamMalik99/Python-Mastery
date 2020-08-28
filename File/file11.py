import os
#write in file
f = open("x.txt","w")
print (f)
for i in  range(1,200):
    f.write("hi "+str(i))
    if i%10==0:
        f.write("\n")
f.close();
#all data
f = open("x.txt","r")
s=f.read(5)
print(s)
f.close();
#single line
f = open("x.txt","r")
s=f.readline()
print(s)
f.close();
#all data line wise
f = open("x.txt","r")
s=f.readlines()
print(s)
f.close();
#all data in list line wise
f = open("x.txt","r")
s=f.readlines()
i=0
print(len(s))
l=len(s)
for i in range(0,l,1):
    print("Line ",i+1," : ",s[i],end="")
f.close();
