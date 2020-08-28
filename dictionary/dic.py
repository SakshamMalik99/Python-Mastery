#Dictonary
d1={"Name":"Ravindra","Age":"27","Class":"BCA","Subject":"PHP"}
print(type(d1))
print(d1)
print(d1.keys())
print(d1.values())
print(d1["Age"])
#nested Dictonary
d2= {
    "DATA1":{"Name":"Ravindra","Age":"27","Class":"BCA","Subject":"PHP"},
    "DATA2":{"Name":"RAMAN","Age":"17","Class":"BBA","Subject":"Python"}
    }
print(type(d2))
print(d2)
print(d2.keys())
print(d2.values())
print("++++++++++++++++++++++++++++++++++++")
l1=list()
for i in d1.keys():
    l1.append(i)
print(l1)
print("++++++++++++++++++++++++++++++++++++")
l2=list()
for i in d2.keys():
    l2.append(i)
print(l2)
print("++++++++++++++++++++++++++++++++++++")
l3=list()
for i in d1.values():
    l3.append(i)
print(l3)
print("++++++++++++++++++++++++++++++++++++")
l4=list()
for i in d2.values():
    l4.append(i)
print(l4)