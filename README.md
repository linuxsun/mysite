

### download

```
https://github.com/linuxsun/mysite.git
```

### edit settings.py

```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'root',
        'PASSWORD': 'abcd123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```


### init

```
> pip install -r requirements
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
```


### run

```
python manage.py runserver 8000
```






