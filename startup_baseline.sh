#!/bin/bash

# Create the collection "cars"
sudo docker exec meic_solr bin/solr create -c cars_baseline

# Wait for the collection to be fully created
sleep 5

# sudo docker exec meic_solr rm /var/solr/data/cars/conf/solrconfig.xml

# sudo docker cp ./solrconfig.xml meic_solr:/var/solr/data/cars/conf/solrconfig.xml

# # Create the schema 
curl -X POST -H 'Content-type:application/json' \
    --data-binary "@./simple_schema.json" \
    http://localhost:8983/solr/cars_baseline/schema

# sleep 2

# Populate the collection using `bin/solr post` instead of the deprecated `bin/post`
sudo docker exec -it meic_solr bin/solr post -c cars_baseline /data/cleaned_fixed_data.csv

# Open a terminal in the /data folder
sudo docker exec -it meic_solr /bin/bash -c "cd /data && exec /bin/bash"
