1. create a 'student' app:
    - python manage.py startapp student


2. inside the urls:
    - from student.views import *

3. inside the views:
    - from .models import *


4. inside the settings:
    - add 'student' inside the EXTERNAL_APPS


5. making 3 fields:
    - Department
    - StudentID
    - Student

    - ForeignKey  -->  One to many or many to one
        - it can be used for multiple time
    
    - one to one  --->  one value assign for one object
        - although it's not about uniqueness
        - it just check the existing keys
        - and keys can be duplicate also 


6. make migrations and migrate


7. go to '/admin' url
    - must have to logined as super user

8. create a superuser
    - python manage.py createsuperuser
    - Username: moon
    - Email: maysha412@gmail.com
    - Password: 1234
    - Password (agein): 1234

9. then loged in

10. why student app not showed in admin dashboard
    - import .models
    - register app fields inside the admin.py


11. Create, Modify, Delete any of these fields via admin dashboard


12. but, its very time consuming if we try to feed these all datas manually
    - here came: [faker](https://faker.readthedocs.io/en/master/)
        - it generate fake datas


13. create a file 'seed.py'

14. then follow faker documentation
    - pip install faker
    - seed_db() creates

15. got to shell 
    - import seed
    - call seed_db() again and again😒

