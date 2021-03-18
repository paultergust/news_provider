
# NEWS API PROJECT

  

A simple project to simulate a news provider API. Made with Django, DRF and PostgreSQL.



<a name=""></a>
# Table of contents

- [Requirements](#requirements)
- [Virtual environment](#virtual-environment)
- [Installation](#installation)
- [Setup](#setup)
          
# Requirements 
 
- [Python](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [PostgreSQL](https://www.postgresql.org/download/)



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

<a name="setup"></a>
# Setup  

Make sure you have PostgreSQL runnint on port 5432. Then setup a databse with credentials found in news_provider/settings.py:
  
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
