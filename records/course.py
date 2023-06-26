# Course Class defintion

class Course():
    """Course class
    """    
    def __init__(self, id, name, credits):
     
        self.id = id
        self.name = name
        self.credits = credits

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credits(self):
        return self.credits
    
    def __repr__(self) -> str:
        return f"Course(id={self.id},name={self.name},credits={self.credits})\n"