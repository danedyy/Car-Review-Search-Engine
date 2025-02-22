#!/bin/bash

./scripts/query_solr.py --query config/query_sys1.json --uri http://localhost:8983/solr --collection cars | ./scripts/solr2trec.py > results_sys1_trec.txt

cat config/qrels.txt | ./scripts/qrels2trec.py > qrels_trec.txt

trec_eval qrels_trec.txt results_sys1_trec.txt