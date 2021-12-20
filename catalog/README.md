This folder contains the majority of the code for the web application. Subdirectories explained below.

# Jobs

This folder contains functions or commands that can be run on the terminal

# Management

You can define custom management commands as needed. Read the docs [here](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/)

# Migrations

This folder contains the initial database migration definitions for initial setups of the database

# Models

This folder contains the object data that Django will use to configure the database migrations

# Seed

This folder contains the initial data that our app needs

#### Run the ff. command to load the data into the database
```sh
$ python3 manage.py runseeder
```

# Templates

This is a default folder from the initial django setup. For modularity and maintainability, only add templates that are specific to /catalog or templates that will be used for the models declared in catalog/models/ directory. Templates that can be used project-wide should be in the project's root /templates directory
