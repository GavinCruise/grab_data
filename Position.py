#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Position:
    name = None
    salary = None
    experience = None
    edu = None
    candy = None
    place = None
    detail = None
    cmp_id = None

    def __init__(self):
        pass

    # print 方法默认调用
    def __str__(self):
        return "%s,%s,%s,%s,%s" % (self.place, self.name, self.detail, self.candy, self.cmp_id)