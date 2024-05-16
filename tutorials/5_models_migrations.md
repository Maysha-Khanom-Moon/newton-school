* most important topics: models and migrations

### models.py
- database structure
- class model-name(models.Model):
    - string = models.CharField(custom) --> single line
    - int = models.IntegerField(custom)
    - email = models.EmailField()
    - address = models.TextField() --> multi line
    - image = models.ImageField()
    - file = models.FileField() --> for doc, excel, txt, etc
- [Checkout all django models](https://docs.djangoproject.com/en/5.0/topics/db/models/)


### migrations
- when we create or modify a schema, we must have to connect each time with db.sqlite3 via migration
- open db.sqlite3 on the DB Browser(SQLite)

- steps:
    - 'core' terminal: python manage.py makemigrations
        - create 0001_initial.py inside the migrations
            - Create model Student(existing models)
        - inside 0001_initial.py: 2 field is most important
            - dependencies: first migration a no dependency
            - operations

    - after some changes if we again makemigrations
        - create 0002_modified_model.py inside the migrations
        - dependencies upon 'home', '0002_modified_model.py'
            - if we delete '0001_initial.py' then database will collapsed.

- now hit the datas into db.sqlite3
    - python manage.py migrate
    - if I delete any of these 000n file then database will collapsed.
    - it create a state model

- how django understand the modifications
    - just compare current state model with previous state model before hit migrate
    - if there is no change then no migration to apply









































