#!/usr/bin/python

# Script to process bounding boxes for CUB-200-2011 dataset

"""
The existing bounding box file contains entries in the following form:

<image_id> <x> <y> <width> <height>

The entries in the new file are adjusted to contain entries in the following form:

<filename> <xmin> <ymin> <xmax> <ymax>

The x and y coordinates will be normalized in order to account for varying image size

This must be done because of the necessary image resizing for feeding images into the network

Usage: process_bounding_boxes.py <dir>

where <dir> refers to the location of the file containing the original bounding box annotations and images.txt in order
to map image files to image ids
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

import numpy as np

from PIL import Image


class CUBImage:
    def __init__(self, identifier, label, file):
        self.id = identifier
        self.label = label
        self.filename = file


class Box:
    def __init__(self, identifier, x, y, width, height):
        self.id = identifier
        self.x = x
        self.y = y
        self.width = width
        self.height = height


# Read image files in from images.txt in <dir> and return as array of Image instances
def image_instances(dir):
    images_file = os.path.join(dir, 'images.txt')
    with open(images_file, 'r') as file:
        lines = file.readlines()
        images = np.array()
        for line in lines:
            img = line.split()
            id = img[0]
            desc = img[1]
            label = desc.split('/')[0]
            file = desc.split('/')[1]
            instance = CUBImage(id, label, file)
            images = np.append(images, [instance])
    return images


# Read bounding box information from bounding_boxes.txt in <dir> and return as array of Box instances
def bounding_box_instances(dir):
    bounding_box_file = os.path.join(dir, 'bounding_boxes.txt')
    with open(bounding_box_file, 'r') as file:
        lines = file.readlines()
        boxes = np.array()
        for line in lines:
            bounding_box = line.split()
            id = bounding_box[0]
            x = bounding_box[1]
            y = bounding_box[2]
            width = bounding_box[3]
            height = bounding_box[4]
            instance = Box(id, x, y, width, height)
            boxes = np.append(boxes, [instance])
    return boxes


if __name__ == '__main__':
    # Quit if invalid arguments
    if len(sys.argv) != 2:
        print('Invalid usage\n'
              'usage: process_bounding_boxes.py <dir>',
              file=sys.stderr)
        sys.exit(-1)

    directory = sys.argv[1]

    # Call methods to acquire image and bounding box instances
    images = image_instances(directory)
    boxes = bounding_box_instances(directory)

    # Create new file for bounding boxes
    bounding_box_file = os.open(os.path.join(directory, 'bounding_boxes.txt'), 'w+')

    # Make sure there is an equal number of images and bounding boxes (arrays are parallel)
    assert (len(images) == len(boxes))

    # Open the new file and calculate new information to be written
    with open(bounding_box_file, 'w') as file:
        # Iterate over image instances and create new bounding box instances with updated information
        for (image, box) in zip(images, boxes):
            image_file = os.path.join(directory, 'images', image.label, image.filename)
            img = Image.open(image_file)
            img_width, img_height = img.size

            # Calculate relative x and y coordinates for bounding box
            xmin = float(box.x) / float(img_width)
            xmax = (float(box.x) + float(box.width)) / float(img_width)
            ymin = float(box.y) / float(img_height)
            ymax = (float(box.y) + float(box.height)) / float(img_height)

            min_x = min(xmin, xmax)
            max_x = max(xmin, xmax)
            xmin_scaled = min(max(min_x, 0.0), 1.0)
            xmax_scaled = min(max(max_x, 0.0), 1.0)

            min_y = min(ymin, ymax)
            max_y = max(ymin, ymax)
            ymin_scaled = min(max(min_y, 0.0), 1.0)
            ymax_scaled = min(max(max_y, 0.0), 1.0)

            # Write updated information to new file
            file.write('%s %.4f %.4f %.4f %.4f\n' % (image.filename, xmin_scaled, ymin_scaled, xmax_scaled, ymax_scaled))
