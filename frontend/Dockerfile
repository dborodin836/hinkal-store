FROM node:18 as build
WORKDIR /usr/local/app
COPY ./ /usr/local/app/
RUN npm install
RUN npm run build
FROM nginx:1.22-alpine
COPY --from=build /usr/local/app/dist/frontend /usr/share/nginx/html
