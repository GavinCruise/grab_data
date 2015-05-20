#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import sys


def add_pos(pos, types):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='root123', db='jobs', port=3306, charset='utf8')
        cur = conn.cursor()

        if types == "position":
            add_position = """insert into job_position(candy,detail,education,experience,name,place,salary,company_id) values (%s,%s,%s,%s,%s,%s,%s,%s)"""
            data_position = (
                pos.candy.encode('utf-8'), pos.detail.encode('utf-8'), pos.edu.encode('utf-8'),
                pos.experience.encode('utf-8'),
                pos.name.encode('utf-8'), pos.place.encode('utf-8'), pos.salary.encode('utf-8'),pos.cmp_id)
            cur.execute(add_position, data_position)
        elif types == 'company':
            add_company = """insert into job_company(id,creator,extent,field,funding,name,main_page) values (%s,%s,%s,%s,%s,%s,%s)"""
            data_company = (
                pos.id, pos.founder,
                pos.extent.encode('utf-8'), pos.field.encode('utf-8'),
                pos.funding.encode('utf-8'),
                pos.name.encode('utf-8'),pos.mainPage.encode('utf-8'))
            cur.execute(add_company, data_company)
        elif types == 'preach':
            add_preach = """insert into job_preach(click,origin_url,post_time,school_name,place,hold_time,title) values (%s,%s,%s,%s,%s,%s,%s)"""
            data_preach = (
                pos.click.encode('utf-8'), pos.origin_url.encode('utf-8'),
                pos.post_time, pos.school.encode('utf-8'), pos.place.encode('utf-8'),
                pos.hold_time.encode('utf-8'), pos.title.encode('utf-8'))
            cur.execute(add_preach, data_preach)

        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])