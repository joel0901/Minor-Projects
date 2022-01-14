# KNN Classifier

Your task is to implement a kNN classifier from scratch on the Cancer dataset. The
dataset contains 9 attributes and a class label for malignant (4) and benign(2) cells.


1) You are given a train.csv and a test.csv file for the dataset. Classify each data
point in the test set into one of the two classes and compute the accuracy.

2) Do a hyperparameter search with values of k = [1,3,5,7] and distance functions
as Cosine Similarity, Euclidean Distance and Normalized Euclidean Distance.
Report the accuracy for each set of hyperparameters and choose the best
performing hyperparameters to report the best accuracy you obtain.

3) BONUS: Try to vectorize the distance computation and nearest neighbor
calculation and reduce the number of for loops in your code. One such example
is given below:

Instead of using two for loops to compute the cosine similarity of every point in the test
set with every point in the train set, you can do it using a single matrix multiplication
between the entire train set and test set using numpy and python as:

cosine_scores = numpy.dot(X_train_norm,X_test_norm)

Look for other such vectorizations and implement them, appropriate points will be
provided for every such vectorization.


## Important Points:

1) DO NOT use any machine learning library such as sklearn for the knn classifier.
You have to implement it from scratch. If found using the sklearn library you will
be awarded 0 points. You can use sklearn for accuracy calculation.

2) DO NOT copy the code. Any plagiarism found will lead to 0 points straight away
and your code or report will not be evaluated.

3) You are allowed to use libraries such as Pandas, Numpy and SciPy for data
preprocessing, distance computation and nearest neighbor calculation.
