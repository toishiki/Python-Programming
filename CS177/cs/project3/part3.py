from utility import *
def stateStatistic(students, registrations, courses, keyword): 
    cid=getCourseId(courses,keyword)
    print("State               Number")
    print("============================")
    state=[["Illinois",0],
           ["Iowa",0],
           ["Wisconsin",0],
           ["Virginia",0],
           ["Minnesota",0],
           ["Louisiana",0,],
           ["Michigan",0],
           ["Kentucky",0],
           ["Ohio",0],
           ["Indiana",0]]
    for j in registrations:
        if j[1]==cid:
            sid=j[0]
            for i in students:
                if sid==i[0]:
                    for k in range(10):
                        if i[3]==state[k][0]:
                            state[k][1]+=1

    for q in range(10):
        print(state[q][0].ljust(20),state[q][1])
    return state
                     



