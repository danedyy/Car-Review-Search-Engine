#!/bin/bash

./scripts/query_solr.py --query config/query5_sys.json --uri http://localhost:8983/solr --collection cars_baseline | ./scripts/solr2trec.py > results_q5_sys1_trec.txt

cat config/Qrels/qrels_q5_final.txt  | ./scripts/qrels2trec.py > qrels_q5_trec.txt

trec_eval qrels_q5_trec.txt results_q5_sys1_trec.txt

cat results_q5_sys1_trec.txt | ./scripts/plot_pr.py --qrels qrels_q5_trec.txt --output prec_q5_rec_sys1.png