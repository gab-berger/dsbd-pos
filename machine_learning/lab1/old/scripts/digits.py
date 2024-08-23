import sys
import cv2
import os
import numpy as np
import random

# Usa o valor dos pixels como caracteristica:
def rawpixel(image, label, X, Y):
	image = cv2.resize(image, (X,Y))

	indice = 0
	image_string = str(label)+" "
	for i in range(Y):
		for j in range(X):
			if(image[i][j] > 128):
				v = 0
			else:
				v = 1		
	
			image_string += str(v)+" "
			indice = indice+1
	
	image_string += "\n"
	return image_string

def gen_img_matrix(path_images, X, Y):
	img_matrix = ''
	archives = os.listdir(path_images)
	arq = open('digits/files.txt')
	lines = arq.readlines()
	for line in lines:
		aux = line.split('/')[1]
		image_name = aux.split(' ')[0]
		label = line.split(' ')[1]
		label = label.split('\n')
		
		for archive in archives:
			if archive == image_name:
				image = cv2.imread(path_images +'/'+ archive, 0)
				img_matrix += rawpixel(image, label[0], X, Y)
	print ('\n>>>>>>>>>>>>>>>>>>>> MATRIX',X,'x',Y,'<<<<<<<<<<<<<<<<<<<<\n')
	return img_matrix

if __name__ == "__main__":
	gen_img_matrix(path_images = 'digits/data', X = 5, Y = 5)