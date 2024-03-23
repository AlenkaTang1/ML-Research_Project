# On going research project on sequence classification
- Research project on finding the optimal model for sequence data classification in bioinformatics.
- implemented with assumption that sequences with similar subsequences have similar functionalities.
- Constructing de-Bruijn graphs for each sequence data (DNA, virus protein strand) with different kmers then using Node2vec and Graph2vec embedding models to extract the features for each sequence.
- Feeding the vectors to Support Vector Machine and Neural Network classifiers while testing different C and gamma values for SVM and convolutional NN with different activation functions.


-- -- 
- graph_list pickle file consists a list of constructed de-bruijn graphs from the DNA sequence data with kmer = 4.
- The graphs are later converted to a list of dictionaries with each node being the key as well as features for training the classifiers.
