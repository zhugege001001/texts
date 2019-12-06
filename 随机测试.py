# __*__coding:utf-8__*__

import requests
from bs4 import BeautifulSoup
import re

url = 'http://movie.douban.com/top250/'

"""获取url地址页面内容"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}
data = requests.get(url, headers=headers).content.decode('utf-8')

soup = BeautifulSoup(data, 'html.parser')
ol = soup.find('ol', class_='grid_view')
name = []  # 名字
star_con = []  # 评价人数
score = []  # 评分
info_list = []  # 短评

#sentence = re.compile('我是一个大傻逼')

for i in ol.find_all('li'):
    detail = i.find('div', attrs={'class': 'hd'})
    movie_name = detail.find(
        'span', attrs={'class': 'title'}).get_text()  # 电影名字
    level_star = i.find(
        'span', attrs={'class': 'rating_num'}).get_text()  # 评分
    star = i.find('div', attrs={'class': 'star'})
    star_num = star.find(text=re.compile('评价'))  # 评价

    info = i.find('span', attrs={'class': 'inq'})  # 短评
    if info:  # 判断是否有短评
        info_list.append(info.get_text())
    else:
        info_list.append('无')
    score.append(level_star)

    name.append(movie_name)
    star_con.append(star_num)

page = soup.find('span', attrs={'class': 'next'}).find('a')  # 获取下一页

print(page)

#print(type(sentence))
