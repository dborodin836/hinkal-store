-- Prohibit new connections
UPDATE pg_database
SET datallowconn = 'false'
WHERE datname = '%DB_NAME%';

-- CLose active connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = '%DB_NAME%' AND pid <> pg_backend_pid();
