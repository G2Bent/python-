#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
def sig(x):
    '''Sigmoid函数
    input: x(mat):feature * w
    output: sigmoid(x)(mat): Sigmoid值
    exp相当于函数中的e
    '''
    return 1.0 / (1+np.exp(-x))

print(sig(0))