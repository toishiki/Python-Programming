from utility import *


def courseStatistic1(students, registrations, courses, keyword1, keyword2):
    cid1=getCourseId(courses, keyword1)
    cid2=getCourseId(courses, keyword2)
    print("CourseId       StudentId      StudentName              Gender         FromWhichState")
    print("=======================================================================================")
    sid1=[]
    sid2=[]
    count=0
    for j in registrations:
        if j[1]==cid1:
            sid1.append(j[0])
        elif j[1]==cid2:
            sid2.append(j[0])
    for i in range(len(sid1)):
        for k in range(len(sid2)):
            if sid1[i]==sid2[k]:
                count+=1
                for q in range((len(students))):
                    if sid1[i]==students[q][0]:
                        print((cid1+'+'+cid2).ljust(20)+sid1[i].ljust(20)+students[q][1].ljust(20)+students[q][2].ljust(20)+students[q][3].ljust(20))
    print("The total number of students taking both CS177 and CS180 is", count)
    return count
           

def courseStatistic2(students, registrations, courses, keyword):
    cid=getCourseId(courses,keyword)
    print("CourseId       StudentId      StudentName              Gender         FromWhichState")
    print("=======================================================================================")
    count=0
    j=0
    for j in range(-1,len(registrations)-1):
        if registrations[j][1]==cid and registrations[j][0]!=registrations[j+1][0] and registrations[j][0]!=registrations[j-1][0]:
                   count+=1
                   for q in range(len(students)):
                                  if registrations[j][0]==students[q][0]:
                                      print(cid.ljust(20)+registrations[j][0].ljust(20)+students[q][1].ljust(20)+students[q][2].ljust(20)+students[q][3].ljust(20))
    print("The total number of students taking only",cid,"is",count)
    return count
                   
