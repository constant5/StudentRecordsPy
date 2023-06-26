# StudentRecords class
from .grade import Grade
from .course import Course
from .student import Student
from typing import List
import io


class StudentRecords():
    def __init__(self, grades:List[Grade]=[], courses:List[Course]=[], students:List[Student]=[]):
        self.grades = grades
        self.courses = courses
        self.students = students
        self.grade_dict = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0}

    def convert_grade(self,letter_grade):
        return self.grade_dict[letter_grade]
    
    def add_grade(self, grade:Grade):
        self.grades.append(grade)
            
    def add_course(self, course:Course):
        self.courses.append(course)
    
    def add_student(self, student:Student):
        self.students.append(student)
    
    def read_grades_file(self, fname):

        with open(fname) as f:
            while True:
                line1 = f.readline()
                line2 = f.readline()
                line3 = f.readline()
                if not line3: break
                sid = int(line1)
                cid = int(line2)
                grd = str(line3).strip('\n')
                self.add_grade(Grade(sid,cid,grd))
    
    def read_course_file(self, fname):
        with open(fname) as f:
            while True:
                line1 = f.readline()
                line2 = f.readline()
                line3 = f.readline()
                if not line3: break
                id = int(line1)
                name = str(line2).strip('\n')
                credits = int(line3)
                self.add_course(Course(id, name, credits))

    
    def read_student_file(self, fname):
         with open(fname) as f:
            while True:
                line1 = f.readline()
                line2 = f.readline()
                if not line2: break
                id = int(line1)
                name = str(line2).strip('\n')
                self.add_student(Student(id, name))
    
    def get_student_name(self,id):
        for student in self.students:
            if student.get_id() == id:
                return student.get_name()

    
    def get_course_name(self,id):
        for course in self.courses:
            if course.get_id() == id:
                return course.get_name()
            
    
    def get_course_credit(self,id):
        for course in self.courses:
            if course.get_id() == id:
                return course.get_credits()
            
    def get_GPA(self, id, stream=None):
        total_points = 0
        total_credits = 0
        for grade in self.grades:
            if grade.get_student_id() == id:
                course_id = grade.get_course_id()
                name = self.get_course_name(course_id)
                credits = self.get_course_credit(course_id)
                points = self.convert_grade(grade.get_grade())
                total_credits += credits
                total_points += points * credits
                print(name, '\t\t', course_id, '\t\t', credits, file=stream)
        return total_points/total_credits
    
    def report_card(self, id, stream, write=False):
         
        print(self.get_student_name(id), file=stream)
        gpa = self.get_GPA(id, stream)
        print(f"GPA: {gpa}", file=stream)
        if isinstance(stream, io.StringIO) and write: 
            with open('reports\\report_card.txt', 'w') as f:
                print(stream.getvalue(), file=f)
            stream.close()

    
    def report_file(self, stream):
        print('=========================================================', file=stream)
        for student in self.students:
            sid = student.get_id()
            self.report_card(sid, stream, False)
            print('=========================================================', file=stream)
        if isinstance(stream, io.StringIO): 
            with open('reports\\report.txt', 'w') as f:
                print(stream.getvalue(), file=f)
        stream.close()
    



