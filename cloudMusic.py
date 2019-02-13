from settings import *

def cloudMusic(input):
    id = re.search('id=(.*)$', input).group(1)
    # print(id)
    url = ' http://music.163.com/song/media/outer/url?id=' + id + '.mp3'
    ## 获取详细信息
    detailUrl = 'http://music.163.com/api/song/detail/?&ids=[' + id + ']&csrf_token='

    ## 获取歌词信息
    lycUrl = 'http://music.163.com/api/song/media?id=' + id
    detail = json.loads(get_one_page(detailUrl))
    name = detail["songs"][0]["name"]
    author = detail["songs"][0]["artists"][0]["name"]
    pic = detail["songs"][0]["album"]["picUrl"]
    lyric = json.loads(get_one_page(lycUrl))['lyric']
    return {
        "title": name,
        "author": author,
        "url": url,
        "pic": pic,
        "lrc": lyric

    }

if __name__ == '__main__':
    result = cloudMusic("https://music.163.com/#/song?id=1338695683")
    print(result)