## CRUD operations
- Create, Read, Update, Delete

- at first go to shell inside project path
- then import home.models

- #### to create:
    - already done. check 6_django_shell.
    - one:
        - car = Car(..., ...)
        - car.save()
    - two:
        - Car.objects.create(..., ...)


- #### to read:
    - create __str__(self):
        return self.car_name
    - Car.objects.all()
        - will show Car object with their name
    - if there is any issues then exit shell, again enter the shell and import

    - to get full object:
        - it will just show car_name/ __str__(self) return value
        - one:
            - Car.objects.all()[1]

        - two:
            - Car.objects.get(id = 2) --> 1 index
            - if id = 10 don't existed then it's an exception
        - we can check that id = 10 exist or not:
            - Car.objects.filter(id = 10)
                - if exist: return __str__(self)
                - else: return empty QuerySet


- #### to update:
    - one:
        - get the object and store into a variable
            - car = Car.objects.get(id = 1)
        - modifying
            - car.car_name = "Creata"
            - car.speed = 180
        - car.save()
    
    - two:
        - use update method
            - Car.objects.filter(id = 1).update(car_name = "Creta Dark Edition Limited")


- #### to delete:
    - delete all  -->  be careful
        - Car.objects.all().delete()
    
    - delete one
        - Car.objects.get(id = 1).delete()
            - it just make QuerySet empty
        - if it already empty then it will show query does not exist