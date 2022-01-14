# KNN Classifier

1. Train a neural network for classification of Sea snail data
(refer ‘Snail.csv’) to predict the gender of the sea snail. It
has three classes ‘Male(M)’ , ‘Female(F)’ & ‘Both(I)’ . The
dataset contains eight features for each sample: Length,
Diameter, Height, Whole-weight, Shucked-weight, Viscera
weight, Shell-weight, rings.
 Design a neural network with the following parameters:
 No. of hidden layers: 1 (with maximum upto 8
nodes)
 Sigmoid activation function for both hidden layer
and output layer
Sigmoid function is given as, 􀬵
􀬵􀬾􀯘􀰷􀳣
 Learning rate: 0.01
 Cost function: 􀬵
􀬶 􀯞 􀯞 􀯞
􀬶, where ok is
calculated output and tk is the target output.
Implement neural network with functions for forward
propagation, error calculation, back propagation and
weight update upto 500 iterations.
(Do not use in-built functions or toolboxes for forward
propagation, gradient calculation and back
propagation)
After training, classify the following samples:
[100 50 20 55.5 42 23 35 11]
[110 74 25 153.6 47.4 15.5 11 10]
[106 73 16 70.3 47.4 29.9 33 19]
[94 81 20 132.9 33.5 34.2 38 10]
(Note: Do not forget to normalize the data)
 Cost vs epoch for the training data using the Neural
Network classifier built.
 Plot to visualise the input values before and after
normalisation of training data.
 Predicted output values and the gender associated for
the test data.
 Calculate the accuracy for the test and training data
for different values of epoch.
