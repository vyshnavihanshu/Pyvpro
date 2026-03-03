class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        if self.marks > 0:
            return True
        return False
s1=Student("Vyshu",45)
s2=Student("Ramya",67)

if s1.is_passed():
    print(s1.name,"has passed")
else:
    print(s1.name,"has not passed")
if s2.is_passed():
    print(s2.name,"has passed")
else:
    print(s2.name,"has not passed")

