print("Program :5 :")
# *number : number of time List.
list1 = [1, 3, 5]
print(list1*2)

list1 = ['Data Structure', 'C', 'C++', 'Java', 'Unix',
         'DBMS', 'Python', 'SQL', 'IBM', 'Microsoft', 'Apple']
print("Orignal list is ", list1)
for data in list1:
    print(data)

list1 = [1, 3, 5, 7, 17, 9, 19, 7, 113, 7, 121, 7]
print("Orignal list is ", list1)
c = list1.count(7)
print(7, " comes ", c, " times")  # 4

list1 = [1, 3, 5, 7, 17, 9, 19, 7, 113, 7, 121, 7]
print("Orignal list is ", list1)
print("Number of items in list : ", len(list1))  # 12

list1.sort()
print("Orignal list is ", list1)
list1.reverse()
print("list After Reverse:  ", list1)
print(list1)
list1.pop(4)
print("Orignal list is ", list1)
print("The Element is ", list1.pop(0))

pow1 = [2 ** x for x in range(10)]
print(pow1)

pow2 = []
for x in range(10):
    pow2.append(2 ** x)
print(pow2)

print("List: ", end="")
for i in pow2:
    print(i, end=", ")
