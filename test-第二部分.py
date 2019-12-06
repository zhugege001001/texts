# __*__coding:utf-8__*__

from bs4 import BeautifulSoup
import re
import requests

DOWNLOAD_URL = 'http://movie.douban.com/top250/'
data = requests.get(DOWNLOAD_URL).content

# 定义一个函数，一个参数，使用BeautifulSoup获得需要的内容（名字，评分，评价，短评等内容）
def get_li(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    ol = soup.find('ol', class_='grid_view')
    name = []  # 名字
    star_con = []  # 评价人数
    score = []  # 评分
    info_list = []  # 短评
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

    if page:
        return name, star_con, score, info_list, DOWNLOAD_URL + page['href']
    return name, star_con, score, info_list, None


if __name__ == '__main__':
    print(get_li(data))

