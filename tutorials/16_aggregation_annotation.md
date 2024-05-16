- shell:
    - from django.db.models import *
    - from student.models import *



#### Django Aggregation
- to perform calculations --> whole sets of database
- Count, Sum, Avg, Max, Min  -->  aggregate functions

- syntax:
    - Student.objects.aggregate(Avg('student_age'))



#### Django Annotate
- identifies the summary from each item in the queryset

- multiple aggregation
- it can perform calculations --> segmentwise or specific
- kind of looping + aggregation

- syntax:
    - Student.objects.values('student_age').annotate(Count('student_age'))
    - Student.objects.values('department').annotate(Count('department'))


- multiple object:
    - Student.objects.values('department', 'student_age').annotate(Count('department'), Count('student_age'))
        - both count answer will same



#### [document](https://docs.djangoproject.com/en/5.0/topics/db/aggregation/)
