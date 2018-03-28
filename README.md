# CPSC 8100 Project - Implementation of arxiv-1605-06217
This repository is for an implementation of the following paper: https://arxiv.org/abs/1605.06217

This project is done in part of the CPSC 8100 (Intro to AI) Spring 2018 course at Clemson University

After the repository is downloaded, we may begin with downloading and preprocessing the dataset

From the data directory, run download_and_preprocess_cub200.sh <data-dir>

This will download and format the data

### Data Directory

The data directory contains several files used in organizing and preparing the data for preprocessing

Here is a brief description of each file:

attributes.py: Grab relevant (used) attributes from attributes.txt and create an ndarray where each row represents the binary attribute vector for an image

build_cub200_data.py: Adapted from a tensorflow file, this file builds tfrecords from the data (unfinished)

download_and_preprocess_cub200.sh: bash script to download data from the web, organize the data, and perform preprocessing

download_cub200.sh: bash script to download data from web (used as component in above bash script)

partition_data.py: Create text files containing the image ids for the train, validation, and test datasets

process_bounding_boxes.py: Process entries in bounding_boxes.txt in order to scale them for varying image size

cub200_preprocessing.py: Adapted from a tensorflow file, this file performs data augmentation on the tfrecord files (unfinished)

cub200_main.py: Adapted from a tensorflow file, this file runs the resnet model on the dataset (unfinished)

### Models Directory
The models directory contains a script for downloading a pretrained ResNet-50 model

download_pretrained_resnet50.sh: bash script to download model checkpoint of pretrained ResNet-50
