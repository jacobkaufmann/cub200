#!/bin/bash

# Script to download CUB_200_2011 data set

# Usage: ./download_cub200.sh [dir_name]
set -e

# Set data directory to script argument
DATA_DIR="${1:-./cub200-data}"
echo "Saving downloaded files to $DATA_DIR"
mkdir -p "${DATA_DIR}"

INITIAL_DIR=$(pwd)
cd "${DATA_DIR}"

# URL to download tarball of CUB_200_2011 data set
BASE_URL="http://www.vision.caltech.edu/visipedia-data/CUB-200-2011/CUB_200_2011.tgz"

# Download and uncompress all data from CUB_200_2011 data set
CUB_200_TAR_BALL="${DATA_DIR}/cub_200.tar.gz"
echo "Downloading CUB_200_2011 data set"
wget "${BASE_URL}" -O "${CUB_200_TAR_BALL}"
echo "Uncompressing CUB_200_2011 data set"
tar xzf "${CUB_200_TAR_BALL}" -C "${DATA_DIR}"
echo "Deleting CUB_200_2011 tarball"
rm -f cub_200.tar.gz