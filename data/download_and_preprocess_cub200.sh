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
WORK_DIR="$0.runfiles/arxiv_1605_06217/arxiv_1605_06217"

