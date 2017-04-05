""" Class Diary
Main system"""
from Student import Student
from Classe import Classe
from Exam import Exam

class Diary:
    def __init__(self):
        self.IDnumber = 0
        self.classesoftheschool = []
        
    def createclasse(self,numberofclasse):
        newclasse = Classe(numberofclasse)
        self.classesoftheschool.append(newclasse) 
    
    def createstudent(self,name, surname, classe):
        newstudent = Student(self.IDnumber,name,surname,classe)
        self.classesoftheschool[classe-1].addstudent(newstudent)
        self.IDnumber+=1
        
    def createexam(self,classenumber, subject, scores):
        newexam = Exam(classenumber, subject, scores)
        self.classesoftheschool[classenumber-1].addexam(newexam)
        self.classesoftheschool[classenumber-1].setscores(newexam.subject)
     
        

if __name__ == '__main__':
    journal = Diary()
    journal.createclasse(1)
    journal.createstudent('John','Smith',1)
    journal.createstudent('Emma','Adams',1)
    journal.createstudent('Bob','Marley',1)
    print journal.classesoftheschool[0]
    journal.classesoftheschool[0].getstudents()
    
    journal.classesoftheschool[0].getexams()
    journal.createexam(1,'Maths',{'Smith':3,'Adams':5})
    journal.createexam(1,'Physics',{'Smith':4.5,'Adams':4})
    journal.classesoftheschool[0].getexams()
    journal.classesoftheschool[0].getstudents()
    journal.classesoftheschool[0].listofstudents[0].getallscores()
    journal.classesoftheschool[0].listofstudents[1].getallscores()
    
    
    
