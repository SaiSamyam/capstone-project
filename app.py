'''
5th STD TO BOARD EXAMINATION Student management application program

Authors:
    Vidyadhar Sharma 
    Sai Samyam v
'''

from studentManager import Student,pprint,json
from tabulate import tabulate

print('-'*40,'\n *************EL ALUMNO************* \n','-'*39)

data= {}# The dictionary used 
try:
    with open('StudentDB.json') as file:
        data.update(json.load(file))    
except:
    pass   
        
# the while loop that keeps repeating the functions 
while True:
    # the options are displayed one below the other 
    print(tabulate([(1,'ENTER STUDENT DETAILS',),(2,'DISPLAY ALL THE STUDENT DETAILS',),(3,'SEARCH STUDENT DETAILS',),(4,'DELETE STUDENT DETAILS',),(5,'UPDATE STUDENT DETAILS AFTER REVALUATION',),(6,'SAVE AND EXIT')]))
    print('\n What option number would you like to choose?: ')
    #the user chooses the suitable opyions to perform his functions 
    ch = int(input('\n Your choice: '))

    if ch == 1:
        # the student detail inputs  
        admittee = Student()
        data[admittee.rollno] = {'a.NAME: ':admittee.name,'b.ROLL NUMBER: ':admittee.rollno,'c.MATHEMATICS: ':admittee.math,'d.SCIENCE: ':admittee.science,'e.SOCIAL SCIENCE: ':admittee.socialscience,'f.ENGLISH: ':admittee.english,'g.LANGUAGE: ':admittee.language,'h.TOTAL: ':admittee.total,'i.PERCENTAGE: ':str(admittee.percentage) + '%'}
   
    elif ch == 2:
        #displays the data in form of a dictionary 
        print('\n Details of all the entered students:')
        pprint(data)
 
    elif ch == 3:
        # allows u to pick the student whose data needs to be displayed 
        rn = int(input('Enter Roll number of student for his/her details: '))
        pprint(data[rn])
 
    elif ch == 4:
        # deletes the details of a particular student
        rn = int(input('Enter roll number of student to delete his/her details: '))
        del (data[rn])

    elif ch == 5: 
        # updates the details of the student
        rn = int(input('Enter roll number of student whose revaluation is completed: '))
        del (data[rn])
        admittee = Student()
        data[admittee.rollno] = {'a.NAME: ':admittee.name,'b.ROLL NUMBER: ':admittee.rollno,'c.MATHEMATICS: ':admittee.math,'d.SCIENCE: ':admittee.science,'e.SOCIAL SCIENCE: ':admittee.socialscience,'f.ENGLISH: ':admittee.english,'g.LANGUAGE: ':admittee.language,'h.TOTAL: ':admittee.total,'i.PERCENTAGE: ':str(admittee.percentage) + '%'}
   


    elif ch == 6:
        #saves the data
        with open('StudentDB.json','w') as file:
            json.dump(data, file)
        print('THANK YOU')
        #breaks the loop 
        break
    
    else:           
        print('Try Again')    

