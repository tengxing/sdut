#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: 阿星
# Description: 教务处爬成绩   感谢官方文档:http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#

import requests
import json
from bs4 import BeautifulSoup


filename = 'data.txt'
data = {
    "post_xuehao": "14110403027"
}
header = {
    "post_xuehao": "14110403027"
}
url = "http://210.44.176.116/cjcx/zcjcx_list.php"


def get_base_info(soup):
    base_info_list_soup = soup.table.table.find_all("td")
    base_info = {}

    base_info["stdId"] = base_info_list_soup[0].text.strip()
    base_info["name"] = base_info_list_soup[1].text.strip()
    base_info["sex"] = base_info_list_soup[2].text.strip()
    base_info["grade"] = base_info_list_soup[3].text.strip()
    base_info["academy"] = base_info_list_soup[4].text.strip()
    base_info["profession"] = base_info_list_soup[5].text.strip()
    base_info["class"] = base_info_list_soup[6].text.strip()
    base_info["major"] = base_info_list_soup[7].text.strip()
    base_info["level"] = base_info_list_soup[8].text.strip()
    base_info["schooling"] = base_info_list_soup[9].text.strip()

    return base_info


def get_subject_score_info(subject_info_list_soup):
    subject_info = {}

    subject_info["NO"] = subject_info_list_soup[0].text.strip()
    subject_info["schoolYear"] = subject_info_list_soup[1].text.strip()
    subject_info["semester"] = subject_info_list_soup[2].text.strip()
    subject_info["courseType"] = subject_info_list_soup[3].text.strip()
    subject_info["courseId"] = subject_info_list_soup[4].text.strip()
    subject_info["courseName"] = subject_info_list_soup[5].text.strip()
    subject_info["hours"] = subject_info_list_soup[6].text.strip()
    subject_info["credits"] = subject_info_list_soup[7].text.strip()
    subject_info["assessmentMethod"] = subject_info_list_soup[8].text.strip()
    subject_info["testScore"] = subject_info_list_soup[9].text.strip()
    subject_info["retestScore"] = subject_info_list_soup[10].text.strip()
    subject_info["coursePoint"] = subject_info_list_soup[11].text.strip()
    subject_info["creditsPoint"] = subject_info_list_soup[12].text.strip()

    return subject_info


def get_subject_info(soup):
    subject_info_list = []
    subject_list_soup = soup.table.find_all('table')[2].find_all('tr')[1::]
    for subject_soup in subject_list_soup:
        subject_info = get_subject_score_info(subject_soup.find_all('td'))
        subject_info_list.append(subject_info)
    return subject_info_list


def get_json_str(dict, ensure_ascii=False):
    return json.dumps(dict, ensure_ascii=ensure_ascii)


def write_file(filename, str):
    with open(filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！ 'r'表示读数据， 'a'表示追加数据
        f.write(str)
        f.close()


def get_std_info(data = data):
    text = requests.post(url, data=data, headers=header).text
    soup = BeautifulSoup(text, 'html.parser')
    # 基础信息
    base_info = get_base_info(soup)
    # 学科信息
    subject_list_info = get_subject_info(soup)

    base_info['subject_info'] = subject_list_info

    json_str = get_json_str(base_info);
    return json_str

#write_file(filename,json_str)




