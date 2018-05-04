#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import gzip
import numpy
import sys


def _read32(bytestream):
    dt = numpy.dtype(numpy.uint32).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(4), dtype=dt)[0]


def _read8(bytestream):
    dt = numpy.dtype(numpy.uint8).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(1), dtype=dt)[0]


train_images = "MNIST_data/train-images-idx3-ubyte.gz"
train_labels = "MNIST_data/train-labels-idx1-ubyte.gz"
t10k_images = "MNIST_data/t10k-images-idx3-ubyte.gz"
t10k_labels = "MNIST_data/t10k-labels-idx1-ubyte.gz"

def read_labels(filename):
    print('Extracting', filename)
    with gzip.open(filename) as bytestream:
        magic = _read32(bytestream)
        num_images = _read32(bytestream)

        print(magic)
        print(num_images)
        while True:
            num = _read8(bytestream)
            print(num)
    return

images = read_labels(train_labels)
