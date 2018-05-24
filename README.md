## CUB 200 Data Processing
This repository contains preprocessing scripts for the CUB 200 Birds Dataset to be used for computer vision AI tasks

### Data Directory

The data directory contains several files used in organizing and preparing the data for preprocessing

Here is a brief description of each file:

attributes.py: Grab relevant (used) attributes from attributes.txt and create an ndarray where each row represents the binary attribute vector for an image

build_cub200_data.py: Adapted from a tensorflow file, this file builds tfrecords from the data (unfinished)

download_and_preprocess_cub200.sh: bash script to download data from the web, organize the data, and perform preprocessing

download_cub200.sh: bash script to download data from web (used as component in above bash script)

partition_data.py: Create text files containing the image ids for the train, validation, and test datasets

process_bounding_boxes.py: Process entries in bounding_boxes.txt in order to scale them for varying image size
