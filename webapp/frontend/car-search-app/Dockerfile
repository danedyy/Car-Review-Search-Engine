# Frontend Dockerfile
FROM node:18

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy application code
COPY . .

# Run Next.js app
CMD ["npm", "run", "dev"]
