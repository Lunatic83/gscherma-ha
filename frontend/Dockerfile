FROM node:14-alpine

# make the 'app' folder the current working directory
WORKDIR /usr/src/app

# # copy both 'package.json' and 'package-lock.json' (if available)
# COPY package*.json ./
# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY package.json .


# install project dependencies
RUN npm install 

COPY . .

EXPOSE 8080
CMD ["npm", "run", "serve"]

