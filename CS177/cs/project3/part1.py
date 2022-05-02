def femaleStudents(students):
    print("StudentId           StudentName         Gender         FromWhichState")
    print("===========================================================================")
    for i in students:
            if (i[3] == 'Indiana') and (i[2] == 'Female'):
                 print(i[0].ljust(20)+i[1].ljust(20)+i[2].ljust(20)+i[3].ljust(20))


