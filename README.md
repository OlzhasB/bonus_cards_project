# bonus_cards_project
Web app for managing database of bonus cards

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/OlzhasB/bonus_cards_project.git
```


Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```


Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```


After that you have to add apps to `settings.py`:

```sh
INSTALLED_APPS = [
    *** django apps ***
    'cards_model',
]
```


You have to connect django project with DB (I used PostgreSQL):

First method(by adding db to databases in `settings.py`):

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'card_db',
        'USER': 'olzhas',
        'PASSWORD': 'olzhas',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    		}
	   }
```

Second method(by docker command):

```sh
docker run -d -p 5432:5432 -e 
POSTGRES_USER=olzhas -e 
POSTGRES_PASSOWRD=olzhas -e 
POSTGRES_DB=card_db --name 
my_postgredb postgres
```


After creating views, models, forms, etc, you have to migrate all the changes to DB: 

```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
```


Finally run your server:

```sh
(venv)$ python manage.py runserver
```


To take admin roots you have to create superuser(edit anything in the web app):

```sh
(venv)$ python manage.py createsuperuser
```

