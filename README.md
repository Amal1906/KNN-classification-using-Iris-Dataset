# 1)Loading the Dataset
  The Iris dataset is used, which contains three classes of flowers (setosa, versicolor, virginica) with four features each. 
# 2)Splitting the Data
  The dataset is divided into training (80%) and testing (20%) subsets using train_test_split().
# 3)Training the KNN Model
  The model stores the training data and labels without making assumptions about the data distribution.
# 4)Making Predictions
  For a given test sample, the Euclidean distance to all training samples is computed.
  The k closest training samples are selected.
  A majority vote determines the predicted class.
# 5)Evaluating the Model
  The predictions are compared with the actual labels to compute the classification accuracy.
# 6)Results and Visualization
  The dataset is visualized using scatter plots to show the distribution of classes.
  
# The accuracy of the model is calculated as:

Accuracy=(Correct Predictions/Total Predictions)×100

A confusion matrix can be used to analyze the model’s performance further.
