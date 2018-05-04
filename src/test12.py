#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image
import struct


def read_image(filename):
  f = open(filename, 'rb')
  index = 0
  buf = f.read()
  f.close()
  magic, images, rows, columns = struct.unpack_from('>IIII' , buf , index)
  index += struct.calcsize('>IIII')
  for i in xrange(images):
  #for i in xrange(2000):
    image = Image.new('RGB', (columns, rows))
    for x in xrange(rows):
      for y in xrange(columns):
        image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
        index += struct.calcsize('>B')
    print 'save ' + str(i) + 'image'
    image.save('test/' + str(i) + '.png')