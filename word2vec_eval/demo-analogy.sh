./format_data_for_word2vec_eval.py ../dataset/dataset_400_v2.csv > ./data/formatted_data_for_word2vec_eval.txt

gcc word-analogy.c -o word-analogy -lm -pthread -Ofast -march=native -Wall -funroll-loops -Wno-unused-result
./word-analogy ./data/GoogleNews-vectors-negative300.bin < ./data/formatted_data_for_word2vec_eval.txt > ./data/eval_results.csv

./word2vec_eval.py ../dataset/dataset_400_v2.csv ./data/eval_results.csv > ./data/results.csv
./word2vec_predict.py ../dataset/dataset_400_v2.csv ./data/results.csv > ./data/final_res.csv
