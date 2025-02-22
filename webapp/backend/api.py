from fastapi import FastAPI, HTTPException
import pysolr
import json
from fastapi.middleware.cors import CORSMiddleware
import gemini

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change this to specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

solr_url = "http://localhost:8983/solr/cars/" # Local Solr instance
# solr_url = "http://host.docker.internal:8983/solr/cars" # Docker Solr instance
solr = pysolr.Solr(solr_url, timeout=10)

with open("queries.json", "r") as file:
    queries = json.load(file)

@app.get("/query_solr")
async def query_solr(user_input: str):
    """
    Endpoint to accept dynamic Solr queries and parameters.
    """
    user_input = user_input.lower()
    query = None
    description_attribute = None

    try:
        if "cruise control" in user_input:
            query = queries["QUERY_1"]
            description_attribute = "Safety_Feature"
        elif "family cars" in user_input:
            query = queries["QUERY_2"]
            description_attribute = "Practicality_Feature"
        elif "smooth driving" in user_input:
            query = queries["QUERY_3"]
            description_attribute = "Driving_Feature"
        elif "modern design" in user_input:
            query = queries["QUERY_4"]
            description_attribute = "Design_Feature"
        elif "high performance" in user_input:
            query = queries["QUERY_5"]
            description_attribute = "Under_Bonnet_Feature"
        else:
            return {"error": "Please insert a valid query"}

        # Execute the Solr query
        results = solr.search(query["query"], **query["params"])

        # Add the description attribute to each document
        for doc in results.docs:
            doc["description"] = doc.get(description_attribute, "No description available")
            doc["relevant_field"] = description_attribute

        # Return response
        return {
            "num_found": results.hits,
            "docs": results.docs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_document_by_id")
async def get_document_by_id(document_id: str):
    """
    Endpoint to retrieve a specific document from Solr by its ID.
    """
    try:
        # Perform the query to get the document by ID
        results = solr.search(f"id:{document_id}")

        # Check if the document was found
        if results.hits == 0:
            return {"error": "Document not found"}

        # Return the document
        return {
            "num_found": results.hits,
            "docs": results.docs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/gemini_re_rank")
async def gemini_re_rank(query: str):
    """
    Endpoint to re-rank the cars based on a user query using the Gemini model.
    """
    try:
        # Re-rank the cars using the Gemini model
        re_ranked_cars = gemini.re_rank_cars(query)

        # Return response
        return {
            "re_ranked_cars": re_ranked_cars
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/more_like_this")
async def more_like_this(document_id: str, fields: str):
    """
    Endpoint to perform a 'More Like This' search based on a document ID.
    """
    try:
        # Build the MLT query string
        query_string = f"{{!mlt qf={fields}}}{document_id}"
        
        # Perform the MLT query with `q` as the primary argument
        results = solr.search(
            q=query_string  # Pass `q` as the main query argument
        )

        # Return response
        return {
            "num_found": results.hits,
            "docs": results.docs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))