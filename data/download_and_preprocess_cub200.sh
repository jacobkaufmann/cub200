#!/bin/bash

# Script to download and preprocess CUB_200_2011 data set

# Usage: ./download_and_preprocess_cub200.sh [data-dir]
set -e

if [ -z "$1"]; then
    echo "Usage: ./download_and_preprocess_cub200.sh [data-dir]"
    exit
fi

# Create the output directories
DATA_DIR="${1%/}"
SCRATCH_DIR="${DATA_DIR}/raw-data"
mkdir -p "${DATA_DIR}"
mkdir -p "${SCRATCH_DIR}"
WORK_DIR="$(pwd)"

# Download the CUB 200 data
DOWNLOAD_SCRIPT="${WORK_DIR}/download_cub200.sh"
"${DOWNLOAD_SCRIPT}" "${SCRATCH_DIR}"

CUB_DIR="${SCRATCH_DIR}/CUB_200_2011"

echo "Converting bounding box values."
BOUNDING_BOX_SCRIPT="${WORK_DIR}/process_bounding_boxes.py"
BOUNDING_BOX_FILE="${CUB_DIR}/bounding_boxes.txt"
IMAGES_FILE="${CUB_DIR}/images.txt"
python "${BOUNDING_BOX_SCRIPT}" "${BOUNDING_BOX_FILE}" "${IMAGES_FILE}"

echo "Finished downloading and preprocessing the CUB-200-2011 data."

echo "Building TF Record files from raw data"
# Build the TFRecords version of the CUB-200-2011 data.
BUILD_SCRIPT="${WORK_DIR}/build_cub200_data.py"
OUTPUT_DIRECTORY="${DATA_DIR}"
IMAGES_DIRECTORY="${CUB_DIR}/images"
CLASSES_FILE="${CUB_DIR}/classes.txt"
DATA_SPLIT_FILE="${CUB_DIR}/train_test_split.txt"

# Make directories for training and validation datasets
TRAIN_DIRECTORY="${OUTPUT_DIRECTORY}/train"
VAL_DIRECTORY="${OUTPUT_DIRECTORY}/validation"

mkdir -p "${TRAIN_DIRECTORY}"
mkdir -p "${VAL_DIRECTORY}"

chmod +x "${BUILD_SCRIPT}"

"${BUILD_SCRIPT}" \
  --images_directory="${IMAGES_DIRECTORY}" \
  --output_directory="${OUTPUT_DIRECTORY}" \
  --classes_file="${CLASSES_FILE}" \
  --bounding_boxes_file="${BOUNDING_BOX_FILE}" \
  --data_split_file="${DATA_SPLIT_FILE}" \
  --images_file="${IMAGES_FILE}"

echo "Finished building TF Record files from raw data"
