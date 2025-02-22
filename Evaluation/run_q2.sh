#!/bin/bash

./scripts/query_solr.py --query config/query2_sys.json --uri http://localhost:8983/solr --collection cars_baseline | ./scripts/solr2trec.py > results_q2_sys1_trec.txt

cat config/Qrels/qrels_q2_final.txt  | ./scripts/qrels2trec.py > qrels_q2_trec.txt

trec_eval qrels_q2_trec.txt results_q2_sys1_trec.txt

cat results_q2_sys1_trec.txt | ./scripts/plot_pr.py --qrels qrels_q2_trec.txt --output prec_q2_rec_sys1.png