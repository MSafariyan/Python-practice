import csv
from statistics import mean
with open('grades.csv') as f: #opening the csv file
    avgClass = list()
    reader = csv.reader(f) #reading file
    for row in reader: #reading each row
        name = row[0] #saving each name
        those_grades = list() #to store grades as int
        for grade in row[1:]: #read scores one by one for every row
            those_grades.append(int(grade)) #conver to int and store in list
        #print(those_grades) #print all scores like an array
        print("The avg of %s is %4.2f" % (name,mean(those_grades))) #print avg of the course's score
        print("Maximom score %s = %4.2f" % (name, max(those_grades))) #print best course's scoure
        print("Minimom score %s = %4.2f" % (name, min(those_grades))) #print lowest course's scoure
        print("_____________________________________")
        avgClass.append(mean(those_grades)) #this is a list of each student's avg
    print("Class average = %4.2f " % (mean(avgClass))) #print avg of class's score
    print("******************************")
    print("Class best score = %4.2f" %(max(avgClass))) #print the score of the class
