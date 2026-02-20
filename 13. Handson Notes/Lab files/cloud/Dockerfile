# NODE APP:

# 1. Use official Node.js base image
FROM node:20-alpine

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency files first (better caching)
COPY package*.json ./

# 4. Install dependencies
RUN npm install --production

# 5. Copy application source code
COPY . .

# 6. Expose the port Express uses
EXPOSE 3000

# 7. Start the Express server
CMD ["npm", "start"]


# Run command:
# docker build -t express-app .
# docker run -p 3000:3000 express-app

# ###############################################################################
# REACT APP:

# 1. Use official Node.js base image
FROM node:20-alpine           

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# Build the React app
RUN npm run build


# ---- Production stage ----
FROM nginx:alpine

# Copy build output to Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Expose port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

# docker build -t react-app .
# docker run -p 3000:80 react-app

# ###############################################################################