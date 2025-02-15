import os
import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pinky_beauty_bar_project.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Obtener credenciales desde variables de entorno
username = os.getenv("DJANGO_SUPERUSER_USERNAME")
email = os.getenv("DJANGO_SUPERUSER_EMAIL")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("✅ Superusuario creado exitosamente")
    else:
        print("⚠️ El superusuario ya existe")
else:
    print("❌ Error: Faltan variables de entorno")
