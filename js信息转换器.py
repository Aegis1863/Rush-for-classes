# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 01:15:41 2020

@author: LiSunBowen
"""

def tran(t):
    if t!='':
        p=dict([line.split(": ",1) for line in t.split("\n")])
        return p
    else:
        return t
t=str(input('输入：'))
p=tran(t)
print('\n{}'.format(p))