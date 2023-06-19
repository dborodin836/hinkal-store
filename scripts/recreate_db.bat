@echo off
set PG_PASSWORD=postgres
set DB_NAME=hinkal-store
set USER_NAME=postgres

setx PGPASSWORD "%PG_PASSWORD%"

psql -U %USER_NAME% -d postgres -f ./sql/close_db_connections.sql
dropdb -U %USER_NAME% --if-exists %DB_NAME% 
createdb  -U %USER_NAME% %DB_NAME% 