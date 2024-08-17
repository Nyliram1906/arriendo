from django.apps import AppConfig


class M7PythonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'm7_python'

class M7PythonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'm7_python'

    def ready(self):
        import m7_python.signals  # Importa las señales aquí