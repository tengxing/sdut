#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Mail: tengxing7452@163.com
# Author: 阿星
# Description: 教务处爬成绩


from openpyxl import Workbook
import json
from openpyxl.compat import range


def shengcheng (id):
    std_info = []
    str = ''
    with open('data/' + id, 'r') as f:
        str = f.read()
    jsonstr = json.loads(str)
    std_info = jsonstr['subject_info']

    wb = Workbook()
    dest_filename = 'data/' + id + '.xlsx'
    ws1 = wb.active
    ws1.title = "range names"

    ws1['A1'] = '学号'
    ws1['B1'] = '姓名'
    ws1['C1'] = '专业'
    ws1['D1'] = '班级'

    ws1['E1'] = '编号'
    ws1['F1'] = '学年'
    ws1['G1'] = '学期'
    ws1['H1'] = '类型'
    ws1['I1'] = '课程名称'
    ws1['J1'] = '学分'
    ws1['K1'] = '原考成绩'
    ws1['L1'] = '补考成绩'
    ws1['M1'] = '课程绩点'
    ws1['N1'] = '学分成绩'
    for i in range(0, len(std_info)):
        vl = []
        vl.append(jsonstr['stdId'])
        vl.append(jsonstr['name'])
        vl.append(jsonstr['profession'])
        vl.append(jsonstr['class'])

        vl.append(std_info[i]['NO'])
        vl.append(std_info[i]['schoolYear'])
        vl.append(std_info[i]['semester'])
        vl.append(std_info[i]['courseType'])
        vl.append(std_info[i]['courseName'])
        vl.append(std_info[i]['credits'])
        vl.append(std_info[i]['testScore'])
        vl.append(std_info[i]['retestScore'])
        vl.append(std_info[i]['coursePoint'])
        vl.append(std_info[i]['creditsPoint'])
        ws1.append(vl)

    wb.save(filename=dest_filename)