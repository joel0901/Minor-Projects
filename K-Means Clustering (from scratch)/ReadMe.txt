Notes 

1. I have coded using Google Colab. Make sure to add the Iris data set to the current directory. Eg, make a directory called Clustering, and add Iris.csv to it
	!mkdir Clustering
	# Upload Iris to Clustering folder 
	#cd Clustering

2. The runtime may take about 10 - 20 seconds to run. 
3. The Results folder has the outpic pictures



Logic : 

Step 1 = We randomly assign values into the Cluster means denoted by C1_mean, C2_mean, C3_mean. 
Step 2 = We initialise three dataframes C1, C2, C3 to store the data points which are close to Cluster 1, Cluster 2 and Cluster 3 repectively. 
Step 3 = Using a for loop, we traverse all the data points in the Iris Dataset and find the distance of the data to each of the three Cluster mean values. 
Step 4 = We find the minimum of these three distances, and assign the data point to that corresponding cluster. 
Step 5 = We now find the mean of the data points in C1 and assign it to C1_mean. Similarly, we find the mean of the data points of C2 and C3 and assign it to C2_mean and C3_mean repectively. 
Step 6 = We do Step 3 to Step 5 a total of 10 times. 
Step 7 = We print the cluster means, ie, C1_mean, C2_mean and C3_mean. 
Step 8 = We now find the Jaccard distance of each cluster with the target values for each of the three clusters.

