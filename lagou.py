#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from Company import Company
from Position import Position
import write_to_db
import re

# 关键词，工作经验，学历，月薪，全职或兼职，发布时间
import sys

def grab_position(keyword, gj='', xl='', yx='', gx='', st='', lc='', workAddress='', city='全国'):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    url = "http://www.lagou.com/jobs/list_" + keyword
    params = {'spc': 1, 'pl': "", 'xl': xl, 'yx': yx, 'gx': gx, 'st': st, 'labelWords': '', 'city': city,
              'requestId': ""}
    list = requests.get(url, params=params)
    parser = BeautifulSoup(list.content)

    # print list.content
    posistions = []
    companys = []

    pos_html = parser.find_all("div", class_="hot_pos_l")
    cmp_html = parser.find_all("div", class_="hot_pos_r")
    for i in range(len(pos_html)):
        p2 = BeautifulSoup(repr(pos_html[i]))
        cmp_parser = BeautifulSoup(repr(cmp_html[i]))
        p = Position()
        c = Company()

        # 抓取职位信息
        spans = p2.find_all('span')
        p.salary = spans[1].text
        p.experience = spans[2].text
        p.edu = spans[3].text
        p.candy = spans[4].text
        p.name = pos_html[i].div.a.text
        p.place = pos_html[i].div.span.text
        p_url = pos_html[i].div.a['href']
        p_detail = requests.get(p_url)
        detail_parser = BeautifulSoup(p_detail.content)
        p.detail = detail_parser.find_all("dd", class_="job_bt")[0].text

        # 抓取公司信息
        hot_pos_r = cmp_parser.find_all("span")
        if len(hot_pos_r) == 4:
            c.field = hot_pos_r[0].text
            c.founder = hot_pos_r[1].text
            c.funding = hot_pos_r[2].text
            c.extent = hot_pos_r[3].text
        elif len(hot_pos_r) == 3:
            c.field = hot_pos_r[0].text
            c.funding = hot_pos_r[1].text
            c.extent = hot_pos_r[2].text

        # 关联
        tmp = cmp_parser.find_all("a")
        c_id_a = tmp[1]
        c.name = c_id_a.text
        c_id = c_id_a['href']
        c_id = re.findall('\d+', c_id)
        cmp_page = requests.get(c_id_a['href'])
        page_parser = BeautifulSoup(cmp_page.content)
        intro = page_parser.find_all("div", class_="c_intro")
        if len(intro) > 0:
            c.mainPage = intro[0].text
        else:
            c.mainPage = '暂无简介'
        p.cmp_id = c_id
        c.id = c_id
        write_to_db.add_pos(p, 'position')
        write_to_db.add_pos(c, 'company')
    print len(posistions)

if __name__ == '__main__':
    # grab_position("产品经理")
    grab_position("PHP")
    grab_position("IOS")
    grab_position("Android")
    grab_position("HTML")
    grab_position("测试")
    grab_position("架构师")
    grab_position("运营")
    grab_position("UI")
    grab_position("前端开发")
    grab_position("游戏")
