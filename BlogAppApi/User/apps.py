from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'
    
    
    def ready(self):
        # Sinyallerin yüklenmesini sağlar
        import User.signals