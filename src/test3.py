from PIL import Image
import struct
def read_image(filename):
    f = open(filename,'rb')

    index = 0
    buf = f.read()
    f.close()
    magic,images,rows,colums = struct.unpack_from('>IIII',buf,index)
    index += struct.calcsize('>IIII')
    for i in xrange(images):
        image = Image.new('L',(colums,rows))
        for x in xrange(rows):
            for y in xrange(colums):
                image.putpixel((y,x),int(struct.unpack_from('>B',buf,index)[0]))
                index+=struct.calcsize('>B')

        print 'save ' + str(i) + 'image'
        image.save('test' + str(i) + '.png')