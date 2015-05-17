#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Preach(object):
    title = None
    school = None
    hold_time = None
    place = None
    post_time = None
    click = None
    origin_url = None

    def __init__(self, title=None, school=None, hold_time=None, place=None,
                 post_time=None, click=None, origin_url=None):
        if title is None:
            self.title = "无"
        if school is None:
            self.school = "无"
        if hold_time is None:
            self.hold_time = "无"
        if place is None:
            self.place = "无"
        if post_time is None:
            self.post_time = None
        if click is None:
            self.click = 0
        if origin_url is None:
            self.origin_url = "无"

    def set_title_school(self, str):
        if str is None:
            str = "error"
        else:
            a = str.split("\n")
            self.title = a[0]
            self.school = a[1]

    def detail(self):
        print(self.title + " " + self.origin_url + " " + self.place + " " + self.click + " " + self.hold_time + " " + self.school)