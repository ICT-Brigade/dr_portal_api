# dr_portal_api
This will serve as the main backend API for the Disaster Relief Ops Portal.
---

Ito ay magsisilbing backend API para sa Disaster Relief Ops Portal.
---

## Setup
Go to root project directory
``` sh
$ cd dr_portal_api/
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

## Setup database
For initial database setup and if there are database schema changes, run the ff. commands
```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## Setup Environment Variables
Inside the folder 'main' create the file '.env' containing key-value pairs in the following format
'''
KEY=VALUE
'''
Note there should be no space around the '=' and string values do not need.
You can refer to the config variables [the heroku dashboard](https://dashboard.heroku.com/apps/dro-portal/settings)
Sample .env file
'''
SECRET_KEY=random_text
DEBUG=1
'''

## Website Test Run
Run django in development mode
``` sh
$ python3 manage.py runserver
```

## Twitter scraper management
### Initialize seeders
Seeder will setup keywords and tags for running the scraper
Run the ff. command
```sh
$ python3 manage.py runseeder
```
### Run twitter scraper
```sh
$ python3 manage.py twitterscraper --run
```
