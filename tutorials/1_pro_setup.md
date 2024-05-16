1. download python

2. virtual environment: pip install virtualenv
    - all thing bind into virtualenv. 
    - Like a room, where we just download our needed packages to complete a project.
    - Athough, now it's global.

3. start virtual environment: virtualenv env
    - will create a 'env' folder

4. activate env folder:
    - cd env
    - cd Scripts
    - activate
    - cd ..
    - cd ..

5. install Django: pip install Django

6. to check Django is installed or not:
    - python
    - import django
    - django.__version__
    - ^Z

7. create new application:
    - django-admin startproject core
        - will create a 'core' folder


### we will go for 'core'
- manage.py: bridge between django and application
- 'core' folder:
    - __init__.py: used to mark a directory as a Python package. To lead others files inside the 'core'

    - asgi.py: server wala file. 
        - supply an application callable which the application server uses to communicate with your code.
        - ASGI: Asynchronous Server Gateway Interface

    - wsgi.py: web wala file.
        - a mediator responsible for conveying communication between a web server and a Python web application.
        - WSGI: Web Server Gateway Interface

    - urls.py: where we maps all the urls
        - contains the root URL configuration or URLConf of the entire project

    - settings.py: we add all the settings
        - configuring all Django projects
        - defined as constant variables and they should be written with capital letters

- mostly we modify: wsgi, urls, settings