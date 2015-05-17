#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.lagou.com/")
soup = BeautifulSoup(r.content)

#print soup.html.head.title
categroy0 = soup.select(".mainNavs h2")    #职位大分类
categroy1 = soup.select(".menu_sub dt a")

print(categroy1)



