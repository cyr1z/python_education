#! /bin/sh

psql -U postgres -c "CREATE DATABASE pagila;"
psql -U postgres -d pagila -f /docker-entrypoint-initdb.d/sql/pagila-schema.sql
psql -U postgres -d pagila -f /docker-entrypoint-initdb.d/sql/pagila-insert-data.sql
