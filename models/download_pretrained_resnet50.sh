#!/bin/bash

# Script to download pretrained ResNet-50 model

# Usage: ./download_pretrained_resnet50.sh [dir_name]
set -e

if [ -z "$1"]; then
    echo "Usage: ./download_pretrained_resnet50.s [model-dir]"
    exit
fi

# Set data directory to script argument
OUTDIR="${1}"
echo "Saving downloaded files to $OUTDIR"
mkdir -p "${OUTDIR}"

INITIAL_DIR=$(pwd)
cd "${OUTDIR}"

# URL to download tarball of pretrained ResNet-50 model
BASE_URL="http://download.tensorflow.org/models/official/resnet50_2017_11_30.tar.gz"

# Download pretrained ResNet-50 model from tensorflow
RESNET_TAR_BALL="resnet.tar.gz"
echo "Downloading ResNet-50 Pretrained Model"
wget "${BASE_URL}" -O "${RESNET_TAR_BALL}"
echo "Uncompressing ResNet-50 Pretrained Model"
tar xzf "${RESNET_TAR_BALL}"
echo "Deleting RESNET tarball"
rm -f resnet.tar.gz
cd -