#Pasos para instalar


py -m venv venv
venv\Scripts\activate
pip install django channels django-allauth django-crispy-forms django-taggit pillow
py manage.py makemigrations
py manage.py migrate

#Para abrir el servidor

py manage.py runserver
