from kuwo import *
from qqMusic import *
from xiaMi import *
from cloudMusic import *
import re
import sys
if __name__ == '__main__':
    #a="https://www.xiami.com/song/1792541433"
    #b="http://music.163.com/song/media/outer/url?id="
    #c="https://y.qq.com/n/yqq/song/001QGcyU3RXtdA.html"
    #d="http://www.kuwo.cn/yinyue/359900"
    url=str(sys.argv[1])
    #print("url= ",url)
    media=re.search('\.(.*)\.(com|cn)',url).group(1)
    if media=='kuwo':
        print(kuwo(url))
    elif media=='163':
        print(cloudMusic(url))
    elif media=='qq':
        print(qqMusic(url))
    elif media=='xiami':
        print(xiaMi(url))
    else:
        print("sorry,this program  only support music released in four website: kuwo, cloudmusic,qqmusic and xiami")
    #print(result)