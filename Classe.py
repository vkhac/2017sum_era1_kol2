"""Class Classe 
Contains students in the class"""
from Student import Student
from Exam import Exam

class Classe:
    def __init__(self, numberofclasse):
        self.numberofclasse = numberofclasse
        self.listofstudents = {}
        self.numberofstudents = 0
        self.listofexams = {}
        self.numberofexams = 0
    
    def addstudent(self,newstudent):
        self.listofstudents[newstudent.ID] = newstudent
        self.numberofstudents+=1
    
    def getstudents(self):
        print self
        for key in self.listofstudents:
            print self.listofstudents[key]

    def addexam(self,newexam):
        self.listofexams[newexam.subject] = newexam
        self.numberofexams+=1
    
    def getexams(self):
        print "The classe number {0} has made {1} exams \n".format(self.numberofclasse, self.numberofexams)
        for key in self.listofexams:
            print(self.listofexams[key])
    
    def setscores(self,examsubject):
        scores = self.listofexams.get(examsubject).scores
        print scores
        for key in self.listofstudents.keys():#A REVOIR
            print key
            if scores.has_key(self.listofstudents[key].surname):
                print self.listofstudents[key].surname, scores[self.listofstudents[key].surname]
                self.listofstudents[key].allscores[examsubject] = scores[self.listofstudents[key].surname]
                self.listofstudents[key].allattendances[examsubject] = 100
            else:
                self.listofstudents[key].allscores[examsubject] = 0
                self.listofstudents[key].allattendances[examsubject] = 0
            self.listofstudents[key].globalaverage = Exam.getaverage(self.listofstudents[key].allscores.values())
            self.listofstudents[key].globalattendance = Exam.getaverage(self.listofstudents[key].allattendances.values())
            self.listofstudents[key].getallscores()
                
            
        
    def __str__(self): #string representation
        return "Classe number {0} is composed of {1} students \n".format(self.numberofclasse, self.numberofstudents)
            
 
