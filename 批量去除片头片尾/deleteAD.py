import os
import re
import time
import subprocess
from decimal import Decimal
from multiprocessing import Pool

path = r'D:\deleteAD\原视频'  # 原文件夹路径
new_path = r'D:\deleteAD\新视频'  # 新文件夹路径
if not os.path.exists(new_path):
    os.mkdir(new_path)
else:
    pass


# 获取视频的 duration 时长 长 宽
def get_video_length(file):
    process = subprocess.Popen(['ffmpeg', '-i', file],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()
    # print(stdout)
    pattern_duration = re.compile(r"Duration:\s(\d+?):(\d+?):(\d+\.\d+?),")
    pattern_size = re.compile(r",\s(\d{3,4})x(\d{3,4})[\s or ,]")
    matches = re.search(pattern_duration, stdout.decode('utf-8'))
    size = re.search(pattern_size, stdout.decode('utf-8'))
    if size:
        size = size.groups()
        # print(size)
    if matches:
        matches = matches.groups()
        # print(matches)
        hours = Decimal(matches[0])
        minutes = Decimal(matches[1])
        seconds = Decimal(matches[2])  # 处理为十进制，避免小数点报错
        total = 0
        total += 60 * 60 * hours
        total += 60 * minutes
        total += seconds
        width = size[0]
        height = size[1]
        return {'total': total, 'width': width, 'height': height}


def cutVideo(startPoint, file, endPoint, newFile):
    command = [
        'ffmpeg', '-ss', startPoint, '-i', file, '-acodec', 'copy', '-vcodec',
        'copy', '-t', endPoint, newFile
    ]
    subprocess.call(command)


def millisecToAssFormat(t):  # 取时间，单位秒
    s = t % 60
    m = t // 60
    if t < 3600:
        h = 00
    else:
        h = t // 3600
        m = t // 60 - h * 60
    return '%02d:%02d:%02d' % (h, m, s)


def main(dict):
    file = dict['file']  # 文件名
    piantou = dict['piantou']  # 片头时长
    pianwei = dict['pianwei']  # 片尾时长
    videoInfo = get_video_length(file)  # 视频信息
    # print(videoInfo)
    if videoInfo:
        duration = videoInfo.get('total')  # 时长 秒
        startPoint = piantou  # 剪掉片头时间,从原文件此处开始播放
        startPoint = millisecToAssFormat(startPoint)
        endPoint = duration - piantou - pianwei  # 剪掉片头片尾时间和,结果等于新文件总时长
        endPoint = millisecToAssFormat(endPoint)
        new_File = new_path + file.replace(path, '')  # 创建生成的文件路径+文件名
        # print(new_File, endPoint)
        cutVideo(startPoint, file, endPoint, new_File)


if __name__ == '__main__':
    # main()
    timt0 = time.time()
    file = [os.path.join(path, file) for file in os.listdir(path)]
    a = input('输入片头时长：')  # 片头时长
    b = input('输入片尾时长：')  # 片尾时长
    piantou = [int(a)] * len(file)  # 片头时长列表
    pianwei = [int(b)] * len(file)  # 片尾时长列表
    dict_list = []  # main函数参数列表
    for x in range(len(file)):
        dict = {
            'file': file[x],
            'piantou': piantou[x],
            'pianwei': pianwei[x]
        }  # main函数参数，文件路径，片头片尾时长
        dict_list.append(dict)
    print('\n规则：去除片头%s秒片尾%s秒,开始。\n' % (a, b))
    pool = Pool()
    pool.map(main, dict_list)
    pool.close()
    pool.join()
    time1 = time.time() - timt0
    print('\n结束，处理%d个视频文件，共用时%.4f秒。\n' % (len(file), time1))
    input('回车键退出')
