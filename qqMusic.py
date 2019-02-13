import base64
from settings import *
def qqMusic(input):
    html=get_one_page(input)
    # 歌曲的基本信息
    songData=json.loads(re.search('g_SongData = (.*?);',html).group(1))
    #print(songData)
    name=songData['songtitle']
    author=songData['singername']
    songid=songData['songid']
    pic='https://y.gtimg.cn/music/photo_new/T002R300x300M000'+songData['albummid']+'.jpg?max_age=2592000'
    ## 获取vkey
    vkeyUrl='https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid='+songData['songmid']+'&filename=C400'+songData['strMediaMid']+'.m4a&guid=6612300644'
    data=json.loads(get_one_page(vkeyUrl))['data']
    #print("data",data)
    #print(data)
    vkey=data['items'][0]['vkey']
    filename=data['items'][0]['filename']
    url='http://dl.stream.qqmusic.qq.com/'+filename+'?vkey='+vkey+'&guid=6612300644&uin=0&fromtag=66'
    lrcUrl="https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg"
    #print(lrcUrl)
    #lrc=re.search('CDATA\[(.*)\]\]>',get_one_page(lrcUrl),re.S).group(1)
    # 模拟请求歌词
    headers={
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://y.qq.com',
    'referer': 'https://y.qq.com/portal/player.html',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
    params={
        '-': 'MusicJsonCallback_lrc',
        'pcachetime': '1548902360952',
        'songmid': songData['songmid'],
        'g_tk': '5381',
        'loginUin': 0,
        'hostUin': 0,
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': 0,
        'platform': 'yqq.json',
        'needNewCode': 0
    }
    lrc=base64.b64decode(json.loads(requests.get(lrcUrl,headers=headers,params=params).text)['lyric']).decode('UTF-8')
    return{
    "title":name,
    "author":author,
    "url":url,
    "pic":pic,
    "lrc":lrc

}



if __name__ == '__main__':
    result = qqMusic("https://y.qq.com/n/yqq/song/001QGcyU3RXtdA.html")
    print(result)