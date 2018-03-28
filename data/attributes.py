#!/usr/bin/python

# Module containing method to extract relevant part attributes for CUB-200-2011 dataset and create the binary vector

"""
The existing attributes file contains 312 attributes while the authors only use a subset

The implementation is only concerned with attributes for the following parts: head, breast, wing, tail

This module contains a method to extract the necessary attributes and return binary vectors for all image instances
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np


class Attribute:
    def __init__(self, identifier, name, value):
        self.id = identifier
        self.name = name
        self.value = value


# Returns necessary attributes, takes attributes.txt file location as an argument
def attribute_list(attributes_file):
    attributes = np.array()
    with open(attributes_file, 'r') as file:
        lines = file.readlines()
        for l in lines:
            if 'wing' in l or 'breast' in l or 'head' in l or 'tail' in l:
                attr = Attribute()
                components = l.split()
                attr.id = components[0]
                attr.name = components[1].split('::')[0]
                attr.value = components[1].split('::')[1]
                attributes = np.append(attributes, [attr])
    return attributes


# Take in directory containing CUB data1 and array of image ids as well as total number of attributes (even unused)
# Returns ndarray of binary attribute vectors for each image
def attribute_vectors_for_images(dir, total_attributes):
    # Call auxiliary function to get array of relevant attributes (attributes used in algorithm)
    attributes_file = os.path.join(dir, 'attributes.txt')
    attributes = attribute_list(attributes_file)

    # Create dictionary for attribute list to quickly retrieve used attributes
    relevant_attributes = {}
    for attr in attributes:
        relevant_attributes[attr.id] = attr.name

    # ndarray for all binary attribute vectors to be returned
    image_attributes = np.ndarray(shape=(0, len(attributes)))

    # Open file containing all image attributes and build the ndarray of binary attribute vectors
    image_attributes_file = os.path.join(dir, 'CUB_200_2011', 'attributes', 'image_attribute_labels.txt')
    with open(image_attributes_file, 'r') as file:
        # Binary attribute vector to append to ndarray
        attr_vec = np.array()

        # Counter to keep track of when to append current vector and clear it for next image
        counter = 1

        # Read through file, updating the binary attribute vector and appending to the ndarray upon reaching new image
        lines = file.readlines()
        for l in lines:
            # If all attributes for image covered, append current vector to ndarray and clear the vector
            if counter > total_attributes:
                assert(len(attr_vec == len(attributes)))
                image_attributes = np.concatenate((image_attributes, attr_vec), axis=0)
                attr_vec = np.array()

            # Extract relevant attribute information from line
            entry = l.split()
            attr_id = entry[1]
            is_present = entry[2]

            # Append the presence of the current attribute to the binary vector if it is a relevant attribute
            if attr_id in relevant_attributes:
                attr_vec = np.append(attr_vec, is_present)
            counter += 1
    return image_attributes
