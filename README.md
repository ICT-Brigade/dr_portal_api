[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# dr_portal_api
This will serve as the main codebase for the Disaster Relief Ops Portal.
---
Ito ang magsisilbing pangunahing codebase para sa Disaster Relief Ops Portal.

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

## Coding Standards
Before you get your hands dirty install pre-commit in your local machine
```bash
$ pre-commit install
```

- Always validate inputs especially those from the client side
- Make your SQLs injection proof
- Break functions/methods more than 10 lines of code
	Long functions are hard to read and debug, and 10 lines is usually a good point to break the function into smaller parts. Smaller functions are easy to read and review. You might even want to convert a series of functions into a class so you don't need to pass parameters through all of them.

	As Steve Mcconnell and Bob Martin say (two pretty good references on coding best practices), a method should do one thing and only one thing. However many lines of code it takes to do that one thing is how many lines it should have. If that "one thing" can be broken into smaller things, each of those should have a method. Good clues your method is doing more than one thing:

	- More than one level of indention in a method (indicates too many logic branches to only be doing one thing)
	- "Paragraph Breaks" - whitespace between logical groups of code indicate the method is doing more than one thing

- Indentation
	- The indentation must be consistent whether you are writing Javascript or Python. Multi-line strings or expressions must also be consistently indented, not hanging like a bee hive at the end of the line. We just think the code looks a lot more stable that way.
- Use simple structures
	- Code must be easy to read, so don't try clubbing multiple conditions in one line and make it complex. If you have a line that has multiple AND or OR, break it up into multiple conditions.
Code must be easy to read, so don't try clubbing multiple conditions in one line and make it complex. If you have a line that has multiple AND or OR, break it up into multiple conditions.
- Commit messages must follow the conventional commit specifications (https://www.conventionalcommits.org/en/v1.0.0-beta.2/)
- Function sequence
	- If you have multiple functions in a file, the calling function should be on the top and the called functions should be below. Check the example below:
	```python
		def fa():
			fb()
			fc()

		def fb():
			pass

		def fc():
			pass
	 ```
- Code Comments
	- While we believe that code should be written in a self-explanatory way, comments will go a long way in expressing "why" the code is written in a particular manner.
	- We don't expect heavily commented code, but some explanation of what a method does is required. Read [this](http://antirez.com/news/124) post on why code commenting is important.
- Avoid using Deprecated API

## Setup database
For initial database setup and if there are database schema changes, run the ff. commands
```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## Setup Environment Variables
Inside the folder 'main' create the file '.env' containing key-value pairs in the following format.
Note that there should be no space around the '=' and string values do not need.
```
KEY=VALUE
```
You can refer to the config variables [the heroku dashboard](https://dashboard.heroku.com/apps/dro-portal/settings)

**Sample .env file**
```
SECRET_KEY=random_text
DEBUG=1
```

## Run Webapp Locally
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

## Heroku Deployment
[Link to Heroku Deployment Documentation](documentation/deployment.md)
