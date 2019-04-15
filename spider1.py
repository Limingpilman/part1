import re
import sys
import urllib.request
from urllib import error
from urllib.robotparser import RobotFileParser

import builtwith
import chardet
import whois


def check(url,user_agent):              ##判断可访问性
    rb = RobotFileParser()
    url_1 = re.match(r'https://(.*?)/',url)
    rb.set_url("{0}/robots.txt".format(url_1.group(0)))
    rb.read()
    return rb.can_fetch(user_agent,url)


def download(url_,user_agent = 'Baiduspider',proxy = None, num_retries = 5):      ##下载函数
    if not check(url_,user_agent):
        sys.exit("{0} is not allowed, please exchange useragent".format(user_agent))
    print("Downloading:",url_)
    headers = {'User-agent':user_agent}
    req = urllib.request.Request(url_, headers = headers)
    opener = urllib.request.build_opener()                  ##添加代理
    if proxy:
        proxy_params = {urllib.request.urlparse(url).scheme:proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        html = opener.open(req).read()
    except urllib.request.HTTPError as e:
        print("DownloadError!",e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code <= 600:
                return download(url_, user_agent, proxy, num_retries - 1)
    return html


def Crawle(url, regex, max_depth=1, b=1):        ##爬虫主体
    html = download(url)
    #chart_s = chardet.detect(html)['encoding']
    t = re.findall(regex,html.decode('gbk'))
    try:
        file = open('shiti{0}.txt'.format(b),'w')
        for i in t:
            ii = re.sub(r'<.*>','',i)
            print(ii,file=file)
            if ii =='':
                continue
            print('\n',file=file)
        file.close()
    except:
        print("输出错误")


url = "https://wenku.baidu.com/view/2f2a06af0342a8956bec0975f46527d3240ca60f.html"
regex = r"<p\s*.*>(.*?)</p>"
Crawle(url,regex)
'''
p = ['83368336910','04190419397','37339019755','87798779455','02030203398']
for a in p:
    url = "http://www.wangxiao.cn/hushi2/{0}.html".format(a)
    Crawle(url,a)
'''

'''

'''
