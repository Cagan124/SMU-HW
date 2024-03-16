# Module 21 Analysis

## Overview
The purpose of this assignment is to create a Neural Network model that can help a foundation select applicants for funding

## Results
Before replacing the application types and classification columns for my targets and features, I removed the name and EIN columns as they were not beneficial. 

For the first model I had 3 layers: The first with 5 neurons, second with 3 neurons and third with 1 neuron. 
I also had 3 activation functions; 2 relu and 1 sigmoid.

For the second model I had 4 layers: The first with 15 neurons, second with 7 neurons, third with 5 neurons and the last with 1 neuron.
This model had 4 activation functions: 3 relu and 1 sigmoid.

For the third model, I stayed with 4 layers but added neurons to the first 2 layers. The first layer had 20 neurons, the second had 10, the third had 5 and the fourth had 1. 
This model had 4 activation functions: 3 relu and 1 sigmoid.

For my fourth and final Neural Network model I decided to add a 5th hidden layer. The first had 20 neurons, the second had 15, the third had 7, the fourth had 3 and the fifth had 1.
This model had 5 activation functions: 4 relu and 1 sigmoid.

I ran all of these models with 500 epochs.

I also added a Random Forest model and Linear Regression model to compare to my models. 

Overall, none of the models were able to achieve the 75% accuracy score, with model #4 coming the closest with a 73.14% accuracy score. As stated above, I attempted to improvve my the performance of the models by adding layers and neurons. 

## Summary
With all of the models scoring in the 72-73% accuracy range, I would not recommend these models. However, I do believe that leaving the Name column in the dataset could possiby boost the performance. There is also a chance that Model #4 could reach the target goal if modified. It is interesting to see how the models perform based on slight modification to the neurons, layers and functions. 

