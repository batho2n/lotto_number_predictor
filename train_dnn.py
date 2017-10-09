#!/usr/bin/python
# -*- coding: utf-8 -*-

# File: train_dnn.py
# Date: 2017.10.09
# Author: batho2n
# Function: Training DNN using Saved Lotto Number

import numpy as np
import matplotlib.pyplot as plt

lotto_file_name = "lotto_number.txt"

# lotto_number.txt에서 로또번호들을 읽어들여 numpy matrix 변수로 저장
def Read_Lotto_Numbers():
    try:
        with open(lotto_file_name, 'r') as f:
            total_lotto_numbers = f.readlines()
    except IOError as err:
        print 'Do >python lotto_number_save.py'
        exit(1)
    else:
        lotto_numbers = []
        for line in total_lotto_numbers:
            lotto_numbers.append(line.split('\n')[0].split(','))

        return np.asarray(lotto_numbers)

def main():
    # lotto 번호 읽기
    np_lotto = Read_Lotto_Numbers()
    
    img = np.zeros(49)
    for i in np_lotto[0]:
        img[int(i)-1] = 1.0 
        
    img = np.reshape(img, (7,7))
   
    plt.imshow(img, cmap = 'gray', interpolation='nearest')
    plt.show()
    

if __name__ == "__main__":
    main()
