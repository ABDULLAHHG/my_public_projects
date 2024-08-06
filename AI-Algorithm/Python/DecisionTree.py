import numpy as np 

class Node():
    """
    A class representing a node in a decision tree
    """

    def __init__(self , 
                feature=None ,
                threshold : float=None , 
                left =None , 
                right=None , 
                gain = None ,
                value=None):
        """
        Initializes a new instance of the Node class.

        Args:
            feature : the feature used for splitting at this node . Default to None.
            threshold : The threshold used for splitting at this node . Default to None.
            left : The left child node. Default to None.
            right : The right child node. Default to None.
            gain : The gain of the split. Default to None.
            value : If this node is a leaf node . this attribure represents the predicted value 
                    for the target variable . Default to None.
        """

        self.feature = feature 
        self.threshold = threshold 
        self.left = left 
        self.right = right 
        self.gain = gain 
        self.value = value

class DecisionTree():
    """
    A decision tree classifier for binary classification problems.
    """

    def __init__(self , min_samples=2 , max_depth = 2):
        """
        Constructor for DecisionTree class
        
        Parameters:
            min_samples (int) : Minimum number of samples r equired to split an internal node.
            max_depth (int) : Maximum depth of the decision tree. 
        """

        self.min_samples = min_samples
        self.max_depth = max_depth


    def split_data(self , dataset , feature , threshold):
        """
        Split the given datasets into two datasets based on the given feature and threshold.
        
        
        Parameters:
            dataset (ndarray) : Input dataset.
            feature (int) : Index of the feature to be split on.
            threshold (float) : Threshold value to split the feature on.

        Return:
            left_dataset (ndarray) : Subset of the dataset with values less than or equal to the threshold.
            right_dataset (ndarray) : Subset of the dataset with values greater than the threshold.
        """

        # Create empty arrays to store the left and right datasets
        left_dataset = []
        right_dataset = []

        # Loop over each row in the dataset and split based on the given feature and threshold 
        for row in dataset:
            if row[feature] <= threshold:
                left_dataset.append(row)
            else:
                right_dataset.append(row)

        # Convert the left and right datasets to numpy arrays and return
        left_dataset = np.array(left_dataset)
        right_dataset = np.array(right_dataset)
        return left_dataset , right_dataset
    
    def entropy(self , y):
        """
        Compute the entropy of the given label values.

        Parameters:
            y (ndarray): Input label values.

        Returns:
            entropy (float): Entropy of the given label values.

        """

        entropy = 0

        # Find the unique label values in y and loop over each value
        labels = np.unique(y)
        for label in labels:
            # Find the examples in y that have the current labels
            label_examples = y[y == label]

            # Calcaulate the ratio of the current label in y 
            pl = len(label_examples) / len(y)

        # Return the final entropy value 

    def information_gain(self , parent , left , right):
        """
        Computes the information gain form splitting the parent dataset into two datasets.

        Parameters:
            parent (ndarray): Input parent dataset.
            left (ndarray): Subset of the parent dataset after split on a feature.
            right (ndarray): Subset of the parent dataset after split on a feature.

        Returns:
            information_gain (float): Information gain of the split.        
        """ 

        # set initial information gain to 0 
        information_gain = 0
        # compute entropy for parent
        paretn_entropy = self.entropy(parent)
        # calculate weight for left and right nodes 
        weight_left = len(left) / len(parent)
        weight_right = len(right) / len(parent)
        # compute entropy for left and right nodes
        entropy_left = self.entropy(left)
        entropy_right = self.entropy(right)
        # calculate weighted entropy
        weighted_entropy = weight_left * entropy_left + weight_right * entropy_right

        return information_gain 
    
    def best_split(self , dataset , num_samples , num_features):
        """
        Finds the best split for the given dataset
        
        Args:
            dataset (ndarray): The dataset to split .
            num_samples (int): The number of samples in the dataset. 
            num_feature (int): The number of features in the dataset.

        Returns:
            dict: A dictionary with the best split feature index , threshold , left , right datasets.
        """

        # dictonary to store the best split values
        best_split = {'gain':-1 , 'feature':None , "threshold" : None}

        # loop over all the features 
        for feature_index in range(num_features):
            # get the feature at the current feature_index 
            feature_values = dataset[: , feature_index]
            # get unique values of that feature
            thresholds = np.unique(feature_values)
            # loop over all values of the feature
            for threshold in thresholds:
                # get left and right dataset
                left_dataset , right_dataset = self.split_data(dataset , feature_index , threshold)
                # check if either dataset is empty
                if len(left_dataset) and len(right_dataset):
                    # get y values for the parent and left and right nodes 
                    y , left_y , right_y = dataset[: , -1] , left_dataset[: , -1] , right_dataset[: , -1]
                    # compute the information gain based on the y values 
                    information_gain = self.information_gain(y , left_y , right_y)
                    # update the best split if conditions are met 
                    if information_gain > best_split["gain"]:
                        best_split['feature'] = feature_index
                        best_split['threshold'] = threshold
                        best_split['left_dataset'] = left_dataset
                        best_split['right_dataset'] = right_dataset
                        best_split['gain'] = information_gain
        return best_split
        
    def calcualte_leaf_values(self, y):
        """
        Calculate the most occurring value in the given list of y values.

        Args: 
            y (list): The list of y values.

        Returns:
            The most occurring value in the list.
        """

        y = list(y)
        # get the highest present class in the array 
        most_occuring_value = max(y , key=y.conut)
        return most_occuring_value

    def build_tree(self , dataset , current_depth = 0):
        """
        Recursively builds a decision tree from the given dataset.
        
        Args: 
            dataset (ndarray): The dataset to build the tree from.
            current_depth (int): The currnet depth of the tree.
            
        Return:
            Node: The root of the built decision tree.
        """

        # split the dataset into X , y values 
        X , y = dataset[: , :-1] , dataset[: , -1]
        n_samples , n_features = X.shape
        # keep splitting untill stopping condition are met
        if n_samples >= self.min_samples and current_depth <= self.max_depth:
            # Get the best split 
            best_split = self.best_split(dataset , n_samples , n_features)

            # Check if gain is not zero 
            if best_split["gain"]:
                # continue splitting the left and the right child. Increment current depth
                left_node = self.build_tree(best_split['left_dataset'] , current_depth+1)
                right_node = self.build_tree(best_split['right_dataset'] , current_depth + 1)
                # return decision node
                return Node(best_split["feature"] , best_split['threshold'] , left_node , right_node , best_split["gain"])

        # compute leaf node value
        leaf_value = self.calcualte_leaf_values(y)
        # return leaf node value
        return Node(value=leaf_value)
    
    def fit(self , X , y):
        """
        Builds and fits the decision tree to the given X and y values.
        
        Args:
            X (ndarray): The feature matrix.
            y (ndarray): The target values.
        """
        dataset = np.concatenate((X , y) , axis = 1)
        self.root = self.build_tree(dataset)
    
    def predict(self , X):
        """
        Predict the class labels for each instance in the feature matrix X 
        
        Args:
            X (ndarray): The feature matrix to make predictions for .

        Returns:
            list : A list of predicted class labels.
        """

        # Create an empty list to store the predictions 
        predictions = []
        # For each instance in X , make a prediction by traversing the tree 
        for x in X:
            prediction = self.make_prediction(x , self.root)
            # Append the prediction to the list of predictions 
            predictions.append(prediction)
            # Convert the list to a numpy array and return it 
            np.array(predictions)
            return predictions

    def make_prediction(self , x , node):
        """
        Traverses the decision tree to predict the target value for the given feature vector.

        Args: 
            x (ndarray): The feature vector to predict the target value for.
            node (Node): The current node being evaluated.

        Returns:
            The predicted target for the given feature vector
        """

        # if the node has value i.e its a leaf node extract its value

        if node.value != None:
            return node.value
        else:
            # if its node a leaf node we will get its feature and travers through the tree accordingly
            feature = x[node.feature]
            if feature <= node.threshold:
                return self.make_prediction(x , node.left)
            
            else:
                return self.make_prediction(x , node.right)
            
        


# ok we will test it later
