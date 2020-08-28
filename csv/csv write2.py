#Write data ad=s dict.
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 
  
import csv
with open('x.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
    writer.writeheader()
    writer.writerows([{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'},
                      {'Grade': 'A', 'first_name': 'Rachael',
                          'last_name': 'Rodriguez'},
                      {'Grade': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
                      {'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
                      {'Grade': 'A', 'first_name': 'Kennzy', 'last_name': 'Tim'}])
print("writing complete")
#wite data from list
import csv 
myData = [["first_name", "second_name", "Grade"],['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']] 
myFile = open('x2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)     
print("Writing complete")
