# Thales NPL API Server

Generate virtual environment
```
$ python3 -m venv ./venv
```

Activate virtual environment
```
$ source venv/bin/activate
```

Install required dependencies
```
$ (venv) pip install -r requirements.txt
```

Generate secret key file 
```
$ (venv) cp thales/secret_key.txt.example  thales/secret_key.txt
```

Migrate project
```
$ (venv) python manage.py migrate
```

Create a super user to define API clients
```
$ (venv) python manage.py createsuperuser
```