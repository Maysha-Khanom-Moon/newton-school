1. got to models.py
2. import User from django.contrib.models
3. user = models.ForeignKey(User, on_delete=models.CASCADE)
    - CASCADE: delete all receipe if user deleted
    - SET_NULL: make null all the values/receipes if user deleted
    - SET_DEFAULT: make default values/receipes if user deleted

4. make a login page
    - add csrf_token and post method
5. create a views for login page
6. add url
7. do same as for register page

8. check User model
9. modify views
    - from django.contrib.auth.models import User
    - password encryption:
        - user.set_password(password) method

10. duplicate username
    - check username already exist or not?
        - if user.exists(): then redirect
        - but we should pass a error [messages](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/)
        - from django.contrib import messages
        - messages.info/X(request, "XXXmessageXXX")

        - then add into html file

11. login as same as register
    - views:
        - from django.contrib.auth import authenticate
        - used for encrypted password checking

12. session addition
    - how much time will loged in
    - import login as authenticate
    - just call login()
        - #### so that we set the views name as login_page, as if we don't faced recursive(infinite) calling


12. import decorator for authentication
    - [The login_required decorator](https://docs.djangoproject.com/en/5.0/topics/auth/default/#:~:text=The%20login_required%20decorator%C2%B6&text=from%20django.contrib.auth.decorators%20import%20login_required%20%40login_required,path%20in%20the%20query%20string.)
    - from django.contrib.auth.decorators import login_required

    - before specific view: @login_required

    - to check authentication: go to incognito mode

13. make logout_page