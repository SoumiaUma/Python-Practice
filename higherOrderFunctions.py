# Higher order fucntions 

#Variable used to store assignment grades
grades = [45.0, 61.5, 70.0, 31.5, 81.5, 68.25, 73.0, 100.0]

#Scaling grades to find how much they are when worth 15% of total grade
def scaleAssignmentGrade(grade):
    return grade *0.15

scaledGrades =list(map(scaleAssignmentGrade, grades))
#Using lambda notation for function
scaledGrade =list(map(lambda g: g * 0.15, grades))
print('Scaled Grades: ', scaledGrades)
print('Scaled Grades Using Lambda: ', scaledGrade)

from functools import reduce

minimum = reduce(lambda a,b: a if a < b else b , grades)
print('Minimum Grade is ', minimum)


names = ['Salvatore', 'Ralph', 'Sandy', 'Bartholomew','Harkirat']
longNames = list(filter(lambda name: True if len(name) > 7 else False ,names))
print('The long names are: ', longNames)

