# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:39:15 2019

@author: Admin
"""

import urllib.request
from bs4 import BeautifulSoup
import csv
# specify the url
urlpage =  'https://vnexpress.net/kinh-doanh/100-noi-lam-viec-tot-nhat-viet-nam-nam-2017-3726338-p2.html'
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
soup_string = str(soup)
print (soup_string)
import pika
import pika.compat
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#connection = pika.AsyncoreConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='top100')

channel.basic_publish(exchange='', routing_key='top100', body=soup_string)
print(" [x] Sent 'Top 100!'")
connection.close()