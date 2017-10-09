#!/usr/bin/python
# -*- coding: utf-8 -*-

# File: lotto_number_save.py
# Date: 2017.10.08
# Author: batho2n
# Function: Save Lotto Number to lotto_number.txt using webcrwawling

import requests
from bs4 import BeautifulSoup

last_lotto_url = "http://www.nlotto.co.kr/gameResult.do?method=byWin"
lotto_url="http://www.nlotto.co.kr/gameResult.do?method=byWin&drwNo="
lotto_file_name = "lotto_number.txt"

# 최근 당첨 번호 페이지를 열어 가장 마지막 회차 숫자 검색
def Find_Last_Index():
    resp = requests.get(last_lotto_url)
    soup = BeautifulSoup(resp.text,"lxml")
    tag_line = str(soup.find('meta',{'id':'desc', 'name':'description'}))
    str_num = tag_line.split(' ')[2]
    index = int(str_num.split('회')[0])
    return index

# lotto_number.txt에 저장된 라인수를 체크한다.
def Find_File_Index():
    try:
        f = open(lotto_file_name, 'r')
    except IOError as err:
        return 0
    else:
        total_lotto_numbers = f.readlines()
        f.close()
        return len(total_lotto_numbers)

# lotto_number.txt에 웹에서 가장 최신 회차까지 번호만 읽어서 저장한다.
def Save_Lotto_Numbers(index):
    with open(lotto_file_name, 'w') as f:
        for i in range(index):
            resp = requests.get(lotto_url + str(i+1))
            soup = BeautifulSoup(resp.text,"lxml")
            tag_line = str(soup.find('meta',{'id':'desc', 'name':'description'}))
            list_num = tag_line.split(' ')[4].split('+')[0].split(',')
            str_num = ','.join(list_num)
            f.write(str_num + '\n')

def main():
    # 웹에서 가장 최근 회차  찾기
    last_lotto_index = Find_Last_Index()
    print 'Web Last Index: ' + str(last_lotto_index)
   
    # lotto_nuber.txt에 저장된 회차 찾기
    file_lotto_index = Find_File_Index()
    print 'File Index: ' + str(file_lotto_index)

    # 웹과 파일이 같으면 끝, 다르면 웹 크롤링을 통해 새롭게 저장
    if last_lotto_index == file_lotto_index:
        print 'Finish Saving New Lotto Numbers'
    else:
        Save_Lotto_Numbers(last_lotto_index)
        print 'Finish Checking New Lotto Numbers'

if __name__ == "__main__":
    main()
