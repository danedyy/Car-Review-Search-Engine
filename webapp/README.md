# Project Setup and Instructions

## How to Run the Project

This project consists of a backend, a frontend, and a Solr instance. Follow the steps below to set it up and run it:

---

### **Step 1: Run the Project with Docker Compose**

1. Open a terminal and navigate to the `webapp` folder.
2. Run the following command to start the backend and frontend services:

    ```bash
    docker-compose up --build
    ```
This will:
- Start the backend service on `http://localhost:8000`.
- Start the frontend service on `http://localhost:3000`.

### **Step 2: Run Solr**

1. Open another terminal and navigate to the folder where your Solr script is located.
2. Run the Solr initialization script as you would normally:

    ```bash
    ./startup.sh
    ```
This will:
- Start the Solr container on `http://localhost:8983`.
- Create and configure the cars core.
- Populate Solr with the required data.