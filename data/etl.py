"""
ETL for populating the World Wealth and Poverty database
"""

import csv, os, sqlalchemy as sql
from sqlalchemy import create_engine
import psycopg2


# Create custom connection function
def db_connection():

    # Define credentials using environment vars
    host = os.environ.get('POSTGRES_HOST')
    db = 'wwp'
    user = os.environ.get('POSTGRES_USER')
    pgpass = os.environ.get('PG_PASS')

    connection = psycopg2.connect(database=db, host=host, user=user, password=pgpass)
    return connection


# Define engine
engine = create_engine('postgresql+psycopg2://', creator=db_connection)


def load_continents():


    # Seed the users table w/ sample data from csv file
    with open('tblContinents.csv', 'r') as data_file:
        reader = csv.reader(data_file)
        next(reader)  # Skip header row
        for row in reader:
            engine.execute( # Parameterize query to avoid SQL injections
                "INSERT INTO nations_continents(id, name, total_population, countries) VALUES(%s, %s, %s, %s)",
                row
            )


def load_nations():


    # Seed the users table w/ sample data from csv file
    with open('tblNations.csv', 'r') as data_file:
        reader = csv.reader(data_file)
        # next(reader)  # Skip header row
        for row in reader:
            engine.execute( # Parameterize query to avoid SQL injections
                "INSERT INTO nations_nations(id, name, region, gov_type, total_population) VALUES(%s, %s, %s, %s, %s)",
                row
            )


def load_economic():


    # Seed the users table w/ sample data from csv file
    with open('tblFinancial.csv', 'r') as data_file:
        reader = csv.reader(data_file)
        # next(reader)  # Skip header row
        for row in reader:
            engine.execute( # Parameterize query to avoid SQL injections
                "INSERT INTO nations_economic(id, name, gdp, gdp_per_capita, gini, unemployment, poverty_rate) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                row
            )


def main():

    db_connection()
    # load_continents()
    # load_nations()
    load_economic()


main()
