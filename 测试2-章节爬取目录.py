# --*-- encoding:utf-8 --*--
# 爬取小说，独立完成，循序渐进


import requests
from bs4 import BeautifulSoup

url = 'https://www.jx.la/book/11961/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
html = requests.get(url,headers).text
soup = BeautifulSoup(html,'html.parser')

bookname = soup.h1.get_text()
intro = soup.find_all('div',id='intro')
#print(bookname +'\n' + str(intro))   这里有个地方一直没绕过去，就是如何直接提取类属性下的文字内容str(intro)

list = soup.find('div', id='list')

f = open("./目录.doc",'w')

for i in list.find_all('dd'):
    chapter_list = i.get_text() +'\n'+ "https://www.jx.la" + i.a['href'] + '\n'
    f.write(chapter_list+'\n')

#print(i.a['href'])
# print(i.get_text() + "https://www.jx.la" + i.a['href'])

'''  还剩下把目录前面部分重复的章节目录去掉，问题在于获取到值 是bs类型 或者 string类型， 怎么去计算它开始的地方？？？  '''




