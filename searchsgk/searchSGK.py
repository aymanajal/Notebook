import sys
import os
import re
import time


def searchTable(key_str, rootPath):
    path_list=os.listdir(rootPath)
    path_list.sort()
    for filename in path_list:
        fileFullPath  =  rootPath + filename
        if(os.path.isdir(fileFullPath)):
            searchTable(key_str, rootPath + filename + '/')
        elif(os.path.isfile(fileFullPath)):
            data = ''
            with open(fileFullPath, 'r', encoding='utf-8', errors='ignore') as f:
                data = f.readline()
                while(data):
                    for search_str in key_str:
                        search_key = r''+search_str + ''
                        if(re.search(search_key, data, re.I|re.M)):
                            print(search_str, data, fileFullPath)
                            time.sleep(1)
                    
                    data = f.readline()

                f.close()

    return ''


if (len(sys.argv) < 2):
    print('请输入查找关键字')
    exit(0)
sys.argv.pop(0)
key_str = sys.argv



pathlist = ['E:/tmp/'
        ]  # 你搜索的数据文件目录路径

for path in pathlist:
    filekey = searchTable(key_str, path)

print('搜索完成')
