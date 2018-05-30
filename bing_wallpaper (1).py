
# coding: utf-8

# In[5]:


import requests
import lxml.etree as etree
import os
import hashlib
from urllib.parse import urljoin


# In[6]:


source_dir = 'https://bing.ioliu.cn/'
page = "?p="
now_page = 1

base_dir = r"F:\爬虫图片\bing壁纸"
if os.path.exists(base_dir) == False:
    os.makedirs(base_dir)
download_nums = len(os.listdir(base_dir))
found_nums = 0


# In[7]:


r = requests.get(source_dir)
html = etree.HTML(r.text)
pages_num = html.xpath("//div[@class='page']")
pages_num = pages_num[0].xpath("./span")[0].xpath("./text()")[0]
pages_num = pages_num[pages_num.index(r'/')+1:]
pages_num = int(pages_num)
print('总共有', pages_num, '页')


# In[8]:


while(now_page <= pages_num):
    r = requests.get(urljoin(source_dir, page+str(now_page)))
    print('现在开始下载', r.url)
    html = etree.HTML(r.text)
    imgs = html.xpath("//a[@class='ctrl download']")
    for img in imgs:
        found_nums += 1
        if found_nums <= download_nums:
            continue
        src = img.get("href")
        pic_number = len(os.listdir(base_dir))
        obj = requests.get(urljoin(source_dir, src))
        if obj.status_code != 200:
            print(f.name, "下载失败，什么咧！")
        else:  
            with open(os.path.join(base_dir, str(pic_number)+".jpg"), "wb") as f:
                obj.raw.decode_content = True
                f.write(obj.content) 
                print(f.name, "已经保存！")
    print("第{0}页的壁纸已经下载完毕！".format(now_page))
    now_page += 1

