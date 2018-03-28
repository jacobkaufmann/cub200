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
SCRATCH_DIR="${DATA_DIR}/raw-data/"
mkdir -p "${DATA_DIR}"
mkdir -p "${SCRATCH_DIR}"
cd ..
WORK_DIR="$(pwd)"

# Download the CUB 200 data
DOWNLOAD_SCRIPT="${WORK_DIR}/data/download_cub200.sh"
"${DOWNLOAD_SCRIPT}" "data/${SCRATCH_DIR}"
