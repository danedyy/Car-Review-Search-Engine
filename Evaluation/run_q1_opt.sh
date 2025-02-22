#!/bin/bash

./scripts/query_solr.py --query config/query_sys1_opt.json --uri http://localhost:8983/solr --collection cars | ./scripts/solr2trec.py > results_sys1_trec_opt.txt

cat config/qrels.txt | ./scripts/qrels2trec.py > qrels_trec_opt.txt

trec_eval qrels_trec_opt.txt results_sys1_trec_opt.txt