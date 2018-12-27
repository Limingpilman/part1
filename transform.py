'''
 * @Author: codeman 
 * @Date: 2018-08-04 18:48:50 
 * @Last Modified by: codeman
 * @Last Modified time: 2018-08-04 18:54:56
'''
import os
import sys
import os.path
import pickle
import struct
dirroot = r'E:/Git_house'
for dirnames in os.listdir(dirroot):
    print('进入文件夹')
    for dirname in os.listdir(dirroot+'/'+ dirnames):
        if dirname.split('.')[1]!='txt':
            continue
        file = open(dirroot+dirnames+'/'+dirname,'r')
        filename = dirname.split('.')[0]+'.dat'
        if not os.path.exists(dirroot+dirnames+'/'):
            os.makedirs(dirroot+dirnames+'/')
        fileNew=open(dirroot+dirnames+'/'+filename,'wb')
        lines = file.readlines()

        for line in lines:
            curLine = line.split(' ')
            for i in range(len(curLine)):
                if len(curLine[i])==0:
                    continue
                parsedata = struct.pack('f',float(curLine[i]))
                fileNew.write(parsedata)
            fileNew.write('\n')
        fileNew.close()
        file.close()
