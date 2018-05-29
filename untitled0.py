# -*- coding: utf-8 -*-
"""
Created on Mon May 28 00:21:12 2018

@author: 12260
"""

import requests
import lxml.etree as etree
import os
import shutil
from urllib.parse import urljoin
source_dir = 'https://bing.ioliu.cn/'
base_dir = r"F:\爬虫图片\bing壁纸"
if os.path.exists(base_dir) == False:
    os.makedirs(base_dir)
r = requests.get(source_dir)
html = etree.HTML(r.text)
imgs = html.xpath("//a[@class='ctrl download']")

for img in imgs:
    src = img.get("href")
    with open(os.path.join(base_dir, str(imgs.index(img))+".jpg"), "wb") as f:
        obj = requests.get(urljoin(source_dir, src))
        print(obj.status_code)
        if obj.status_code == 200:
            obj.raw.decode_content = True
            f.write(obj.content)
            #shutil.copyfileobj(obj.raw, f)   
            print(f.name, "已经保存！")
        else:
            print(f.name, "下载失败，什么咧！")
#help(str)
#help(etree)
#print(r.text)
