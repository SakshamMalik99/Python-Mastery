company={1:"IBM",2:"Microsoft",3:"Apple",4:"Intel"}
del company[4]
i=0
i=i+1
print("Result :",i," : ",company)
company[4]="Intel"
company[5]="Dell"
l=len(company)
i=i+1
print("Result :",i," : ",l)
comp1=company.copy()
i=i+1
print("Result :",i," : ",company)
i=i+1
print("Result :",i," : ","1:",company.get(1))
i=i+1
print("Result :",i," : ",company.setdefault(3,"telnet"))
company.update(comp1)
i=i+1
print("Result :",i," : ",company)
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)
i=i+1
print("Result :",i," : ",vowels)
i=i+1
print("Result :",i," : ",company.keys())
i=i+1
print("Result :",i," : ",company.items())
i=i+1
element = company.pop(3)
print("Result :",i," : ",'The popped element is:', element)
result = company.popitem()
i=i+1
print("Result :",i," : ",'person = ',company)
i=i+1
print("Result :",i," : ",'Return Value = ',result)
i=i+1
print("Result :",i," : ",company.values())
i=i+1
print("Result :",i," : ",all(company))
i=i+1
print("Result :",i," : ",any(company))
i=i+1
print("Result :",i," : ",sorted(company))
people={1:{"name":"Shivam","age":19},2:{"name":"ashish","age":50}}
i=i+1
print("Result :",i," : ",people)
i=i+1
print("Result :",i," : ",people[1]["name"])
i=i+1
print("Result :",i," : ",people[2]["name"])
people[3]={"name":"priya","age":45}
i=i+1
print("Result :",i," : ",people)
del people[2]
i=i+1
print("Result :",i," : ",people)
