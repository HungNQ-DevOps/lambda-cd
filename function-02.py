# function.py:
import json
import psycopg2
import psycopg2.extras
import os
 # Comment test continuous deployment 1

def lambda_handler(event, context):
    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']
    db_host = os.environ['DB_HOST']
    db_port = os.environ['DB_PORT']
    db_pass = os.environ['DB_PASS']