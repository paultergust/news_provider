
# NEWS API PROJECT

  

A simple project to simulate a news provider API. Made with Django, DRF and PostgreSQL.



<a name=""></a>
# Table of contents

- [Requirements](#requirements)
- [Virtual environment](#virtual-environment)
- [Installation](#installation)
- [Development Mode Setup](#dev_setup)
- [Production Mode Setup](#prod_setup)
          
# Requirements 
 
- [Python](https://www.python.org/)
- [Pip](https://pip.pypa.io/)
- [Django](www.djangoproject.com)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)



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


<a name="installation"></a>
# Installation

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

<a name="dev_setup"></a>
# Development Mode Setup  

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
After all set, just run:

```bash
make prod
```


OBS: If you get an error on this step, make sure you have port 5432 open. Maybe stop your local PostgreSQL service


```bash
sudo systemctl stop postgresql
```
