# App Deployment
App is hosted in [heroku](https://dashboard.heroku.com/apps/dro-portal)

## Connecting Github Repo and Heroku for Deployment
- in the [deploy page](https://dashboard.heroku.com/apps/dro-portal/deploy/github) of your app, choose the deployment option 'Github'
- Login into the Github account that Heroku will use to access your repo.
- Choose which repo to connect to the Heroku app

### Manual deployment
In this section you can choose to deploy a branch to run from the Github repo.

### Automatic Deployment
In this section you can choose which branch Heroku will monitor for automatic deployments. Once set, all updates to the assigned branch, whether from pushing direct commits or merging of pull requests, will trigger the app to automatically redeploy itself.

## Deploying Steps
### Build Phase
In this Phase Heroku will build the environment around the app. For this app it loads the Python buildpack and sets up the necessary dependencies based on the following files:
- [runtime.txt](../runtime.txt): loads the Python version stated there, if not available Heroku loads the latest supported version
- [requirements.txt](../runtime.txt): loads all necessary Python dependencies that the app needs
### Release Phase
Heroku runs shell commands stated after the "release:" tag in the [Procfile](../Procfile). These are for commands you might need to run before running the actual application. For this app, we set up the database and run the scraper.
### Deployment Complete
Heroku finally runs your application based on the shell commands after the "web:" tag in the [Procfile](../Procfile). For this app we run the [wsgi.py](../main/wsgi.py) file using gunicorn and set the PORT to whatever heroku default port

---

# Buildpacks and Add-ons
## Buildpacks
Buildpacks are scripts that are run when your app is deployed. They are used to install dependencies for your app and configure your environment. These are used to define the languages Heroku might expect from your code (i.e. Python, RoR, etc.) They are located in the [settings page](https://dashboard.heroku.com/apps/dro-portal/settings)

# Add-ons
Add-ons are secondary applications that will be connected to your application. These include databases and storage, monitoring and logging tools, testing, etc. They are located in the [resources page](https://dashboard.heroku.com/apps/dro-portal/resources)

---

# Config variables
Config variables contain specific environment variables that the app may reference at runtime but need to be defined outside the code. You can find these in the [settings page](https://dashboard.heroku.com/apps/dro-portal/settings)
