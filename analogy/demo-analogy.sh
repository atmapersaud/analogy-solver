#~ gcc model.c -o model -lm -pthread -Ofast -march=native -Wall -funroll-loops -Wno-unused-result
#~ ./model ./data/GoogleNews-vectors-negative300.bin > ./data/GoogleNews-3M-300.bin

./analogy.py ./data/GoogleNews-3M-300.bin ../dataset/dataset_400_v2.csv > ./data/final_res_v2.csv
./analogy.py ./data/GoogleNews-3M-300.bin ../dataset/dataset_v3.1.csv > ./data/final_res_v3.1.csv

./analogy-pos.py ./data/postag-vec.bin ../dataset/dataset_400_v2.csv > ./data/posres_v2.csv
./analogy-pos.py ./data/postag-vec.bin ../dataset/dataset_v3.1.csv > ./data/posres_v3.1.csv
