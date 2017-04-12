#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

import json


#These functions are used for average calculation
def get_sum(list):
    result = 0
    for elem in list:
        result+=elem
    return result

def get_average(list):
    if len(list) == 0:
        return 0
    else:
        return float(get_sum(list))/float(len(list))


#These functions manage json import and export    
def import_data(input_file):
    json_data = open(input_file, 'r')
    data = json.load(json_data)
    json_data.close()
    print(input_file + ' imported\n')
    return data

def export_data(output_file, output_data):
    json_file = open(output_file, 'w+')
    json_file.write(json.dumps(output_data, indent=4))
    json_file.close()
    print(output_file + ' exported\n')

           
#This class object is a dictionnary with subjects, students and scores 
class Schoolclass(dict):
    
    def add_subjects(self, *name_subjects):
        for subject in name_subjects:
            if self.has_key(subject):
                print('Subject already exists\n')
            else:
                self[subject]=None
                print('New subject ' + subject + ' has been registered\n')
    
    def add_scores(self, name_subject, scores):
        if not self.has_key(name_subject):
            print('Subject is not registered\n')
        elif type(scores) != dict:
            print('Scores must be a dictionnary\n')
        else:
            self[name_subject] = scores
            print('Scores of ' + name_subject + ' have been registered\n')
    
    def import_scores(self, name_subject, import_file):
        scores = import_data(import_file)
        self.add_scores(name_subject, scores)

    def get_students(self):
        list_students = {}
        for subject in self:
            if self[subject]:
                list_students.update(self[subject])
        return list_students.keys()
    
    def __str__(self):
        result = ''
        for  subject in self:
            result += '     ' + subject + ' :\n'
            for student in self[subject]:
                result += student + ' : ' + str(self[subject][student]) + '\n'
            result += '\n'
        return result

    
#These functions calculate different average for one student             
def get_student_subject_average(schoolclass, student, subject): 
    if not schoolclass.has_key(subject):
        print(schoolclass + ' do not have the subject '+ subject + '\n')
    elif not schoolclass[subject]:
        print('Scores of ' + subject + ' have not been registered\n')
    elif not schoolclass[subject].has_key(student):
        print(student + ' did not attend the subject ' + subject + '\n')
    else:   
        return get_average(schoolclass[subject][student])

def get_student_global_average(schoolclass, student):
    global_scores = []
    for subject in schoolclass:
        temp = get_student_subject_average(schoolclass, student, subject)
        if temp:
            global_scores.append(temp)
    return get_average(global_scores)
   

#These functions export some useful data
def export_schoolclass_average(schoolclass, name_class):
    data = dict.fromkeys([name_class])
    data[name_class] = dict.fromkeys(schoolclass.get_students())
    for key in data[name_class]:
        data[name_class][key] = get_student_global_average(schoolclass, key)
    export_data(name_class + '.json', data)

def export_student_school_report(schoolclass, student):
    data = dict.fromkeys([student], {})
    for subject in schoolclass:
        if schoolclass[subject]:
            try:
                data[student][subject] = schoolclass[subject][student]
            except KeyError:
                data[student][subject] = 'Not attended'
        else:
            data[student][subject] = 'Not registered'
    data[student]['Average'] = get_student_global_average(schoolclass, student)
    export_data(student + '.json', data)

    


if __name__ == '__main__':

    #Creation of the first schoolclass
    class1 = Schoolclass()

    #Creation of the dictionnary of subjects
    class1.add_subjects('Python')
    class1.add_subjects('C', 'VBA', 'Java')
    
    #Registration of scores
    class1.add_scores('Java', {'John': [2, 2, 2], 'Adams': [3, 3.5, 4]})
    class1.add_scores('Python',{'John': [1, 1, 1]})
    class1.add_scores('VBA',{'John': [4], 'Adams': [4.5,4]})
    class1.import_scores('C', 'C.json')
    
    print 'Class1 :'
    print class1
    
    #Calculation of average per subject or global average
    avg1 = get_student_subject_average(class1, 'Adams', 'Python')
    print 'Adams average in Python : ', avg1
    
    avg2 = get_student_subject_average(class1, 'John', 'Java')
    print 'John average in Java : ', avg2
    
    avg3 = get_student_global_average(class1, 'John')
    print 'John global average : ', avg3
    
    avg4 = get_student_global_average(class1, 'Adams')
    print 'Adams global average : ', avg4
    
    #Export of a school report for one student
    export_student_school_report(class1, 'John')
    export_student_school_report(class1, 'Adams')
    
    #Export of the list of students with the average score 
    export_schoolclass_average(class1, 'Semester1')

    #Possibility to manage the whole school by creating new schoolclasses
    class2 = Schoolclass()
	
    #Storage system of schoolclasses to be reused (export/import)
    export_data('class1.json', class1)
    
    class3 = Schoolclass(import_data('class3.json'))
    print 'Class3 :'
    print class3


