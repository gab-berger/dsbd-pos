#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

import sys
import numpy as np
import pandas as pd
import io
import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from old.scripts.digits import gen_img_matrix


def main(img_matrix):
        data = np.genfromtxt(io.StringIO(img_matrix))
        X_data = data[:, 1:]
        y_data = data[:,0]

        X_train, X_test, y_train, y_test =  train_test_split(X_data, y_data, test_size=0.5, random_state = 5)

        # cria um kNN
        neigh = KNeighborsClassifier(n_neighbors=3, metric='euclidean')

        neigh.fit(X_train, y_train)

        # predicao do classificador
        y_pred = neigh.predict(X_test)

        # mostra o resultado do classificador na base de teste
        print ('Accuracy: ',  neigh.score(X_test, y_test))

        # cria a matriz de confusao
        cm = confusion_matrix(y_test, y_pred)
        #print (cm)
        #print(classification_report(y_test, y_pred))

        return neigh.score(X_test, y_test)

if __name__ == "__main__":
        big_start_time = time.time()
        df = pd.DataFrame(columns=['knum', 'x', 'y', 'acc', 'time'])
        
        for knum in range(3, 4, 2):
                print('==================== KNUM =',str(knum),'====================')
                for x in range(10,51,10):
                        for y in range(10,51,10):
                                start_time = time.time()
                                img_matrix = gen_img_matrix(path_images = 'digits/data', X = x, Y = y)  
                                acc = main(img_matrix)

                                end_time = time.time()
                                elapsed_time = round(end_time - start_time, 4)
                                
                                new_row = pd.DataFrame({'knum': [knum], 'x': [x], 'y': [y], 'acc': [acc], 'time': [elapsed_time]})
                                df = pd.concat([df, new_row], ignore_index=True)

        print(df.sort_values(by='acc',ascending=False).head(20))
        df.to_csv('prediction_results_v1.csv', index=False, sep=',')

        big_end_time = time.time()
        elapsed_time = big_end_time - big_start_time
        print(f"Tempo decorrido: {elapsed_time} segundos")