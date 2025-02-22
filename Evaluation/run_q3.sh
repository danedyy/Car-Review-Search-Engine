#!/bin/bash

./scripts/query_solr.py --query config/query_sys3.json --uri http://localhost:8983/solr --collection cars | ./scripts/solr2trec.py > results_sys3_trec.txt

cat config/qrels.txt | ./scripts/qrels2trec.py > qrels_trec3.txt

trec_eval qrels_trec3.txt results_sys3_trec.txt