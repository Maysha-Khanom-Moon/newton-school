1. activate env

2. then go to 'core' project path
    - newton-school\core>

3. python manage.py startapp home
    - django will create a directory as 'home'

4. file system check of 'home'
    - __init__.py: used to mark a directory as a Python package. To lead others files inside the 'home'
    - admin.py: customised admin panel or model registration
    - apps.py: AppConfig classes so that Django can find them. Generic entry point for applications.
    - models.py: django models are python classes representing data structures in a relational database for efficient database operations.
    - tests.py: contain test cases, which are subclasses of Django TestCase class.
    - views.py: takes http requests and returns http response, like HTML documents.
        - add functionalit


5. server boot-up
    - python manage.py runserver
    - follow http link

6. for custom port
    - python manage.py runserver 5000
    - it will open via 5000 port

7. django k bolte hobe j amr project er moddhe ami kon kon app use korchi
    - go to settings.py
    - add 'accounts', 'home' inside INSTALLED_APPS
        - 2 ways have
        - for big project use EXTERNAL_APPS


* * * we divide our module as individual directory. so, we can re-use our features via copy-paste.