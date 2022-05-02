def readStudent():
    f = open('student.txt','r')
    lines = f.readlines()
    f.close()
     
    students = []

     
    for i in range(len(lines)):
        list = lines[i].split("|")
        sid = list[0].strip().split("=")[1]
        name = list[1].strip().split("=")[1]
        gender = list[2].strip().split("=")[1]
        state = list[3].strip().split("=")[1]
  
        entry = [sid, name, gender, state]
        
        students.append(entry)
    return students
def readCourse():    
    f = open('course.txt','r')
    lines = f.readlines()
    f.close()
     
    courses = []
  
    for i in range(len(lines)):
        list = lines[i].split("|")
        cid = list[0].strip().split("=")[1]
        name = list[1].strip().split("=")[1]
  
        entry = [cid,name]
  
        courses.append(entry)

    return courses

def readRegistration():
    f = open('registration.txt','r')
    lines = f.readlines()
    f.close()
     
    registrations = []
  
    for i in range(len(lines)):
        list = lines[i].split("|")
        sid = list[0].strip().split("=")[1]
        cid = list[1].strip().split("=")[1]
        grade = list[2].strip().split("=")[1]
  
        entry = [sid, cid, grade]
  
        registrations.append(entry)
        
  
    return registrations
  
def getCourseId(courses, keyword):
    for line in courses:
        for token in line[1].split():
            if (token == keyword or token=='"'+keyword or token==keyword+'"'):
                return(line[0])



                
