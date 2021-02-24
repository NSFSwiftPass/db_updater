# CU PASS Database Updater

## Getting started
1. Install a new Pyhton virtual environment
   1. `python3 -m venv venv`
   1. Run `source ./venv/bin/activate` in each terminal session.
1. Install `requirements.txt`
   1. `pip install -r requirements.txt`
1. Get connection and login information
   1. See the "Getting a DB User Account" section
1. Set up `.env` file
   1. Refer to the "Config Variables" section of this document.
1. Run importer script
   ```bash
   python3 db_updater/scripts/daily_sync.py
   ```

## Config Variables
Ask another developer for these values

- DB_NAME
- DB_PASSWORD
- DB_URL
- DB_USERNAME
- LOG_LEVEL

## Getting a DB User Account
1. Create login for new user
   1. Right-click on DB cluster in pgAdmin -> create login
   1. Right click on schema -> Properties -> Security -> grant user
   1. Right click on schema -> Grant wizard -> grant all tables to user
1. Whitelist IP address
   1. Visit https://whatismyipaddress.com/
   1. Add PostgresSQL as inbound rule on that IP address in the DB security group
https://us-east-2.console.aws.amazon.com/vpc/home?region=us-east-2#SecurityGroup:group-id=sg-0da92c9dcabda08bd
1. Follow https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html#USER_ConnectToPostgreSQLInstance.pgAdmin
   1. Use your personal login created in previous steps.
   1. Other connection information can be found here https://docs.google.com/spreadsheets/d/1jYc5yAl-P9QssvucMNjV2xRnnVV5RKaNq3MJ8xuAplo/edit#gid=0
