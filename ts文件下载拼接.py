# --*-- coding:utf-8--*--
# 2019/11/30

import os
import requests

"""
下载M3U8文件里的所有片段
"""


def download(url):
    download_path = os.getcwd() + "\download"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    all_content = requests.get(url).text  # 获取M3U8的文件内容
    file_line = all_content.split("\r\n")  # 读取文件里的每一行
    # 通过判断文件头来确定是否是M3U8文件
    if file_line[0] != "#EXTM3U":
        raise BaseException(u"非M3U8的链接")
    else:
        unknow = True  # 用来判断是否找到了下载的地址
        for index, line in enumerate(file_line):
            if "EXTINF" in line:
                unknow = False
                # 拼出ts片段的URL
                pd_url = file_line[index + 1]
                res = requests.get(pd_url)
                # c_fule_name = str(index)+ '.ts'
                c_fule_name = "%(index)02d" % {'index': index} + '.ts'
                with open(download_path + "\\" + c_fule_name, 'ab') as f:
                    f.write(res.content)
                    f.flush()
        if unknow:
            raise BaseException("未找到对应的下载链接")
        else:
            print("下载完成")


# 合并的时候名字要有规律，从前往后排
def merge_file(path):
    os.chdir(path)
    os.system("copy /b * new.mp4")


if __name__ == '__main__':
    download(
        "http://pl-ali.youku.com/playlist/m3u8?vid=XMTQ2NzQyMjY1Ng&type=hd2&ups_client_netip=0156f41f&utid=cKsgFHBPZVECAXUjhXp%2Bu8Ip&ccode=0502&psid=244b3690aa7b9cd1c11c2f6c8ae6582b&duration=90&expire=18000&drm_type=1&drm_device=7&ups_ts=1547012701&onOff=0&encr=0&ups_key=9a7e324bb33543281964c43caa15dc80")
    merge_file(os.getcwd() + "\download")
''''————————————————
版权声明：本文为CSDN博主「H - KING」的原创文章，遵循
CC
4.0
BY - SA
版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / liujiayu2 / article / details'''