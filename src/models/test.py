



# Importing libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.simplefilter('ignore')

from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

file_path = os.path.dirname('__file__')

def test_comparative(df):
    
    
    """" Getting the features and the target variable from the dataframe """
    x_variable = df.iloc[:,0:-1]
    y_variabel = df.iloc[:,-1:]

    
    """" Split the data into train and test subsets """
    x_train, x_test, y_train, y_test = train_test_split(x_variable, y_variabel, test_size=0.25)


    """" Initializing the three different models used on the comparative """
    dummy_model_stratify = DummyClassifier(strategy='stratified').fit(x_train,y_train)
    dummy_model_stratify_accuracy = (dummy_model_stratify.score(x_test,y_test)*100).round(2)


    dummy_model_most_freq = DummyClassifier(strategy='most_frequent').fit(x_train,y_train)
    dummy_model_most_freq_accuracy = (dummy_model_most_freq.score(x_test,y_test)*100).round(2)


    linear_svc = LinearSVC().fit(x_train, y_train)
    linear_svc_accuracy = (linear_svc.score(x_test,y_test)*100).round(2)


    decision_tree_model = DecisionTreeClassifier(max_depth=3).fit(x_train, y_train)
    decision_tree_model_accuracy = (decision_tree_model.score(x_test,y_test)*100).round(2)

    """" Return a dataframe comparing the four models accuracy """
    accuracy_df_comparative_test = pd.DataFrame([[dummy_model_stratify_accuracy],[dummy_model_most_freq_accuracy],[linear_svc_accuracy],[decision_tree_model_accuracy]], index = ['Dummy_Stratify', 'Dummy_Most_Freq','LinearSVC','DecisionTreeClassifier'], columns=['Model Accuracy'])
    
    return accuracy_df_comparative_test

def main():
    df = pd.read_csv(os.path.join(file_path, os.pardir, '../data/processed/processed.csv'))

    model_comparative = test_comparative(df)
    print(model_comparative)

if __name__ == '__main__':
    main()