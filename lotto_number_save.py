# File: lotto_number_save.py
# Date: 2017.10.08
# Author: batho2n
# Function: Save Lotto Number to lotto_number.txt using webcrwawling

#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def Find_Last_Index():
    resp = requests.get("http://www.nlotto.co.kr/gameResult.do?method=byWin")
    soup = BeautifulSoup(resp.text,"lxml")
    tag_line = str(soup.find('meta',{'id':'desc', 'name':'description'}))
    str_num = tag_line.split(' ')[2]
    index = (str_num.split("회"))
    print index
    return index

def main():
    last_web_index = Find_Last_Index()

    basic_url="http://www.nlotto.co.kr/gameResult.do?method=byWin&drwNo="
    resp = requests.get(basic_url + '1')
    soup = BeautifulSoup(resp.text,"lxml")
    tag_line = str(soup.find('meta',{'id':'desc', 'name':'description'}))
    str_num = tag_line.split(' ')[4]
    str_num = str_num.split('+')[0]
    str_num = str_num.split(',')

if __name__ == "__main__":
    main()
