# Disk Golf tournament organization web application. Designed by CS-3450 - Council of the Brandons

## Workspace Naming Scheme / Structure

API/Backend - /backend

Documentation/Diagrams - /docs

Frontend - /frontend (eventually)

## Version-control procedures

The version control is going to be handled utilizing github's available tools.  We will be cloning the MAIN branch, and then submitting pull requests.
Once a pull request for a feature is made, another member of the team that didn't write that code will read through it and merge it into MAIN.

## Tool stack description and setup procedure
	Github
	Discord
	Zoom
	Jira
	Python
	Django Framework

## Build instructions

### Prerequisits:

- Python 3.x ![Installation Steps](https://docs.python.org/3/using/index.html)
- pip ![Installation Steps](https://pip.pypa.io/en/stable/installation/)

### Clone Repository
```
git clone git@github.com:sbeckstrand/cs-3450-disk-golf.git
cd cs-3450-disk-golf
```

### Backend:

Install `pipenv` and start Virtual Environment

```
pip install pipenv
pipenv shell
```

Install Django and other dependencies for the application

```
pipenv install django django-rest-framework djangorestframework-simplejwt django-cors-headers npm Pillow
```

Populate database with placeholder data and run application
```
cd backend
python manage.py migrate
python manage.py runserver
```

### Frontend
See Nuxt Documentation: https://nuxtjs.org/docs/get-started

1) In a separate terminal window,pane or screen session, change to repository directory

2) Activate the virtual enviornment for the new session

```
pipenv shell
```

Install needed Node modules (may need to be run as root):

```
cd frontend
npm install 
npm run dev
```

### General Notes

For the purpose of demonstrating the app's functionality, three default users have been created with different roles

1: User: `manager` Pass: `manager` ID: `1`

2: User: `drinkster` Pass: `drinkster` ID: `2`

3: User: `sponsor` Pass: `sponsor` ID: `3`

Note: 'Manager' role can access other profiles at `/profile/<id>` and change their role assignments

## Unit testing instructions

Unit tests exist under `/backend/api/tests.py`

Currently unit tests exist to check valid creation of object types: User, Tournament, Drink, DrinkOrder

Tests can be run by issuing the following command from the backend directory: 

```
python manage.py test
```



	
## Other development notes, as needed
	