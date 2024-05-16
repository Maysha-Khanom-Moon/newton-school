### how we can get data from backend which we stored already
1. go to views.py
2. we will pass the queryset as context
3. we will print on the index.html
4. but image will not showed
    - [django managing file](https://docs.djangoproject.com/en/5.0/topics/files/)
    - [make django static file](https://docs.djangoproject.com/en/5.0/howto/static-files/)
        - follow these instructions
    
    - settings.py updating:
        - don't forget:
            - from django.conf import settings
            - from django.conf.urls.static import static
            - from django.contrib.staticfiles.urls import staticfiles_urlpatterns
        - copy-paste that section



#### how to delete:
1. create def delete_receipe inside views.py
    - import HttpResponse from django.http
    - get the id
    - then delete it

2. register this route inside the urls.py

3. add <a> tag and href="/return redirect('/receipes/')


#### update:
1. create update html page
2. set urls
3. make an app to update
4. then traditional methods


#### search:
1. set search option at index
2. browser understand it automatically
3. no method needed
4. get value:
    - at views.py: request.GET.get('search_receipe')
5. do filter:
    - queryset.filter.(receipe_name__icontains = search_receipe)