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
pipenv install django django-rest-framework djangorestframework-simplejwt django-cors-headers npm
```

Populate database with placeholder data and run application
```
cd backend
python manage.py migrate
python manage.py runserver
```

### Frontend
See Nuxt Documentation: https://nuxtjs.org/docs/get-started

Install needed Node modules (may need to be run as root):

```
cd frontend
npm install 
npm run dev
```

## Unit testing instructions
	--TODO--

## System testing instructions
	--TODO--
	
## Other development notes, as needed
	