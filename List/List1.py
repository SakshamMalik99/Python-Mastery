subjects = ['Data Structure', 'C', 'C++', 'Java', 'Unix', 'DBMS', 'Python']
subjects.append('SQL')
i = 0
i = i+1
print("Result :", i, " : ", subjects)
new_list = subjects.copy()
new_list.append('C#')
i = i+1
print("Result :", i, " : ", new_list)
count = subjects.count('C')
i = i+1
print("Result :", i, " : ", "Number of times C occurs: ", count)
subjects2 = ['IBM', 'Microsoft', 'Apple']
subjects.extend(subjects2)
i = i+1
print("Result :", i, " : ", subjects)
index = subjects.index('Apple')
i = i+1
print("Result :", i, " : ", "Apple found at position: ", index)
subjects.insert(11, 'Dell')
i = i+1
print("Result :", i, " : ", subjects)
r_value = subjects.pop(3)
i = i+1
print("Result :", i, " : ", r_value)
subjects.remove('Dell')
i = i+1
print("Result :", i, " : ", subjects)
i = i+1
print("Result :", i, " : ", len(subjects))
subjects.reverse()
i = i+1
print("Result :", i, " : ", subjects)
subjects.sort()
i = i+1
print("Result :", i, " : ", subjects)
