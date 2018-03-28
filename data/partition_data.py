#!/usr/bin/python

"""
Usage: partition_data.py <dir>

where <dir> refers to the CUB-200 data directory
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import random

import numpy as np


class CUBImage:
    def __init__(self, identifier, label, file):
        self.id = identifier
        self.label = label
        self.filename = file


# Read image files in from images.txt in <dir> and return as array of Image instances
def image_instances(dir):
    images_file = os.path.join(dir, 'images.txt')
    with open(images_file, 'r') as file:
        lines = file.readlines()
        images = np.array([])
        for line in lines:
            img = line.split()
            id = img[0]
            desc = img[1]
            label = desc.split('/')[0]
            file = desc.split('/')[1]
            instance = CUBImage(id, label, file)
            images = np.append(images, [instance])
    return images


# Extract class labels from classes.txt file
def parse_classes(classes_file):
    with open(classes_file, 'r') as file:
        lines = file.readlines()
        classes = []
        for l in lines:
            c = l.split()[1]
            classes = np.append(classes, c)
    return classes


# Interpret train/test data1 set assignments
def train_test_split(split_file):
    with open(split_file, 'r') as file:
        lines = file.readlines()
        train_images = []
        test_images = []
        for l in lines:
            id, is_train = l.split()
            if is_train == '1':
                train_images.append(id)
            else:
                test_images.append(id)
        return train_images, test_images


if __name__ == '__main__':
    # Quit if invalid arguments
    if len(sys.argv) != 2:
        print('Invalid usage\n'
              'usage: partition_data.py <dir>',
              file=sys.stderr)
        sys.exit(-1)

    directory = sys.argv[1]

    # Read in all class names from classes.txt
    classes_file = os.path.join(directory, 'CUB_200_2011', 'classes.txt')
    class_names = parse_classes(classes_file)

    # Collect all image instances from images.txt
    images_file = os.path.join(directory, 'CUB_200_2011')
    images = image_instances(images_file)

    # Determine train and test datasets and create validation dataset with 10% of train dataset
    split_file = os.path.join(directory, 'CUB_200_2011', 'train_test_split.txt')
    train, test = train_test_split(split_file)
    validation = [train[i] for i in sorted(random.sample(range(len(train)), int(len(train)/10)))]
    duplicates = []
    for i in range(len(train)):
        if train[i] in validation:
            duplicates.append(train[i])
    for dup in duplicates:
        train.remove(dup)

    # Create directories for train, validation, and test
