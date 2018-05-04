#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import os
import gzip
import numpy
import sys

baseUrl = "http://yann.lecun.com/exdb/mnist/"


def download(dir, fileName):
    if not os.path.exists(dir):
        os.mkdir(dir)
    fullFilePath = dir + fileName
    if os.path.exists(fullFilePath):
        return os.path.abspath(fullFilePath)
    filepath, _ = urllib.urlretrieve(baseUrl + fileName, fullFilePath)
    statinfo = os.stat(filepath)
    print('Successfully downloaded', fileName, statinfo.st_size, 'bytes.')
    return os.path.abspath(fullFilePath)


def _read32(bytestream):
    dt = numpy.dtype(numpy.uint32).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(4), dtype=dt)[0]


def _read8(bytestream):
    dt = numpy.dtype(numpy.uint8).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(1), dtype=dt)[0]


baseDir = "MNIST_data/"
train_images = download(baseDir, "train-images-idx3-ubyte.gz")
train_labels = download(baseDir, "train-labels-idx1-ubyte.gz")
t10k_images = download(baseDir, "t10k-images-idx3-ubyte.gz")
t10k_labels = download(baseDir, "t10k-labels-idx1-ubyte.gz")


# import test12
# test12.read_image("/Users/Wiki/PycharmProjects/untitled1/src/MNIST_data/t10k-images-idx3-ubyte")


def extract_images(filename):
    """Extract the images into a 4D uint8 numpy array [index, y, x, depth]."""
    print('Extracting', filename)
    with gzip.open(filename) as bytestream:
        magic = _read32(bytestream)
        # if magic != 2051:
        #   raise ValueError(
        #       'Invalid magic number %d in MNIST image file: %s' %
        #       (magic, filename))
        num_images = _read32(bytestream)
        # rows = _read32(bytestream)
        # cols = _read32(bytestream)
        # buf = bytestream.read(rows * cols * num_images)
        # data = numpy.frombuffer(buf, dtype=numpy.uint8)
        # data = data.reshape(num_images, rows, cols, 1)

        print(num_images)
        # print(rows)
        while True:
            num = _read8(bytestream)
            print(num)
        # print(cols)
        # print(buf)

        return


# bytestream = gzip.open(t10k_images)
#
#
# num_images = _read32(bytestream)
# rows = _read32(bytestream)
# cols = _read32(bytestream)
# buf = bytestream.read(rows * cols * num_images)
# data = numpy.frombuffer(buf, dtype=numpy.uint8)
# data = data.reshape(num_images, rows, cols, 1)


# images = extract_images(train_labels)


# print(len(images))
# print(len(images[0]))
# print(len(images[0][0]))
#
# images = images.reshape(images.shape[0],
#                               images.shape[1] * images.shape[2])
#
#
#
# def printChat(image):
#     for i in range(0, 28):
#         for j in range(0, 28):
#             num = image[j * i]
#             # sys.stdout.write(str(num)+" ")
#             if num < 58:
#                 sys.stdout.write(str(' '))
#             else:
#                 sys.stdout.write(str('*'))
#             #
#         sys.stdout.write('\n')
#     return
# printChat(images[1110])
# printChat(images[1111])
# printChat(images[1112])
# printChat(images[1113])
#
# print(len(images[0]))


# for item in images[0]:
#     for j in item:
#         sys.stdout.write(str(j[0]))
#     sys.stdout.write('\n')


sys.stdout.flush()
import struct


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
            num = struct.unpack_from('b', buf, index)
            print(num[0])
            index += 1


read_labels(train_labels)
