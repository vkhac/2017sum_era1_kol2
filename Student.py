""" Class Student """
class Student:
    def __init__(self,ID,name,surname,classenumber,allscores={},allattendances={},globalaverage=0,globalattendance=100):
        self.ID = ID
        self.name = name
        self.surname = surname
        self.classenumber = classenumber
        self.allscores = allscores
        self.allattendances = allattendances
        self.globalaverage = globalaverage
        self.globalattendance = globalattendance
    
    def getallscores(self):
        for key, value in self.allscores.items():
            print key, ":", value
        
    def __str__(self): #string representation
        return "ID : {3} \nName : {0} \nSurname : {1} \nClasse : {2} \nGlobal average : {4} \nGlobal attendance : {5}% \n".format(self.name, self.surname, self.classenumber, self.ID, self.globalaverage, self.globalattendance)


if __name__ == '__main__':
    eleve = Student(0001,'John','Smith',1,{'Maths':4.5,'Physics':5})
    print eleve
    eleve.getallscores()
        
