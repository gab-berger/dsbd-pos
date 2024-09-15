#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

import sys
import numpy as np
import pandas as pd
import time

from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.metrics import confusion_matrix 
from sklearn.datasets import load_svmlight_file

from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB 
from sklearn.linear_model import Perceptron

def load_data():
	print ("Loading data...")
	X_train, y_train = load_svmlight_file('train.txt')
	X_test, y_test = load_svmlight_file('test.txt')
	dataset = [X_train, y_train, X_test, y_test]
	print('...data loaded!')
	return dataset

def get_classifier(method, **kwargs):
    method = method.strip().lower()
    if method == 'knn':
        classifier = KNeighborsClassifier(**kwargs)
    elif method == 'logreg':
        classifier = linear_model.LogisticRegression(**kwargs)
    elif method == 'gauss':
        classifier = GaussianNB(**kwargs)
    elif method == 'lindisc':
        classifier = LinearDiscriminantAnalysis(**kwargs)
    else:
        raise ValueError(f"Método inválido: '{method}'. Escolha entre ['KNN', 'LogReg', 'Gauss', 'LinDisc'].")
    return classifier

def train_test_data(dataset:list, classifier_str, batchsize:int):
	start_time = time.time()
	classifier = get_classifier(classifier_str)
	
	X_train, y_train, X_test, y_test = dataset[0], dataset[1], dataset[2], dataset[3]
	X_train = X_train[0:batchsize].copy()
	y_train = y_train[0:batchsize].copy()
	
	X_train_dense = X_train.toarray()
	classifier.fit(X_train_dense, y_train)

	X_test_dense = X_test.toarray()
	y_pred = classifier.predict(X_test_dense) 
	
	acc = round(classifier.score(X_test_dense, y_test) * 100, 4)
	cm = confusion_matrix(y_test, y_pred)    
	total_time = round(time.time() - start_time, 4)
    
	print(f'[{classifier_str}] [{batchsize}] trained in {total_time}s -> acc = {acc}%')
	return [classifier_str, int(batchsize), float(total_time), float(acc), cm]

if __name__ == "__main__":
	batchsize = 1000

	dataset = load_data()
	train_full_size = dataset[0].shape
	methods = ['KNN','LogReg','Gauss','LinDisc']
	
	results = []
	for method in methods:
		current_batchsize = batchsize
		while(current_batchsize <= train_full_size[0]):
			result = train_test_data(dataset, method, current_batchsize)
			results.append(result)
			current_batchsize = current_batchsize + batchsize
    
	processed_results = []
	for result in results:
		classifier_str, batchsize, total_time, acc, cm = result
		cm_list = cm.tolist() if hasattr(cm, 'tolist') else cm
		processed_results.append([classifier_str, batchsize, total_time, acc, cm_list])
	df = pd.DataFrame(processed_results, columns=['Classifier', 'BatchSize', 'TotalTime', 'Accuracy', 'ConfusionMatrix'])
	
	df = df.sort_values(by='Accuracy',ascending=False)
	print(df.head())
	df.to_csv('resultados_classificadores.csv', index=False)