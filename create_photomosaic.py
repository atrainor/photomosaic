import csv
import sys
import os, os.path
import cv2
import pandas as pd
import numpy as np



def process_image(image, size):

	img = cv2.imread(image)
	resized = cv2.resize(img, (size,size))
	name = os.path.splitext(image)[0].split('/')[1]
	resized_folder = 'resized_' + str(size) + '/' + name + os.path.splitext(image)[1]
	print resized_folder
	cv2.imwrite(resized_folder, resized)
	return resized

def read_index():

	image_df = pd.read_csv('index.csv', 
		names = ["path", "B", "G", "R"])
	return image_df

def create_advanced_index(size, image_path):

	if not os.path.exists('resized_' + str(size) + '/'):
			os.makedirs('resized_' + str(size) + '/' )


	print "Creating Advanced Index File and Folder"
	images = []
	for root, dirs, files in os.walk(image_path):
	    for f in files:
	        full_path = os.path.join(root, f)
	        if os.path.splitext(full_path)[1] in ['.jpg', '.png']:
	            print "Indexing file: " + f
	            image = process_image(full_path, size)
	            to_index = ['resized_' + str(size) + '/' + f, image]
	            images.append(to_index)

	df = pd.DataFrame(images)
	df.columns = ['path', 'pixels']
	return images




def resize_input(image, size):
	img = cv2.imread(image)

	height, width, pix = img.shape
	#make it compatable with size of tile!
	resized = cv2.resize(img, (width / size * size, height / size * size)) 
	cv2.imwrite(image, resized)
	return resized

def find_best_match(means, index):
	index['r_diff'] = (index['R'] - means[2])**2
	index['g_diff'] = (index['G'] - means[1])**2
	index['b_diff'] = (index['B'] - means[0])**2
	index['diff'] = (index['b_diff'] + index['g_diff'] + index['r_diff']) ** .5
	df = index.sort_values(by=['diff'], ascending=1)
	return df['path'].iloc[0]

def resize_match(image, size):
	img = cv2.imread(image)
	resized = cv2.resize(img, (size,size))
	return resized



def create_simple_mosaic(image, index, size):
	height, width, pix = image.shape

	print "Starting replacement"
	for i in range(0, height / size):
		for j in range(0, width / size):
			to_replace = image[(i * size):((i + 1) * size), (j * size):((j + 1) * size)]
			means = list(cv2.mean(to_replace)[:3])
			best_match = find_best_match(means, index)
			resized_match = resize_match(best_match, size)
			image[(i * size):((i + 1) * size), (j * size):((j + 1) * size)] = resized_match
			cv2.imshow("Progress", image)
        	cv2.waitKey(1)

	return image

def find_best_advanced_match(replace, index):
	diff_list = []
	for image in index:
		image_array = np.float64(image[1])
		rep = np.float64(replace)
		diff = np.linalg.norm(image_array - rep)
		diff_list.append(diff)
	min_index = diff_list.index(min(diff_list))
	return index[min_index][1]



def create_advanced_mosaic(image,index, size):
	height, width, pix = image.shape

	print "Starting replacement"
	for i in range(0, height / size):
		for j in range(0, width / size):
			to_replace = image[(i * size):((i + 1) * size), (j * size):((j + 1) * size)]
			best_match = find_best_advanced_match(to_replace, index)
			image[(i * size):((i + 1) * size), (j * size):((j + 1) * size)] = best_match
			cv2.imshow("Progress", image)
        	cv2.waitKey(1)
	return image
			



def main():

	input_image = sys.argv[1]
	tile_size = int(sys.argv[2])
	method = sys.argv[3]

	resized_input = resize_input(input_image, tile_size)

	if method == 'simple': 
		index_df = read_index()

		final_image = create_simple_mosaic(resized_input, index_df, tile_size)
		write_to = "simple_mosaic_" + str(tile_size) + input_image
		print "Final mosaic written to {}".format(write_to)
		cv2.imwrite(write_to,  final_image)

	elif method =='advanced':

		image_path = sys.argv[4]

		index_df = create_advanced_index(tile_size, image_path)
		final_image = create_advanced_mosaic(resized_input, index_df, tile_size)
		write_to = "advanced_mosaic_" + str(tile_size) +  input_image
		print "Final mosaic written to {}".format(write_to)
		cv2.imwrite(write_to,  final_image)

		
		#final_image = create_advanced_mosaic(resized_input, tile_size)
		

	else:
		print "Choose either simple or advanced method"


	


if __name__ == "__main__":
    main()
