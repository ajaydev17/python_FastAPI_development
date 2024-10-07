#!/bin/sh

export PGUSER=postgres

# Create the database
psql -c "CREATE DATABASE inventory;"

# Create the uuid-ossp extension in the newly created database
psql -d inventory -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"