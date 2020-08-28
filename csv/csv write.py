import csv # importing the csv module 
fields = ['Name', 'Branch', 'Year', 'CGPA'] # field names 
# data rows of csv file 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 
filename = "MYCSV.csv"# name of csv file 
with open(filename, 'w') as csvfile: # writing to csv file
    csvwriter = csv.writer(csvfile) # creating a csv writer object
    csvwriter.writerow(fields) # writing the fields 
    csvwriter.writerows(rows)# writing the data rows
#read CSV
import csv
with open('MYCSV.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
#Write data ad=s dict.
import csv
with open('example5.txt', 'w') as csvfile:
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
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)     
print("Writing complete")
