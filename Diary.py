""" Class Diary
Main system"""
from Student import Student
from Classe import Classe
from Exam import Exam

class Diary:
    def __init__(self):
        self.firstclasse = Classe() 
    
    def createstudent(self,name, surname, classe):
        newstudent = Student(name,surname,classe)
        classe.addstudent(newstudent)
        
    def createexam(self,present_students, scores):
        newexam = Exam(present_students, scores)
        
        
    def getstudentsinaclass(self, classe):
        pass
        

