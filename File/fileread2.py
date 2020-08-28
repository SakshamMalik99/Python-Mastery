f1=open("data1.txt","r")
s=f1.read()
L=len(s)
print(L,", ",s)
c1=0
if s[0].isupper():
    c1=c1+1
for i in range(0,L):
    if s[i].isspace():
        if s[i+1].isupper():
            c1=c1+1
print("U: ",c1)
f1.close()
