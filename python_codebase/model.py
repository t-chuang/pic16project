import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree, preprocessing
from sklearn.model_selection import train_test_split
import numpy as np

class model:
    def __init__(self, fileName, sheetName):
        self.fileName = fileName
        self.data = pd.read_excel(fileName, sheetName)


    def trimData(self, cols):
        '''
        Trims the data to the specified columns and gets rid of zeros

        Args:
            cols - a list of column names

        Returns:
            none
        '''
        self.data = self.data[cols]

        # get rid of rows with zeros in any column
        for col in cols:
            self.data = self.data[self.data[col] != 0]


    def getData(self):
        '''
        Shows the data.

        Args:
            none

        Returns:
            data - the data
        '''
        return self.data


    def trainModel(self, targetCol, testSize, maxDepth):
        '''
        Trains a model to predict targetCol using the other columns.
        Splits test/train data with testSize and creates a decision tree with maxDepth

        Args:
            targetCol - string of the name of the target data
            testSize - 0 to 1 value for percent of test data to get
            maxDepth - determins the max amount of "layers" in the decision tree

        Returns:
            T - the decision tree
        '''
        # drops the target column from data
        self.X = self.data.drop([targetCol], axis = 1)

        # create label encoder to fit transform the target column
        le = preprocessing.LabelEncoder()
        y = le.fit_transform(self.data[targetCol])

        # split and create test/train getData
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, y, test_size = testSize)

        # create decision tree
        self.T = tree.DecisionTreeClassifier(max_depth = maxDepth)
        self.T.fit(self.X_train, self.y_train)

        return self.T

    
    def scoreTree(self):
        '''
        Shows the score of the tree for

        Args:
            none
        
        Return:
            none
        '''
        print("The score for the training data is:", self.T.score(self.X_train, self.y_train))
        print("The score for the testing data is:", self.T.score(self.X_test, self.y_test))


    def visualizeTree(self):
        '''
        Shows a visual model of the generated tree

        Args:
            none

        Return:
            none
        '''
        fig, ax = plt.subplots(1, figsize = (20, 20))
        tree.plot_tree(self.T, filled = True, feature_names = self.X.columns)


