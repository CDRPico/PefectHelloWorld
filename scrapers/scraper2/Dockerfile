# Dockerfile for Scraper1

# Use a Node.js image
FROM node:latest

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Install Playwright dependencies
RUN npx playwright install
RUN npx playwright install-deps

# Copy your TypeScript scraper script and tsconfig.json
COPY scraper2.ts .
COPY tsconfig.json .

# Compile TypeScript to JavaScript
RUN npx tsc scraper2.ts

# Command to run the scraper
CMD ["node", "scraper2.js"]
