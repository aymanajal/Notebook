# FFmoeg命令

## FFmpeg 语法格式
```
ffmpeg [全局选项] {[输入文件选项] -i 输入_url_地址} ...
 {[输出文件选项] 输出_url_地址} ...
 ```

## 删除片头命令  
`ffmpeg -ss 00:03:00 -i input.mp4 -c:v copy -c:a copy output.mp4`  

## 剪掉固定时长片头的同时也剪掉固定时长的片尾
 ```ffmpeg
{beg=7
end=7

#用 for 循环直接获取当前目录下的 mp4、mp3、avi 等文件循环处理，单个文件可以去掉 for 循环
for i in (*.mp4,*.mp3,*.avi ); do
	#将元数据信息临时保存到 tmp.log 文件中
    nohup /usr/local/ffmpeg/bin/ffmpeg -i "$i" > tmp.log
    #获取视频的时长，格式为  00:00:10,10 （时：分：秒，微妙）
    time="`cat /usr/local/ffmpeg/tmp.log |grep Duration: |awk  '{print $2}'|awk -F "," '{print $1}'|xargs`"
    echo $time
    #求视频的总时长，先分别求出小时、分、秒的值，这里不处理微秒，可以忽略
    hour="`echo $time |awk -F ":" '{print $1}' `"
    min="`echo $time |awk -F ":" '{print $2}' `"
    sec="`echo $time |awk -F ":" '{print $3}'|awk -F "." '{print $1}' `"
    #echo $hour $min $sec
    num1=`expr $hour \* 3600`
    num2=`expr $min \* 60`
    num3=$sec
    #计算出视频的总时长（秒）
    sum=`expr $num1 + $num2 + $num3`  
    
    #总时长减去开头和结尾就是截取后的视频时长,并且这里不需要再转回 hour:min:sec 的格式，直接使用结果即可
    newtime=`expr $sum - $beg - $end`
    echo $newtime
    /usr/local/ffmpeg/bin/ffmpeg -ss 00:00:07 -i $i -t $newtime -c:v copy -c:a copy /data/tmp/$i -y
done}
```

## 去除水印  
```
ffmpeg -i input.mp4 -b:v 3170k -vf  "delogo=x=1:y=1:w=1918:h=30:show=0" output.mp4
#-b:v 3170k 是设置视频的码率，可以不加。
#-vf  "delogo=x=1:y=1:w=100:h=30:show=0" 表示给视频添加一个类似马赛克的滤镜效果，滤镜的大小是以视频左上角为（1，1）坐标，宽为 100，高为 30 的滤镜，如果 show=1 就会有一个绿框，我这里是直接设置不可见
```

## 修改视频格式  
```
ffmpeg -i input.mp4 -qscale 0 -y output.mp4
#-qscale 0 参数是为了不影响资源的质量
```

## mp3 转换 wav
```
ffmpeg -i 01.mp3 -acodec pcm_s16le -ac 1 -ar 8000 output.wav
```

## 添加水印  
```
ffmpeg -i 031.mp4 -acodec copy -b:v 42695k -vf "movie=log.png[watermark];[in][watermark]overlay=20:20" out.mp4
```

## 合并视频  
1. 先转换为ts流  
```
ffmpeg -i 1.mp4 -vcodec copy -acodec copy -vbsf h264_mp4toannexb 11.mp4
ffmpeg -i 2.mp4 -vcodec copy -acodec copy -vbsf h264_mp4toannexb 12.mp4
ffmpeg -i 3.mp4 -vcodec copy -acodec copy -vbsf h264_mp4toannexb 13.mp4

ffmpeg -i [1.1.1]--俄罗斯经典文学在中国的接受.mp4 -vcodec copy -acodec copy -vbsf h264_mp4toannexb 1.mp4
```
2. 再进行合并  
```
ffmpeg -i "concat:1.ts|2.ts" -acodec copy -vcodec copy -absf aac_adtstoasc output.mp4
```

## 从视频末尾开始截取
` ffmpeg -sseof -10 -i 005.mp4 -to 00:00:00 -c copy out005.mp4 ` 只保留截取位置

## 删除末尾片尾
`麻烦-不如pr`