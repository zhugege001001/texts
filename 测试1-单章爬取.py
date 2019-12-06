# --*-- encoding:utf-8 --*--
# 爬取小说，独立完成，循序渐进
import parser

import requests
import selector as selector
from bs4 import BeautifulSoup

'''
第一步：爬取小说单独章节整个页面的HTML文档的前端源码
'''

chapter_url = 'https://www.jx.la/book/11961/6501006.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
chapter_html = requests.get(chapter_url, headers).text
soup = BeautifulSoup(chapter_html, 'html.parser')
chapter_title = soup.h1.get_text()
chapter_content = soup.find('div', id='content')
chapter_content_text = chapter_content.text.replace('\xa0', '\n')

with open(chapter_title+'.doc','w',encoding='utf-8') as fp:
    fp.write(chapter_title + chapter_content_text)

'''上述部分，完成整个单章页面小说内容的爬取'''
'''if __name__=="__main__":
    main()'''
