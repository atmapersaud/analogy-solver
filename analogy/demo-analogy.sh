#~ gcc model.c -o model -lm -pthread -Ofast -march=native -Wall -funroll-loops -Wno-unused-result
#~ ./model ./data/GoogleNews-vectors-negative300.bin > ./data/GoogleNews-3M-300.bin

./analogy.py ./data/GoogleNews-3M-300.bin ../dataset/dataset_400_v2.csv > ./data/final_res.csv
