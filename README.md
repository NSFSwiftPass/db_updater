# CU PASS Database Updater

## Getting started
1. Install a new Pyhton virtual environment
   1. `python3 -m venv venv`
   1. Run `source ./venv/bin/activate` in each terminal session.
1. Install `requirements.txt`
   1. `pip install -r requirements.txt`
1. Get connection and login information
   1. https://docs.google.com/document/d/1qG4dIsfTwPXKOwS7E3sjHcpNjHM5uV5bs8Z5hOv91d8/edit
1. Set up `.env` file
   1. Refer to the `Config Variables` section of this document.
1. Generate ORM classes
   ```bash
   python3 db_updater/database/generate_db_classes.py
   ```

## Config Variables
- DB_USERNAME
- DB_PASSWORD
