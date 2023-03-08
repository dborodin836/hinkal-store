FROM node:18-alpine as build
WORKDIR /usr/local/app
COPY ./ /usr/local/app/
RUN npm install --legacy-peer-deps
RUN npm run build -- --configuration=docker

FROM nginx:1.22-alpine
COPY --from=build /usr/local/app/dist/frontend /usr/share/nginx/html
RUN mkdir -p /home/app/staticfiles
