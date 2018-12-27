'''
 * @Author: codeman 
 * @Date: 2018-08-04 20:00:44 
 * @Last Modified by:   codeman 
 * @Last Modified time: 2018-08-04 20:00:44 
'''
import os
import sys
import os.path
import pickle
import struct
dirroot = r'E:/Git_house'
for i in os.listdir(dirroot):
    if i.split('.')[1]!='txt':
        continue
    file = open(dirroot + '/' + i, 'r')
    filename = i.split('.')[0] + '.dat'
    fileNew = open(dirroot + '/' + filename, 'wb')
    lines = file.readlines()
    for line in lines:
        padata = struct.pack('20s',bytes(line,'gb2312'))
        fileNew.write(padata)
    fileNew.close()
    file.close()
    fileNew = open(dirroot + '/' + filename, 'rb')
    lines = fileNew.readlines()
    for line in lines:
        t=len(line)
        padata, = struct.unpack('{0}s'.format(t),line)
        print(padata.decode('gb2312'))
    fileNew.close()