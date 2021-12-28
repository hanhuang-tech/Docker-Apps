FROM node:alpine
WORKDIR /home/expressapp/
COPY package*.json /home/expressapp/
COPY index.js /home/expressapp/
RUN npm install
EXPOSE 9000
CMD npm run start

