import sys
import cv2
import os
import numpy as np
import random

# Usa o valor dos pixels como caracteristica:
def rawpixel(image, label, txt_file, X, Y):
	image = cv2.resize(image, (X,Y))
	
	indice = 0
	txt_file.write(str(label) +  " ")
	for i in range(Y):
		for j in range(X):
			if(image[i][j] > 128):
				v = 0
			else:
				v = 1		
	
			txt_file.write(str(v)+" ")
			indice = indice+1

	txt_file.write("\n")

def load_images(path_images, txt_file, X, Y):
	print ('Loading images...')
	archives = os.listdir(path_images)
	images = []
	arq = open('digits/files.txt')
	lines = arq.readlines()
	print ('Extracting dummy features')
	for line in lines:
		aux = line.split('/')[1]
		image_name = aux.split(' ')[0]
		label = line.split(' ')[1]
		label = label.split('\n')
		
		for archive in archives:
			if archive == image_name:
				image = cv2.imread(path_images +'/'+ archive, 0)
				rawpixel(image, label[0], txt_file, X, Y)

	print ('Done!')
	return images

def digits_main(file_name, X:int, Y:int):
	txt_file = open(file_name,"w")
	print ('Using matrix size:',X,'x',Y)
	load_images('digits/data', txt_file, X,Y)
	txt_file.close()

if __name__ == "__main__":
	digits_main(file_name = 'features.txt', X = 5, Y = 5)