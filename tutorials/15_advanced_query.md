1. go to shell

2. import student.models

3. queries:
    - queryset = Student.objects.filter(student_name__startswith = 'mo')

    - queryset = Student.objects.filter(student_email__endswith = 'org')
    
    - queryset = Student.objects.filter(student_name__icontains = 'moon')


4. How to access foreign key?
    - '__' used for inbuilt funtions
    - but for foreign key sometimes we overright the funtinos
    - Student.objects.filter(department__department = 'Civil')
        - '__' works as '.'
        - 1st department: access department of Student
        - 2nd department: access department of Department
    
    - queryset = Student.objects.filter(department__department__icontains = 'Civil').count()
        - 1st '__': foreign key wala --> work as '.'
        - 2nd '__': django wala --> inbuilt funtion call
        - queryset.count(): total elements which matched
    

5. find Civil or Com department at once:
    - d = ['Civil', 'Electrical']
    - for number:
        - queryset = Student.objects.filter(department__in = d)
            - field id expectedd

    - for string:
        - queryset = Student.objects.filter(department__department__in = d)
        - a khetre puro nam match kora lagbe


6. Find all student data except 'Civil' department:
    - queryset = Student.objects.exclude(department__department = "Civil")


7. data existing check:
    - queryset = Student.objects.filter(student_name = "Moon")
    - queryset.exists()
        - False


8. Set limit to showing data:
    - just like slice
    - queryset[0:100]
        - show first 100 datas


9. Showing all values of a object:
    - queryset.values()
    - to get foreign key value
        - do not use '.'
        - use '__'


10. [Finds more queries](https://docs.djangoproject.com/en/5.0/ref/models/querysets/)