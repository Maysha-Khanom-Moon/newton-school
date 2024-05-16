### django shell
- allows you to work directly from the root folder of a Django project
- through shell we interact with django or database

- to go shell: python manage.py shell
    - from home.models import *

    - create a new object:
        - student = Student(name="Abhijeet", age=26, email="abhijeetg40@gmail.com", address="Lucknow", )
            - print(student)/ student  -->  Student object(None)
            - we just follow Student object field
        - to save student object: student.save()


    - create a new object via another way:
        - student = Student.objects.create(name="moon", age=21, email="maysha412@gmail.com", address="216/1 Kajla")
            - objects: model manager
        - it saved automatically
    
    - to see all objects: 
        - Student.objects.all()
        - we will get an array
        - so we can access data like an array
            - Student.objects.all()[0].name
            - Student.objects.all()[0].id  -->  in-built key
    
    - to update key-value of any object:
        - student = Student.objects.all()[1]
        - student.name = "Moon"
        - student.save()
        - Student.objects.all()[1].name


- #### funtion run/ test on shell:
    - make a file: utils.py
    - after putting import and def func, if we run directly then we will got ImportError
    - but we can call the def function from django shell
        - from home.utils import *
        - run_this_function()