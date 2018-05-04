#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import os
import gzip
import numpy
import sys

import struct

train_images = "MNIST_data/train-images-idx3-ubyte.gz"
train_labels = "MNIST_data/train-labels-idx1-ubyte.gz"
t10k_images = "MNIST_data/t10k-images-idx3-ubyte.gz"
t10k_labels = "MNIST_data/t10k-labels-idx1-ubyte.gz"

labels = []

def read_labels(filename):
    with gzip.open(filename) as bytestream:
        # magic = _read32(bytestream)
        f = bytestream
        index = 0
        buf = f.read()
        f.close()
        magic, images = struct.unpack_from('>II', buf, index)
        # num =  struct.unpack_from('>B', buf, 8)
        # print(num)
        print(magic)
        print(images)
        index = 8
        while index < images:
            num = struct.unpack_from('b', buf, index)[0]
            # print(num[0])
            labels.append(num)
            index += 1
    return


def read_images(filename):
    with gzip.open(filename) as bytestream:
        # magic = _read32(bytestream)
        f = bytestream
        index = 0
        buf = f.read()
        f.close()
        magic, size,rows,columns = struct.unpack_from('>IIII', buf, index)
        # num =  struct.unpack_from('>B', buf, 8)
        # print(num)
        print(magic)
        print(size)
        print(rows)
        print(columns)
        index = 12

        for i in xrange(size):
            image = [[]]
            print(labels[i])
            for x in xrange(rows):
                for y in xrange(columns):
                    num = struct.unpack_from('B', buf, index)[0]
                    if num > 50:
                        sys.stdout.write(str('1'))
                    else:
                        sys.stdout.write(str('0'))
                    # print(num)
                    # image[x][y] = num
                    index += 1
                sys.stdout.write(str('\n'))
            # print(image)
            sys.stdout.flush()
            # print()


        # while index < size:
        #     num = struct.unpack_from('B', buf, index)
        #     #num = struct.unpack_from('b', buf, index)
        #     print(num[0])
        #     index += 1
    return


read_labels(train_labels)

read_images(train_images)