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

To get the environmental variables stores in the machine

echo $VARIABLE_NAME

To save a variable name

echo 'export VARIABLE_NAME=VALUE' >> ~/.bashrc
source ~/.bashrc

echo 'export LUNCHROULETTE_URI=mysql+mysqlconnector://root:rockclimber1!@database-1.ciiowaujelgi.us-west-2.rds.amazonaws.com:3306/lunchroulette' >> ~/.bashrc