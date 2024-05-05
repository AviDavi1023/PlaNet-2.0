from django.apps import AppConfig


class PlantidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PlantID'

class UserAuthConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'user_auth'