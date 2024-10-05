#!/bin/sh

export PGUSER=postgres

# Create the database
psql -c "CREATE DATABASE fkcommerce;"

# Create the uuid-ossp extension in the newly created database
psql -d fkcommerce -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"