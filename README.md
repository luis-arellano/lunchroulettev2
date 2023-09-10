# PRE-REQS

## BackEnd

the list of backend dependencies will be listed on requirements.txt

always use a virual environment

```
source myenv/bin/activate
```

to install all the requirements (after activating the virtual environment)

```
pip install -r requirements.txt
```

there are some environmental variables needed to run the application

LUNCHROULETTE_URI

## Frontend

The list of react dependencies will be listed in frontend/package.json
To install these run:

yarn will crate the node modules and will pick up the right version to avoid conflicts
```
yarn install
```
-----------------------------------
## Running LunchRoulette

to start the backend we can run

```
python3 app.py
```

to start the frontend we can run

```
npm start
```

# Database
The db is stored in AWS RDS. 

-host name: is database-1.ciiowaujelgi.us-west-2.rds.amazonaws.com
-database: lunchroulette

# Working with Env Variables

To get the environmental variables stored in the machine we need to save them on ~/.bash_profile (mac)

nano ~/.bash_profile

LUNCHROULETTE_URI = 'path_to_the_uri'

To view the varibale

echo $VARIABLE_NAME