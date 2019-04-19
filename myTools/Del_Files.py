#!/usr/bin/python
# -*- coding: utf-8 -*-  #指定编码格式，python默认unicode编码
'''
    删除指定路径下文件夹里文件或文件夹的工具类
    删除文件时可以看到删除的结果
'''
import os
class Deleter():
    def __init__(self, ToPrint=True, Logger=None):
        self.Logger = Logger
        self.ToPrint = ToPrint
        return

    def Log(self, Str):
        if self.Logger:
            self.Logger.Log(Str)
        if self.ToPrint:
            print Str
        return

    ## Delete a folder
    # @param FolderName folder to delete
    # <br/>
    # Example:
    # <pre>
    #  T = Common()
    #  FolderName = r'Temp'
    #  T.DeleteFolder(FolderName)
    # </pre>
    def DeleteFolder(self, FolderName):
        '''''delete files and folders'''
        for Item in os.listdir(FolderName):
            TempPath = os.path.join(FolderName, Item)
            if os.path.isfile(TempPath):
                self.DeleteFile(TempPath)
                pass
            elif os.path.isdir(TempPath):
                self.DeleteFolder(TempPath)
                pass
            else:
                self.Log("Not a file or folder: %s" % (FolderName))
                pass
            pass

        try:
            os.rmdir(FolderName)
            self.Log("Folder deleted: %s" % (FolderName))
        except:
            self.Log("Failed to delete folder: %s" % (FolderName))
            pass

        return

    ## Delete a file
    # @param FileName file to delete
    # <br/>
    # Example:
    # <pre>
    #  T = Common()
    #  FolderName = r'TempFile.txt'
    #  T.DeleteFile(FileName)
    # </pre>
    def DeleteFile(self, FileName):
        try:
            os.remove(FileName)
            self.Log("File deleted: %s" % (FileName))
        except:
            self.Log("Failed to delete file: %s" % (FileName))
            pass
        return

    ## Delete a list of folders
    # @param FolderList a list of folder to delete
    # <br/>
    # Example:
    # <pre>
    #  T = Common()
    #  FolderNameList = [r'Temp1', r'Temp2']
    #  T.DeleteFolders(FolderNameList)
    # </pre>
    def DeleteFolders(self, FolderNameList):
        for FolderName in FolderNameList:
            self.DeleteFolder(FolderName)
        return

    ## Delete a list of files
    # @param FolderList a list of files to delete
    # <br/>
    # Example:
    # <pre>
    #  T = Common()
    #  FolderNameList = [r'Temp1.txt', r'Temp2.txt']
    #  T.DeleteFiles(FileNameList)
    # </pre>
    def DeleteFiles(self, FileNameList):
        for FileName in FileNameList:
            self.DeleteFile(FileName)
        return

if __name__ == '__main__':
    Op = Deleter()
    #删除 D:\test 路径下的 redis文件夹里面的所有文件
    path=u'D:\\test\\redis\\'
    # path=u'\\MI 6\\内部存储设备\\DCIM\\Camera\\'
    Op.DeleteFolder(path)
    pass

