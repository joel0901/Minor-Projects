The folders have the corresponding pics and ipynb files for

1. MNIST dataset 
2. CIFAR10 dataset

We will be using 2 different optimisers for both the Dataset to see the effect on the accuracy. 
The ones used for MNIST are : 
1. SGD
2. AdamW

The ones used for CIFAR10 are :
1. SGD
2. Adam

We will be using 3 different learning rates on all the datsets. The ones used are :

1. Lr = 0.001
2. Lr = 0.005
3. Lr = 0.01


Conclusions :
1. We see that, there is no direct correlation between learning rate and accuracy, but it depends on the optimiser too. 
2. For both the datasets, for the SGD classifier, as the learning rate increases, the accuracy increases. But there will be a upper limit beyond which it will start decreasing. 
3. For both datasets, Adam and AdamW have an inverse relation between learning rate and accuracy