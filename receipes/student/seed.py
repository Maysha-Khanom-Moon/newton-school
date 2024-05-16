from faker import Faker
fake = Faker()

import random
from .models import *

def seed_db(n=10) -> None:
    
    try:
        for _ in range(0, n):
            department_objs = Department.objects.all()

            department_index = random.randint(0, len(department_objs) - 1)
            department = department_objs[department_index]

            student_id = f'STU-0{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            Student.objects.create(
                department =department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )
    except Exception as e:
        print(e)


# create marks
def create_subject_marks():
    try:
        student_objs = Student.objects.all()
        
        for obj in student_objs:
            subjects = Subject.objects.all()
            
            for sub in subjects:
                SubjectMark.objects.create(
                    subject = sub,
                    student = obj,
                    marks = random.randint(0, 100)
                )
            
    except Exception as e:
        print(e)