#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

import sys
import numpy as np
import pandas as pd
import io
import time
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor, as_completed
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from old.scripts.digits import gen_img_matrix


def main(img_matrix, knn_met):
        data = np.genfromtxt(io.StringIO(img_matrix))
        X_data = data[:, 1:]
        y_data = data[:,0]

        X_train, X_test, y_train, y_test =  train_test_split(X_data, y_data, test_size=0.5, random_state = 5)

        # cria um kNN
        neigh = KNeighborsClassifier(n_neighbors=3, metric=knn_met)

        neigh.fit(X_train, y_train)

        # predicao do classificador
        y_pred = neigh.predict(X_test)

        # mostra o resultado do classificador na base de teste
        acc = neigh.score(X_test, y_test)

        # cria a matriz de confusao
        #cm = confusion_matrix(y_test, y_pred)
        #print (cm)
        #print(classification_report(y_test, y_pred))

        return acc

def processa_combinacao(knn_met, knum, img_matrix, x, y):
        start_time = time.time()
        print('START',knn_met,'k',knum,'...')

        acc = main(img_matrix, knn_met)
        
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)
        print ('DONE',knn_met,'k',knum,'|',elapsed_time,'s | acc:',acc)
    
        return {'knn_met': knn_met,'knum': knum, 'x': x, 'y': y, 'acc': acc*1000, 'time': elapsed_time}

if __name__ == "__main__":
        big_start_time = time.time()
        knn_met_list = [
                'minkowski',
                'euclidean',
                'manhattan',
                #'chebyshev'
        ]

        with ProcessPoolExecutor(max_workers=12) as executor:
                futures = []
                for x in range(60, 61, 1):
                        for y in range(25, 26, 1):
                                img_matrix = gen_img_matrix(path_images='digits/data', X=x, Y=y)
                                for metric in knn_met_list:
                                        for knum in range(3, 4, 2):
                                                futures.append(executor.submit(processa_combinacao, metric, knum, img_matrix, x, y))

                results = []
                for future in as_completed(futures):
                        results.append(future.result())
        
        df = pd.DataFrame(results)
        for column in ['knum','x','y','acc','time']:
                df[column] = pd.to_numeric(df[column],errors='coerce')
        df = df.sort_values(by=['acc','time'], ascending=[False,True])

        print(df.head(20))
        print(df.tail(20))

        final_time = datetime.now().strftime('%Y%m%d_%H%M')
        df.to_csv('prediction_results_'+final_time+'.csv', index=False, sep=',')

        big_end_time = time.time()
        elapsed_time = big_end_time - big_start_time
        print(f"Tempo decorrido: {elapsed_time} segundos")