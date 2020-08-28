people ={1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}
people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people)
print(people[2])
print(people[3])
print(people[4])
print("========================================")
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
                2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
                3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
               4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}
del people[3]['married']
del people[4]['married']
print(people[3])
print("========================================")
print(people[4])
print("========================================")
print(people(key))
print("========================================")
"""people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():    
    print("\nPerson ID:", p_id)
    for key in p_info:
        print(key + ':', p_info[key])
"""
