import re
import json
import time
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def print_color(notice_time, title):
    grep_list = ['活动', '周岁', '周年', '双倍', '三倍', '端午', '七夕', '双11安全保卫战']
    num = 1
    for i in grep_list:
        if (i in title) and (num == 1) and ('2020' in notice_time or notice_time == '' or '20-' in notice_time) and (
                '公示' not in title and '公告' not in title):
            print('\033[0;33m| \033[0m\033[0;31m%s\t%s\033[0m' % (notice_time, title))
            num = num + 1
    if num == 1:
        print('\033[0;33m| \033[0m' + notice_time + '\t' + title)


def src_360(number):
    print('\n\033[0;33m-----------------------360 SRC------------------------\033[0m')
    url = 'https://security.360.cn/News/news?type=-1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.news-content')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 4].select('.new-list-time')[0].text.strip()
        title = notice_list[i + 4].select('a')[0].text
        print_color(time, title)


def src_58(number):
    print('\n\033[0;33m-----------------------58 SRC------------------------\033[0m')
    url = 'https://security.58.com/notice/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.time')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text
        title = bs.select('.box')[0].select('a')[i].text
        print_color(time, title)


def alibaba(number):
    print('\n\033[0;33m-----------------------阿里SRC------------------------\033[0m')
    url = 'https://security.alibaba.com/api/asrc/pub/announcements/list.json?&page=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['rows']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['lastModify']
        title = notice_list[i]['title']
        print_color(time, title)


def ele(number):
    print('\n\033[0;33m-----------------------阿里本地生活SRC----------------\033[0m')
    url = 'https://security.ele.me/api/bulletin/listBulletins?offset=0&limit=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['modelList']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['createdAt']
        time_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color(time_format, title)


def iqiyi(number):
    print('\n\033[0;33m-----------------------爱奇艺SRC----------------------\033[0m')
    url = 'https://security.iqiyi.com/api/publish/notice/list?sign=6ce5b4f7ad460b2ae3046422f61f905e4e3ecd03'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['create_time_str']
        title = notice_list[i]['title']
        print_color(time, title)


def baidu(number):
    print('\n\033[0;33m-----------------------百度SRC------------------------\033[0m')
    url = 'https://bsrc.baidu.com/v2/api/announcement?type=&page=1&pageSize=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['retdata']['announcements']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTime']
        title = notice_list[i]['title']
        print_color(time, title)


def ke(number):
    print('\n\033[0;33m-----------------------贝壳SRC------------------------\033[0m')
    url = 'https://security.ke.com/api/notices/list'
    headers = {
        'Referer': 'https://security.ke.com/notices',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    r = requests.post(url, headers=headers, data={"page": 1})
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTime']
        title = notice_list[i]['title']
        print_color(time, title)


def bilibili(number):
    print('\n\033[0;33m-----------------------哔哩哔哩SRC---------------------\033[0m')
    url = 'https://security.bilibili.com/announcement/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    number = number * 2 + 1
    notice_list = bs.select('td')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(2, number, 2):
        time = notice_list[i].text.replace('\n', '')
        title = notice_list[i + 1].text.replace('\n', '')
        print_color(time, title)


def cainiao(number):
    print('\n\033[0;33m-----------------------菜鸟SRC------------------------\033[0m')
    url = 'https://sec.cainiao.com/announcement.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('td')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text.split('\n')[0].strip().split('][')[0].replace('[', '')
        title = notice_list[i].text.split('\n')[1].strip()
        print_color(time, title)


def didichuxing(number):
    print('\n\033[0;33m-----------------------滴滴出行SRC---------------------\033[0m')
    url = 'http://sec.didichuxing.com/rest/article/list?page=1&size=5&option=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['time']
        time_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color(time_format, title)


def duxiaoman(number):
    print('\n\033[0;33m-----------------------度小满SRC----------------------\033[0m')
    url = 'https://security.duxiaoman.com/index.php?v2api/announcelist'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='page=1&type=0&token=null')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['rows']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['time']
        title = notice_list[i]['title']
        print_color(time, title)


def guazi(number):
    print('\n\033[0;33m-----------------------瓜子SRC------------------------\033[0m')
    url = 'https://security.guazi.com/gzsrc/notice/queryNoticesList'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data="pageNo=1")
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['publishDate']
        title = notice_list[i]['title']
        print_color(time, title)


def jd(number):
    print('\n\033[0;33m-----------------------京东SRC------------------------\033[0m')
    url = 'https://security.jd.com/notice/list?parent_type=2&child_type=0&offset=0&limit=12'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['notices']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['CreateTime']
        title = notice_list[i]['Title']
        print_color(time, title)


def alipay(number):
    print('\n\033[0;33m-----------------------蚂蚁金服SRC---------------------\033[0m')
    url = 'https://security.alipay.com/sc/afsrc/notice/noticeList.json?_input_charset=utf-8&_output_charset=utf-8'
    headers = {
        'Referer': 'https://security.alipay.com/home.htm',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['resultAfsrc']['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['noticeTime']
        title = notice_list[i]['title']
        print_color(time, title)


def meituan(number):
    print('\n\033[0;33m-----------------------美团SRC------------------------\033[0m')
    url = 'https://security.meituan.com/api/announce/list?typeId=0&curPage=1&perPage=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['items']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['createTime']
        time_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['name']
        print_color(time_format, title)


def immomo(number):
    print('\n\033[0;33m-----------------------陌陌SRC------------------------\033[0m')
    url = 'https://security.immomo.com/blog'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    # 动态渲染
    session = HTMLSession()
    r = session.get(url,headers=headers)
    r.html.render()

    bs = BeautifulSoup(r.html.html, 'html.parser')
    notice_list = bs.select('.blog-list')[0].select('span')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text
        title = bs.select('.blog-list')[0].select('h2')[i].text.strip().split('\n')[-2].strip()
        print_color(time, title)


def oppo(number):
    print('\n\033[0;33m-----------------------OPPO SRC-----------------------\033[0m')
    url = 'https://security.oppo.com/cn/be/cn/osrc/FEnotice/findAllNotice'
    headers = {
        'Host': 'security.oppo.com',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='{"pageNum":1,"pageSize":10}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    print(number)
    for i in range(0, number):
        time = notice_list[i]['notice_online_time']
        title = notice_list[i]['notice_name']
        print_color(time, title)


def pingan(number):
    print('\n\033[0;33m-----------------------平安SRC------------------------\033[0m')
    url = 'https://security.pingan.com/announcement/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('#News_List')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 1].select('span')[0].text.strip()
        title = notice_list[i + 1].select('a')[0].text.strip()
        print_color(time, title)


def shuidihuzhu(number):
    print('\n\033[0;33m-----------------------水滴SRC------------------------\033[0m')
    url = 'https://api.shuidihuzhu.com/api/wide/announce/getAnnouncePageList'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    r = requests.post(url, headers=headers, data='{"pageNum":1,"pageSize":10}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['updateTime']
        time_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color(time_format, title)


def sf_express(number):
    print('\n\033[0;33m-----------------------顺丰SRC------------------------\033[0m')
    url = 'http://sfsrc.sf-express.com/notice/getLatestNotices'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data="limit=10&offset=0")
    r_json = json.loads(r.text)
    notice_list = r_json['rows']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['modifyTime']
        time_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['noticeTitle']
        print_color(time_format, title)


def tencent(number):
    print('\n\033[0;33m-----------------------腾讯SRC------------------------\033[0m')
    url = 'https://security.tencent.com/index.php/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.section-announcement')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text
        title = notice_list[i].select('a')[0].text
        print_color(time, title)


def vivo(number):
    print('\n\033[0;33m-----------------------vivo SRC-----------------------\033[0m')
    url = 'https://security.vivo.com.cn/api/front/notice/noticeListByPage.do'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='{"pageNo":1,"pageSize":10,"pageOrder":"","pageSort":""}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['updateTime']
        title = notice_list[i]['noticeTitle']
        print_color(time, title)


def src_163(number):
    print('\n\033[0;33m-----------------------网易SRC------------------------\033[0m')
    url = 'https://aq.163.com/api/p/article/getNoticeList.json'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='{"offset":0,"limit":20,"childCategory":1}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['createTime']
        time_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color(time_format, title)


def vip(number):
    print('\n\033[0;33m-----------------------唯品会SRC----------------------\033[0m')
    url = 'https://sec.vip.com/notice'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.vsrc-news-nameLink')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.news-date')[0].text
        title = notice_list[i].text
        print_color(time, title)


def wifi(number):
    print('\n\033[0;33m-----------------------WiFi万能钥匙SRC-----------------\033[0m')
    url = 'https://sec.wifi.com/api/announce'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='pageNo=0&limit=10')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['result']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['publish_time']
        title = notice_list[i]['title']
        print_color(time, title)


def zto(number):
    print('\n\033[0;33m-----------------------中通SRC------------------------\033[0m')
    url = 'https://sec.zto.com/api/notice/list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['updated_at'].split('.')[0].replace('T', ' ')
        title = notice_list[i]['title']
        print_color(time, title)

def find_div_module_cell(tag):
    if tag.name != "div":
        return False
    if not tag.has_attr("class"):
        return False
    if "index-module--feed_cell" in "\n".join(tag.attrs["class"]):
        return True
    return False

def bytedance(number):
    print('\n\033[0;33m-----------------------字节跳动SRC---------------------\033[0m')
    url = 'https://security.bytedance.com/techs'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.find_all(find_div_module_cell)
    number = min(number, len(notice_list))
    for i in range(0, number):
        mytime = notice_list[i].select('span')[0].text
        title = notice_list[i].select('h3')[0].text
        
        print_color(mytime, title)


if __name__ == '__main__':
    print('''\033[0;33m
   _____ ____  ______   _   __      __  _         
  / ___// __ \/ ____/  / | / /___  / /_(_)_______ 
  \__ \/ /_/ / /      /  |/ / __ \/ __/ / ___/ _ \\
 ___/ / _, _/ /___   / /|  / /_/ / /_/ / /__/  __/
/____/_/ |_|\____/  /_/ |_/\____/\__/_/\___/\___/ 

✔ 爬取各个SRC平台的公告通知
✔ 对2020年发布的活动通知进行红色高亮显示
✔ 【进阶版】将当天发布的公告推送到微信上，结合系统定时任务可实现SRC平台公告监测
✔ 支持的SRC平台[当前共计27家]：
360、58、阿里、阿里本地生活、爱奇艺、百度、贝壳、哔哩哔哩、菜鸟裹裹、滴滴出行、度小满、瓜子、京东、
蚂蚁金服、美团、陌陌、OPPO、平安、水滴互助、顺丰、腾讯、vivo、网易、唯品会、WIFI万能钥匙、中通、字节跳动

Version：0.1              date: 2020-11-15
Author: TeamsSix          微信公众号：TeamsSix
Blog: teamssix.com        Github: github.com/teamssix
\033[0m''')

    number = 3
    src_360(number)  # 360
    src_58(number)  # 58
    alibaba(number)  # 阿里
    ele(number)  # 阿里本地生活
    iqiyi(number)  # 爱奇艺
    baidu(number)  # 百度
    ke(number)  # 贝壳
    bilibili(number)  # 哔哩哔哩
    cainiao(number)  # 菜鸟裹裹
    didichuxing(number)  # 滴滴出行
    duxiaoman(number)  # 度小满
    guazi(number)  # 瓜子
    jd(number)  # 京东
    alipay(number)  # 蚂蚁金服
    meituan(number)  # 美团
    immomo(number)  # 陌陌
    oppo(number)  # OPPO
    pingan(number)  # 平安
    shuidihuzhu(number)  # 水滴互助
    sf_express(number)  # 顺丰
    tencent(number)  # 腾讯
    vivo(number)  # vivo
    src_163(number)  # 网易
    vip(number)  # 唯品会
    wifi(number)  # WIFI万能钥匙
    zto(number)  # 中通
    bytedance(number)  # 字节跳动
