### ORM
- Object Relational Mapping
- a pythonic technique to build SQL to query and edit your database and obtain results.


1. create a new field inside the Receipe model
    - receipe_view-count

2. makemigrations and migrate

3. go to shell
    - from vege.models import *
    - check all objects  --->  vege
    - import random

4. interate all objects  --->  vege
    - for veg in vege:
        - veg.receipe_view_count = random.randint(10, 100)  ---> between 10 to 100
    
    - check the random view_count of receipes
        - via vege[i]  -->  it's not saved yet inside the DBs
        - to save: vege[i].save()
            - we can add this save function side the loop
    
    - now you can get values via get method or iteration.


5. sorting
    - order_by:
        - ascending order
            - vege.order_by('receipe_view_count')
        
        - descending order
            - vege.order_by('-receipe_view_count')
            - most viewed **


6. limit
    - slicing operator:
        - vege.order_by('receipe_view_count')[0:2]
            - get only 1st 2 records
        - [n: m]: from n-th index to after --> get m recodes

7. filter
    - just finds the matches
        - Receipe.objects.filter(receipe_view_count = 89)
            - it returns a list
        - see the attribute values use loop
    
    - find the equal and greater ones
        - Receipe.objects.filter(receipe_view_count__gte = 89)
    
    - find the equal and lesser ones
        - Receipe.objects.filter(receipe_view_count__lte = 89)