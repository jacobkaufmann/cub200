import os
import sys
import numpy as np


# Extract class labels from classes.txt file
def parse_classes(classes_file):
    with open(classes_file, 'r') as file:
        lines = file.readlines()
        classes = []
        for l in lines:
            c = l.split()[1].split('.')[1]
            classes = np.append(classes, c)
    print(len(classes))
    return classes


# Create tuples of image id, class label, and image file
def image_instances(images_file):
    with open(images_file, 'r') as file:
        lines = file.readlines()
        instances = []
        for l in lines:
            img = l.split()
            id = img[0]
            desc = img[1]
            label = int(desc.split('.')[0])
            file = desc.split('/')[1]
            instance = (id, label, file)
            instances = np.append(instances, instance)
    return instances


# Intepret train/test data set assignments
def train_test_split(split_file):
    with open(split_file, 'r') as file:
        lines = file.readlines()
        train_images = []
        test_images = []
        for l in lines:
            id, is_train = l.split()
            if is_train == '1':
                train_images = np.append(train_images, id)
            else:
                test_images = np.append(test_images, id)
        return train_images, test_images



# Call function to define classes
# parse_classes('/Users/jacobkaufmann/Dropbox/Projects/arxiv_1605_06217_aux/data/CUB_200_2011/CUB_200_2011/classes.txt')
# print(image_instances('/Users/jacobkaufmann/Dropbox/Projects/arxiv_1605_06217_aux/data/CUB_200_2011/CUB_200_2011/images.txt')[0])
train, test = train_test_split('/Users/jacobkaufmann/Dropbox/Projects/arxiv_1605_06217_aux/data/CUB_200_2011/CUB_200_2011/train_test_split.txt')
print('train: ', len(train))
print('test: ', len(test))
