from pyquery import PyQuery as pq
import re
import json
import requests
def get_one_page(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
    response = requests.get(url,headers=headers)
    response.encoding = "utf-8"
    if response.status_code == 200:
        return response.content.decode("utf8", "ignore")
    return None