#!/usr/bin/env python
# coding: utf-8

# In[3]:


m = float(input('Nhập vào số cần kiểm tra'))

if m%2==0:
    print('Số đã nhập là số chẵn')
elif m%2==1:
    print('Số đã nhập là số lẻ')
else:
    print('Số đã nhập không phải là số tự nhiên')

