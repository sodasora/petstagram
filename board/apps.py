from django.apps import AppConfig


<<<<<<<< HEAD:feed/apps.py
class FeedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feed'
========
class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'
>>>>>>>> a1fb7d826eb555cc6721eaef68944ec40a67a1fb:board/apps.py
