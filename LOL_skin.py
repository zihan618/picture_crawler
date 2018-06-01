
# coding: utf-8

# In[143]:


import requests
from lxml import etree
import json, os


# In[145]:


heroes = requests.get(r"http://lol.qq.com/biz/hero/champion.js")
if heroes.status_code != 200:
    print(网页加载失败)
    exit()
start_str = '{"266":"Aatrox","103"'
end_str = ',"data":{"Aatrox":{"id":"Aatrox"'
heroes = heroes.text[heroes.text.index(start_str): heroes.text.index(end_str)]
heroes = json.loads(heroes)
for i in heroes:
    print(heroes[i])


# In[159]:


end_str = ',"info":'
start_str = '"skins"'
base_source = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big{0}.jpg'
base_dir = r"F:\爬虫图片\lol皮肤"
if os.path.exists(base_dir) == False:
    os.makedirs(base_dir)
for i in heroes:
    hero_name = heroes[i]
    
    hero = requests.get(r"http://lol.qq.com/biz/hero/" + hero_name + '.js')
    if hero.status_code != 200:
        print(hero_name, "下载失败！")
        continue
    
    this_dir = os.path.join(base_dir, hero_name)
    if os.path.exists(this_dir) == False:
        os.mkdir(this_dir)
    
    text = hero.text
    text = text[text.index(start_str) + len(start_str) + 1: text.index(end_str)  ]
    
    skins = json.loads(text, encoding = hero.encoding)
    for i in skins:
        pic_path = os.path.join(this_dir, i["name"].replace(" ", "-") + '.jpg')
        #print(pic_path)
        with open(str(pic_path), "wb") as f:
            pic = requests.get(base_source.format(i["id"]))
            if(pic.status_code != 200):
                print(pic.url, "下载失败")
            f.write(pic.content)
    print(hero_name, '皮肤下载完毕')
   


# In[156]:




