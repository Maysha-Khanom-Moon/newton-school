## Receipe Project:
1. create new application:
    - django-admin startproject receipes
        - will create a 'receipes' folder

2. cd receipes

3. create a 'vege' app
    - python manage.py startapp vege

4. create class inside the 'vege' models
    - we create Receipe class

5. linked Receipe class inside the settings.py with INSTALLED_APPS

6. now make migrations

7. hit the migrate state
    - to registrate new table

9. create templates inside the 'vege' app

10. inside templates create html files

11. create views funtions
    - from django.http import HttpResponse
    - def function inside views.py
    - render with templates repo's html file

12. urls.py
    - import vege.views
    - add url path

13. python manage.py runserver

14. add form inside the index.html

15. Then store data from frontend to backend
    - post method: data frontend to backend  -->  at form
    - set the name of inputs same as models variable
    - for file upload:
        - add enctype="multipart/form-data"  -->  at form
            - otherwise just text data will pass


16. work on views.py
    - request.POST: we get all the data from fromend

    - but we will got Forbidden(403)
        - add {% csrf_token %} at the starting point of form
            - it checked that this request is from same server(where deployed) or not

    - at views file:
        - check if request.method == "POST":
            - for text:
                - data = data = request.POST
                - then data.get('input_name')

            - for file: 
                - 1. request.FILES.get('input_file_name')
                - 2. request.FILES['input_file_name']
    
    - import all from models
    - create a Receipe object
        - we will get a receipe folder with uploaded file


17. to see our uploaded text
    - go to admin.py
    - import .models
    - register model
        - admin.site.register(model_name)
        - admin.site.register(Receipe)
    
    - go to /admin panel at the url


18. check uploaded file via query(shell)
    - python manage.py shell
    - import all from vege.models
    - Receipe.objects.all()
        - Receipe.objects.all()[0].receipe_name
    
    - we can read  our name, file, description via shell.


19. After submit one time then if we reload:
    - it shows confirm resubmission
    - to solve this issue:
        - because it refreshed. So avoid it we should redirect this page
            - import redirect from django.shortcuts
            - return redirect('/receipes/')
            - add that url at urls.py