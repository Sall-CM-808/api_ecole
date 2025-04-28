from django.apps import AppConfig


<<<<<<<< HEAD:src/student/apps.py
class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'
========
class EvaluationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'evaluation'
>>>>>>>> a71fe55a5ff9da5affa9962e7941512fa64bc7c8:src/evaluation/apps.py
