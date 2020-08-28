#nested_dict = { 'dictA': {'key_1': 'value_1'},'dictB': {'key_2': 'value_2'}}
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people)
#{1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
"""
John
27
Male
"""
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
people[3] = {}
people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'
print(people[3])
#{'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}
people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])
#{'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}
del people[3]['married']
del people[4]['married']
print(people[3])
print(people[4])
#{'name': 'Luna', 'age': '24', 'sex': 'Female'}
#{'name': 'Peter', 'age': '29', 'sex': 'Male'}
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}
del people[3], people[4]
print(people)
#{1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
         2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
#Person ID: 1
for key in p_info:
    print(key + ':', p_info[key])
"""
Person ID: 2
name: Marie
age: 22
sex: Female
"""