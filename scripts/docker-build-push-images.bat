docker build ./backend/ --tag dborodin836/hinkal-backend:latest
docker push dborodin836/hinkal-backend:latest

docker build ./frontend/ --tag dborodin836/hinkal-nginx:latest
docker push dborodin836/hinkal-nginx:latest
