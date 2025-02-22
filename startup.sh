#!/bin/bash

sudo docker run -p 8983:8983 --name meic_solr \
  -v ${PWD}/solr.xml:/opt/solr-9.7.0/server/solr/solr.xml \
  -v ${PWD}:/data \
  -e SOLR_JAVA_MEM="-Dsolr.max.booleanClauses=100000" \
  -d solr:9


# # Start the Solr container
# sudo docker run -p 8983:8983 --name meic_solr -v ${PWD}:/data -d solr:9

# Wait for Solr to start up before creating the core
sleep 10

# Create the collection "cars"
sudo docker exec meic_solr bin/solr create -c cars

# Wait for the collection to be fully created
sleep 5

# # Copy the solr_synonyms.txt file into the Solr container
sudo docker cp ./solr_synonyms.txt meic_solr:/var/solr/data/cars/conf/solr_synonyms.txt

# sudo docker exec meic_solr rm /var/solr/data/cars/conf/solrconfig.xml

# sudo docker cp ./solrconfig.xml meic_solr:/var/solr/data/cars/conf/solrconfig.xml

# # Create the schema 
curl -X POST -H 'Content-type:application/json' \
    --data-binary "@./schema_cars.json" \
    http://localhost:8983/solr/cars/schema

# sleep 2

# Populate the collection using `bin/solr post` instead of the deprecated `bin/post`
sudo docker exec -it meic_solr bin/solr post -c cars /data/cleaned_fixed_data.csv

# Open a terminal in the /data folder
sudo docker exec -it meic_solr /bin/bash -c "cd /data && exec /bin/bash"