# grade class

class Grade():
    def __init__(self, student_id, course_id, grade) -> None:
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade

    def get_student_id(self):
        return self.student_id
    
    def get_course_id(self):
        return self.course_id
    
    def get_grade(self):
        return self.grade
    
    def __repr__(self):
        return f"Grade(sid={self.student_id},cid={self.course_id},grd={self.grade})\n"