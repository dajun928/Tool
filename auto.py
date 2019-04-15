#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@version : 
@file : auto.py
@time : 2019/04/15 20:06:53
@func : 剪切目录A 的内容到目录B
"""
import os
import shutil


A = r"D:\test\a"
B = r"D:\test\b"
#通过校验MD5 判断B内的文件与A 不同
def get_MD5(file_path):
    files_md5 = os.popen('md5 %s' % file_path).read().strip()
    file_md5 = files_md5.replace('MD5 (%s) = ' % file_path, '')
    return file_md5



def main(path, out):
    for files in os.listdir(path):
        name = os.path.join(path, files)
        back_name = os.path.join(out, files)
        if os.path.isfile(name):
            if os.path.isfile(back_name):
                if get_MD5(name) != get_MD5(back_name):
                    print(back_name)
                    shutil.move(name,back_name)
            else:
                print(back_name)
                shutil.move(name, back_name)
        else:
            if not os.path.isdir(back_name):
                os.makedirs(back_name)
            main(name, back_name)


if __name__ == '__main__':
    main(A, B)

#src dst
