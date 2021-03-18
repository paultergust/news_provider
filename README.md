
# NEWS API PROJECT

  

A simple project to simulate a news provider API. Made with Django, DRF and PostgreSQL.



<a name=""></a>
# Table of contents

- [Requirements](#requirements)
- [Virtual environment](#virtual-environment)
- [Development Mode Setup](#dev_setup)
- [Production Mode Setup](#prod_setup)
- [Endpoints](#endpoints)
          
<a name="requirements"></a>
# Requirements 
 
- [Python](https://www.python.org/)
- [Pip](https://pip.pypa.io/)
- [Django](https://www.djangoproject.com)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)



# Virtual environment

  
Create new directory

```bash
mkdir news_provider
```
Change directory

```bash
cd news_provider/
```
Create virtual environment

```bash
python3 -m venv env
```
Activate virtual environment
```bash
# Windows:
env\Scripts\activate.bat

# On Unix or MacOS, run:
source env/bin/activate
```


<a name="dev_setup"></a>
# Development Mode Setup  

## Installation

Clone repository

```bash
git clone git@github.com:paultergust/news_provider.git
```
Change directory
```bash
cd news_provider
```
Install all dependencies
```bash
pip install -r requirements.txt
```

Make sure you have PostgreSQL runnint on port 5432. Then setup a database with credentials found in news_provider/settings.py:
  
```python
# news_provider/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': news_provider_api,
        'USER': news_provider_api,
        'PASSWORD': news_provider_api,
        'HOST': localhost,
        'PORT': 5432,
    }
}
```

Run django migrations
```bash
python manage.py makemigrations
```


Run django server with specific settings file
```bash
python manage.py runserver --settings=news_provider/dev_settings
```

<a name="prod_setup"></a>
# Production Mode Setup  

You'll need to have installed Docker, docker-compose and have a 'dockerd' instance running.

Clone repository

```bash
git clone git@github.com:paultergust/news_provider.git
```
Change directory
```bash
cd news_provider
```
After all set, just run:

```bash
make prod
```


OBS: If you get an error on this step, make sure you have port 5432 open. Maybe stop your local PostgreSQL service


```bash
sudo systemctl stop postgresql
```
<a name="endpoints"></a>
# Endpoints

- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- List articles: `/api/articles/?category=:slug`
- Administrator restricted APIs:
  - CRUD `/api/admin/authors/`
  - CRUD `/api/admin/articles/`


<a name="models"></a>
# Models

##Article:
  ```json
  {
    "id": "39df53da-542a-3518-9c19-3568e21644fe",
    "author": {
      "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
      "name": "Author Name",
      "picture": "https://picture.url"
    },
    "category": "Category",
    "title": "Article title",
    "summary": "This is a summary of the article"
  }

```

##Author:
```json

  {
    "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
    "name": "Author Name",
    "picture": "https://picture.url"
  }
```

##User:
```json

  {
    "username": "Username",
    "password": "write-only hashed password",
    "is_admin": false,
  }
```
