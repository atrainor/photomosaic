import csv
import sys
import os, os.path
import cv2



def main(): 

	image_path = str(sys.argv[1])
	images = []


	print "Creating Simple Index File"
	for root, dirs, files in os.walk(image_path):
	    for f in files:
	        full_path = os.path.join(root, f)
	        if os.path.splitext(full_path)[1] in ['.jpg', '.png']:
	            print "Indexing file: " + f
	            means = cv2.mean(image)[:3]
	            to_index = [full_path, means[0], means[1], means[2]]
	            images.append(to_index)


	print 'Done indexing, writing {} files to index.csv'.format(len(images))
	with open("index.csv", "wb") as index:
		writer = csv.writer(index)
		writer.writerows(images)
	print "Creating index.csv complete"            


if __name__ == "__main__":
    main()


