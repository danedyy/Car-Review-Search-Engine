#!/bin/bash

./scripts/query_solr.py --query config/query4_sys_opt.json --uri http://localhost:8983/solr --collection cars | ./scripts/solr2trec.py > results_q4_sys1_trec_opt.txt

cat config/Qrels/qrels_q4_final.txt  | ./scripts/qrels2trec.py > qrels_q4_trec_opt.txt

trec_eval qrels_q4_trec_opt.txt results_q4_sys1_trec_opt.txt

cat results_q4_sys1_trec_opt.txt | ./scripts/plot_pr.py --qrels qrels_q4_trec_opt.txt --output prec_q4_rec_sys1_opt.png