import csv # importing the csv module 
fields = ['Name', 'Branch', 'Year', 'CGPA'] # field names 
# data rows of csv file 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 
filename = "x.csv"# name of csv file 
with open(filename, 'w') as csvfile: # writing to csv file
    csvwriter = csv.writer(csvfile) # creating a csv writer object
    csvwriter.writerow(fields) # writing the fields 
    csvwriter.writerows(rows)# writing the data rows
#read CSV
import csv
with open('x.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
