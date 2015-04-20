gcc model.c -o model -lm -pthread -Ofast -march=native -Wall -funroll-loops -Wno-unused-result
./model ./data/GoogleNews-vectors-negative300.bin > ./data/GoogleNews-3M-300.bin
