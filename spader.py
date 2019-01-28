import builtwith
import whois
from urllib.robotparser import RobotFileParser
import urllib.request
from urllib import error

def download(url_,user_agent = 'asp',num_retries = 5):
    print("Downloading:",url_)
    headers = {'User-agent':user_agent}
    req = urllib.request.Request(url_, headers = headers)
    try:
        html = urllib.request.urlopen(req).read()
    except urllib.request.HTTPError as e:
        print("DownloadError!",e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code <= 600:
                return download(url_,num_retries - 1)
    return html

rb = RobotFileParser()
rb.set_url("http://www.runoob.com/robots.txt")
rb.read()
url = "http://www.runoob.com"
a = builtwith.parse(url)
print(a)
print(whois.whois("runoob.com"))
user_agent = "goodCrawler"
download(url, user_agent, 6)

