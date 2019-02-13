from settings import *

def timeTag(seconds):
    m, s = divmod(seconds, 60)
    return ("%02d:%.2f" % (m, s))


def kuwo(input):
    id = re.search('.*/(.*)$', input).group(1)
    # print(id)
    url = 'http://player.kuwo.cn/webmusic/st/getNewMuiseByRid?rid=MUSIC_' + id
    # 解决中文乱码
    html = get_one_page(url)
    # 歌名
    title = pq(html)('name').text()
    # 歌手
    author = pq(html)('singer').text()
    # 链接地址
    url = 'http://' + pq(html)('mp3dl').text() + '/resource/' + pq(html)('mp3path').text()
    # 封面图片
    pic = pq(html)('artist_pic').text()

    lyc = json.loads(re.search('lrcList = (.*?])', get_one_page(input)).group(1))
    ## 解析歌词
    lyric = ''
    for item in lyc:
        time = '[' + timeTag(seconds=float(item["time"])) + ']'
        lyric = lyric + time + item['lineLyric'] + '\n'
    return {
        "title": title,
        "author": author,
        "url": url,
        "pic": pic,
        "lrc": lyric

    }


if __name__ == '__main__':
    result = kuwo("http://www.kuwo.cn/yinyue/359900")
    print(result)
