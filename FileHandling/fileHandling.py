"""
Part 1
Creating a function load data that reads the office_sales_data.tsv file If the column and
headers (region, rep, and items) match the arguments, add a new entry into the
dictionary with the value from the OrderDate column as the key, and the value from
the Units column as the value. 
"""
def loadData(region,rep,items):
        inputInfo = []
        dictionary = {}
        with open ('office_sales_data.tsv','r') as file:
                for line in file:
                        #Reading the file with which is tab-seperated 
                        inputInfo = line.split('\t') 
                        #If the columns match then in the dictionary for the OrderDate column will be the values from the Units column
                        if (inputInfo [1] == region and inputInfo [2] == rep and inputInfo [3] == items):
                                dictionary[inputInfo[0]]=inputInfo[4]
                #Returning the dictionary
                return dictionary

#Printing the loadData function
print(loadData('Central','Jardine','Pencil'))

"""
Part 2
Outputting the data from the loadData function into a JSON file
"""
print()
import json
#Writing the json file with the loadData function
with open('data.json', 'w') as file:
	json.dump(loadData('Central','Jardine','Pencil'), file)
#Reading the JSON file and displaying the JSON file
with open('data.json', 'r') as file:
	officeInfo = json.load(file)
	print(officeInfo)


    
