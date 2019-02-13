from settings import *
def xiaMi(input):
    id=re.search('.*/(.*)$',input).group(1)
    #print(id)

    ## 恺撒阵列
    import urllib
    def caesar(location):
        num = int(location[0])
        avg_len, remainder = int(len(location[1:]) / num), int(len(location[1:]) % num)
        result = [location[i * (avg_len + 1) + 1: (i + 1) * (avg_len + 1) + 1] for i in range(remainder)]
        result.extend([location[(avg_len + 1) * remainder:][i * avg_len + 1: (i + 1) * avg_len + 1] for i in range(num-remainder)])
        url = urllib.parse.unquote(''.join([''.join([result[j][i] for j in range(num)]) for i in range(avg_len)]) + \
                            ''.join([result[r][-1] for r in range(remainder)])).replace('^','0')
        return url

    ## json链接
    jsonUrl='https://www.xiami.com/song/playlist/id/'+id+'%20/object_name/default/object_id/0/cat/json'
    headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53',
    'Referer':'http://www.xiami.com/song/playlist/id/'+id
    }

    ## 没有headers就不行
    info=json.loads(requests.get(jsonUrl,headers=headers).content)['data']['trackList'][0]
    #print(info)
    name=info['songName']
    author=info['artist']
    url='http:'+caesar(info['location'])
    lrc=requests.get('http:'+info['lyric_url']).text
    pic='http:'+info['pic']
    return{
    "title":name,
    "author":author,
    "url":url,
    "pic":pic,
    "lrc":lrc

    }

if __name__ == '__main__':
    result = xiaMi("https://www.xiami.com/song/1792541433")
    print(result)