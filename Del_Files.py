#!/usr/bin/python
# -*- coding: utf-8 -*-  #指定编码格式，python默认unicode编码
'''
   删除指定文件夹里面的非 .jpg 文件
   删除小于10K大小的文件（单位：K）
'''
import os
def del_files(path):
    '''
    删除指定文件夹里面的非 .jpg 文件
    '''
    for root , dirs, files in os.walk(path):
        print root,dirs,files
        for file in files:
            if file.endswith(".jpg"):
                # print file
                pass
            else:
                # 删除文件  文件要绝对路径下
                os.remove(os.path.join(root, file))
                print ("Delete File: " + os.path.join(root, file))
        return

def deleteBySize(path,minSize):
    """删除小于minSize的文件（单位：K）"""
    files = os.listdir(path) #列出目录下的文件
    # print files
    for file in files:
        file = os.path.join(path, file)
        if os.path.getsize(file) < minSize * 1000:
            os.remove(file)    #删除文件
            print(file + " deleted")
    return

if __name__ == "__main__":
    path = u'D:\\Users\\40325\\Pictures\\新建文件夹\\人间四月天，相约金岭间 - 美篇_files'
    del_files(path)
    deleteBySize(path,10)