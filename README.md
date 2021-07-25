# dr_portal_api

This will serve as the main backend API for the Disaster Relief Ops Portal.

---

Ito ay magsisilbing backend API para sa Disaster Relief Ops Portal.

---

## Setup
Go to root project directory
``` sh
$ cd ict/dr_portal_api
```

## Setup Virtual Environment
We will use [venv](https://docs.python.org/3/library/venv.html), to initialize local virtual environment run the ff. command
``` sh
$ python3 -m venv venv
```
Activate virtual environment
``` sh
$ source venv/bin/activate
```
Install dependencies
``` sh
$ pip3 install -r requirements.txt
```
## Website Test Run
Run django in development mode 
``` sh
$ python3 django_test/manage.py runserver
```

## Twitter scraper management
Run twitter scraper
```sh
$ python3 django_test/manage.py twitterscraper --run
```
