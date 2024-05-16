#### HTML Tamplate/Response
- data return from backend


- all logical parts written inside the views.py
    1. import HttpResponse form django.http

    2. so our backend server will return a http response for a http request

    3. def func(request): 
        return HttpResponse("htlm_code")

        - for multiline html_code use """.... """



- routing inside the urls.py
    4. Then bind the app inside the urls.py of 'core'
        - import * form home.views
            - 'home': we can choose any other app

        - now make a router inside the urlpatterns
            - path('route_extention', funtion)
                - which function will return
            - path('', home, name="home")
            - blank-wala route



#### nowadays
- html codes are very complex, so we have to return actual html tamplate codes form backend django server
- create a tamplates folder  (inside the working repo)
    - like: if 'views.py' inside the 'home' then 'templates' also create inside the 'home'
- then create index.html inside the tamplate
- to render the html file
    - return render(request, "index.html")