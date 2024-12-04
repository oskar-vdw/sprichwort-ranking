# Define the base image for Node.js
FROM node:18 as base

# Set the working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the application code
COPY . .

# Builder stage for production
FROM base as build
RUN npm run build

# Production stage with Nginx
FROM nginx:alpine as production
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# Development stage
FROM base as development
EXPOSE 5173
CMD ["npm", "run", "dev"]
