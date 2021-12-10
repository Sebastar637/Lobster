#Pasos para instalar


py -m venv venv

venv\Scripts\activate

pip install django==3.1.7 channels django-allauth django-crispy-forms django-taggit pillow

py manage.py makemigrations

py manage.py migrate


#Para abrir el servidor

py manage.py runserver
