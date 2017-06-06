import struct

# This code present the size and color number of a bmp.
def check_bmp(file):
    with open(file, 'rb') as f:
        s = f.read(30)
    data = struct.unpack('<ccIIIIIIHH', s)
    if data[0] == b'B' and data[1] == b'M':
        print('The size of the bmp is %dx%d, the number of colors is %d.' % (data[6], data[7], data[-1]))
    else:
        print('The file is not a bmp.')
