#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from Preach import Preach
import write_to_db


def grab_preach():
    baseURL = "http://xjh.haitou.cc"

    index = requests.get(baseURL)
    parser = BeautifulSoup(index.content)

    pagination = parser.select(".paginate_button")

    preachs = []

    for button in pagination:
        # print button['class']
        if button['class'][-1] == 'active':
            url = baseURL
        elif len(button['class']) == 1:
            url = baseURL + button.a['href']

        if button['class'][-1] == 'active' or len(button['class']) == 1:

            index = requests.get(url)
            parser = BeautifulSoup(index.content)

            titles = parser.find_all("td", class_="preach-tbody-title")
            holdtimes = parser.find_all("td", class_="text-center xjh-holdtime")
            posttimes = parser.find_all("td", class_="text-center xjh-posttime")
            clicks = parser.find_all("td", class_="text-right xjh-click")
            places = parser.find_all("td", class_="preach-tbody-addre xjh-place")

            for i in range(len(titles)):
                preach = Preach()
                preach.set_title_school(titles[i].a['title'])
                preach.origin_url = baseURL + titles[i].a['href']
                preach.hold_time = holdtimes[i].span.text
                preach.post_time = posttimes[i].span.text
                preach.click = clicks[i].text
                preach.place = places[i].text
                preachs.append(preach)
                write_to_db.add_pos(preach, 'preach')

    return preachs


if __name__ == '__main__':
    p = grab_preach()
    print len(p)
    for i in p:
        i.detail()



