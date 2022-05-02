from utility import *
    
def studentsInPython(students, registrations, courses, keyword):
    cid=getCourseId(courses,keyword)
    print("CourseId            StudentId           StudentName         Gender              FromWhichState ")
    print("====================================================================================================")
    for j in registrations:
        if j[1]==cid:
            sid=j[0]
            for i in students:
                if sid==i[0]:
                    print(cid.ljust(20)+i[0].ljust(20)+i[1].ljust(20)+i[2].ljust(20)+i[3].ljust(20))
                    
  




