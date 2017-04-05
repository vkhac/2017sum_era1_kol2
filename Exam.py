"""class Exam"""

class Exam:
    def __init__(self, classnumber, subject, scores):
        self.classnumber = classnumber
        self.subject = subject
        self.scores = scores
        self.averagescore = Exam.getaverage(scores.values())

    @classmethod
    def getaverage(self,list): #calculate average of a list
        return float(self.getsum(list))/float(len(list))
    
    
    @classmethod
    def getsum(self,list): #calculate sum of a list 
        sum = 0
        for elem in list:
            sum+=elem
        return sum
            

    def __str__(self): #string representation
        return "Exam of {0} of classe number {1} \nAverage score : {2} \n".format(self.subject, self.classnumber, self.averagescore)


if __name__ == '__main__':
    maths = Exam(1,'Maths',{"Smith":5,"Adams":4})
    print maths
    
        
    
    
    
    
