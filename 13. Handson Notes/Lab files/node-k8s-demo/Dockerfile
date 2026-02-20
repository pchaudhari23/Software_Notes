# Use official Node image
FROM node:18-alpine

# Create app directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy source
COPY server.js .

# Expose port
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
