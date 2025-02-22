# Car Review Search Engine

## Project Overview

This project is a comprehensive car review search engine that leverages web scraping, data cleaning, and advanced search capabilities using Solr. The project includes a backend service written in Python and a frontend application built with React. The primary goal is to provide users with an efficient and user-friendly interface to search and explore car reviews.

## Features

### Web Scraping
- **Source**: Car reviews are scraped from [CarsGuide](https://www.carsguide.com.au).
- **Script**: The web scraping is handled by [`scrape.py`](scrape.py).

### Data Cleaning
- **Process**: Cleaning involves removing HTML tags and unwanted data, and organizing the data into a structured format.
- **Script**: Data cleaning is performed by [`pri_cleaning_script.py`](pri_cleaning_script.py).

### Data Visualization
- **Plots**: Various plots are created to gain insights into the data.
- **Word Clouds**: Word clouds are generated to visualize the most frequent terms in the reviews.
- **Notebook**: Visualization is handled in [`Plots.ipynb`](Plots.ipynb).

### Solr Integration
- **Search Platform**: Solr is an open-source search platform built on Apache Lucene, used for handling large-scale search applications.
- **Configuration**: Solr configuration files include [`solr.xml`](solr.xml) and [`solrconfig.xml`](solrconfig.xml).
- **Schema**: The schema for indexing data is defined in [`schema_cars.json`](schema_cars.json) and [`schema_semantic.json`](schema_semantic.json).
- **Initialization**: Solr collections are created and populated using scripts like [`startup.sh`](startup.sh), [`startup_baseline.sh`](startup_baseline.sh), and [`startup_semantic.sh`](startup_semantic.sh).

### Solr Features
- **Full-Text Search**: Implements full-text search for car reviews.
- **Faceted Search**: Allows filtering search results based on different attributes.
- **Data Indexing**: Indexes large datasets, making it easier to search and analyze data.
- **Query Building**: Supports complex query building for efficient search.
- **More Like This (MLT)**: Finds documents similar to a given document or query.
- **Semantic Search**: Enhances search capabilities with semantic understanding.

### Backend
- **Language**: Python
- **Framework**: FastAPI
- **Solr Communication**: The backend communicates with the Solr service to fetch and rank search results.
- **Scripts**: Key scripts include [`query_solr.py`](Evaluation/scripts/query_solr.py) and [`api.py`](webapp/backend/api.py).

### Gemini Integration
- **Purpose**: The Gemini model is used for re-ranking car search results based on relevance to user queries.
- **Script**: The re-ranking functionality is implemented in [`gemini.py`](webapp/backend/gemini.py).
- **Process**: The script uses a generative AI model to re-rank cars by generating a ranking list based on the relevance of car descriptions to the user's query.

### Frontend
- **Language**: JavaScript
- **Framework**: React
- **UI Components**: The frontend includes search UI and result listing components.

## Usage

### Running the Project

1. **Backend and Frontend**:
    - Navigate to the `webapp` folder.
    - Run the following command to start the backend and frontend services:
    ```bash
    docker-compose up --build
    ```
    - Backend service will be available at `http://localhost:8000`.
    - Frontend service will be available at `http://localhost:3000`.

2. **Solr**:
    - Navigate to the folder containing the Solr script.
    - Run the Solr initialization script:
    ```bash
    ./startup.sh
    ```
    - Solr will be available at `http://localhost:8983`.

### Video Demonstration
- A video demonstration of the project can be ![found here](video/Screen-Recording.mov)
