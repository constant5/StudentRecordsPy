#python3

from records.studentrecords import StudentRecords
import sys
import io



if __name__=='__main__':

    SR = StudentRecords()

    SR.read_grades_file('data\\grades.txt')
    SR.read_course_file('data\\courses.txt')
    SR.read_student_file('data\\students.txt')


    SR.report_card(1, io.StringIO(), True)
    SR.report_file(io.StringIO())

    SR.report_card(1, sys.stdout, False)
    SR.report_file(sys.stdout)
  
