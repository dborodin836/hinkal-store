FROM node:18-alpine as build
WORKDIR /usr/local/app
COPY ./ /usr/local/app/
RUN npm install --legacy-peer-deps &&\
    npm run build
FROM nginx:1.22-alpine
COPY --from=build /usr/local/app/dist/frontend /usr/share/nginx/html
