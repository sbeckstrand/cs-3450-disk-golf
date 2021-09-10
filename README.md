# cs-3450-disk-golf

Disk Golf tournament organization web application. Designed by CS-3450

Sign up individual Competitors that can indicate their score and order drinks. They have a "cell phone" to track their score and get drinks.
- Drink Miester -- prepares the different drinks.
- Manager -- Creates tournaments. Picks winner and concludes that the game is finished.
- Sponsors -- Advertiser for drinks and pays for tournaments.

## Deployment

Prerequisits: 
- Python 3.x ![Installation Steps](https://docs.python.org/3/using/index.html)
- pip ![Installation Steps](https://pip.pypa.io/en/stable/installation/)


Clone Repository

```
git clone git@github.com:sbeckstrand/cs-3450-disk-golf.git
cd cs-3450-disk-golf
```

### Backend

Install `pipevn` and start Virtual Environment

```
pip install pipenv
pipenv shell
```

Install Django and other dependencies for the application

```
pipenv install django django-rest-framework django-cors-headers
```


Populate database with placeholder data and run application
```
cd backend
python manage.py migrate
python manage.py runserver
```

### Frontend


