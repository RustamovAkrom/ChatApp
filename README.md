## My Django Project ChatApp

### Run on Shell Windows

---
 - Configurations secret keys
 1. create ".env" file add django secret key to atribute "SECRET_KEY" example file ".env-example"

 - Configurations env and install modules
1. ```python -m venv env```
2. ```env\Scripts\activate```
3. ```pip install -r requirements.txt```
 - Configurations database and start project
1. ```python manage.py makemigrations```
2. ```python manage.py migrate```
3. ```python manage.py runserver```

### Enter Browser url ->
    http://127.0.0.1/