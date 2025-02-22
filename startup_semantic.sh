sudo docker exec meic_solr bin/solr delete -c cars_semantic

# Create the collection "cars"
sudo docker exec meic_solr bin/solr create -c cars_semantic

# Wait for the collection to be fully created
sleep 5

# # Copy the solr_synonyms.txt file into the Solr container
sudo docker cp ./solr_synonyms.txt meic_solr:/var/solr/data/cars_semantic/conf/solr_synonyms.txt

# sudo docker exec meic_solr rm /var/solr/data/cars/conf/solrconfig.xml

# sudo docker cp ./solrconfig.xml meic_solr:/var/solr/data/cars/conf/solrconfig.xml

# # Create the schema 
curl -X POST -H 'Content-type:application/json' \
    --data-binary "@./schema_semantic.json" \
    http://localhost:8983/solr/cars_semantic/schema

# sleep 2

# Populate the collection using `bin/solr post` instead of the deprecated `bin/post`
sudo docker exec -it meic_solr bin/solr post -c cars_semantic /data/final.json

# Open a terminal in the /data folder
sudo docker exec -it meic_solr /bin/bash -c "cd /data && exec /bin/bash"