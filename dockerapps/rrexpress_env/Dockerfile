FROM node:alpine
WORKDIR /home/rrexpress_env/
COPY package*.json /home/rrexpress_env/
COPY index.js /home/rrexpress_env/
RUN npm install
EXPOSE 9000
CMD node index.js
