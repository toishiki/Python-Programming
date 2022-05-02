from utility import *
from plot import *
from part1 import *
from part2 import *
from part3 import *
from part4 import *

    
def main():
    print("***************************")
    print("*    1. To run part 1     *")
    print("*    2. To run part 2     *")
    print("*    3. To run part 3     *")
    print("*    4. To run part 4     *")
    print("*    5. To exit           *")
    print("***************************")

    ind=eval(input("Please select [1-5] to run different parts："))

    students=readStudent()
    courses=readCourse()
    registrations=readRegistration()
    
    while ind!=5:
        if ind==1:
            femaleStudents(students)
            ind=eval(input("Please select [1-5] to run different parts："))
        elif ind==2:
            keyword="Python" 
            studentsInPython(students, registrations,courses, keyword)
            ind=eval(input("Please select [1-5] to run different parts："))
        elif ind==3:
            keyword="Java"  
            states=stateStatistic(students,registrations,courses,keyword)
            plotBarChart(states)
            ind=eval(input("Please select [1-5] to run different parts："))
        elif ind==4:
            keyword1="Java"
            keyword2="Python"
            count1=courseStatistic1(students, registrations, courses, keyword1, keyword2)
            keyword="Java"
            count2=courseStatistic2(students, registrations, courses, keyword)
            keyword="Python"
            count3=courseStatistic2(students, registrations, courses, keyword)
            counts=[count1,count3,count2]
            plotPieChart(counts)
            ind=eval(input("Please select [1-5] to run different parts："))
        else:
            ind=eval(input("Please select [1-5] to run different parts："))

        
       

main()
