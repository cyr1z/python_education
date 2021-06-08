#! /bin/sh

psql -U postgres -c "CREATE DATABASE shop;"
psql -U postgres -d shop -f /docker-entrypoint-initdb.d/sql/schema.sql
psql -U postgres -d shop -f /docker-entrypoint-initdb.d/sql/import-data.sql
