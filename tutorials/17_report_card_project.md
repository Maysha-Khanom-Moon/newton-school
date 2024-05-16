1. make a subject and SubjectMark model
    - inside models.py

2. register models
    - inside admin.py

3. make migrations and migrate

4. run server

5. go to admin panel

6. add subjects

7. def create_subject_marks
    - inside seed.py

8. go to shell
    - import seed
    - call create_subject_marks
    - we generate all marks

9. overwrite site registration --> admin list display
    - via SubjectMarkAdmin()
    - inside admin.py


10. #### for big data:
- inside views.py:
    - def get_students()