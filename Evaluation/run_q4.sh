#!/bin/bash

./scripts/query_solr.py --query config/query4_sys.json --uri http://localhost:8983/solr --collection cars_baseline | ./scripts/solr2trec.py > results_q4_sys1_trec.txt

cat config/Qrels/qrels_q4_final.txt  | ./scripts/qrels2trec.py > qrels_q4_trec.txt

trec_eval qrels_q4_trec.txt results_q4_sys1_trec.txt

cat results_q4_sys1_trec.txt | ./scripts/plot_pr.py --qrels qrels_q4_trec.txt --output prec_q4_rec_sys1.png