# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:55:29 2022

@author: perry
"""

import pymysql
dbsetting ={
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456789',
    'db':'jobs',
    'charset':'utf8'
    
    
    
    }

conn=pymysql.connect(**dbsetting) 

