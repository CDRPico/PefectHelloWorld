# Dockerfile for Scraper1

# Use a Node.js image
FROM node:latest

# Set the working directory
WORKDIR /app

RUN apt-get update

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Install Playwright dependencies
RUN npx playwright install
RUN npx playwright install-deps

# Copy your TypeScript scraper script and tsconfig.json
COPY scraper1.ts .
COPY tsconfig.json .

# Compile TypeScript to JavaScript
RUN npx tsc scraper1.ts

# Command to run the scraper
CMD ["node", "scraper1.js"]
