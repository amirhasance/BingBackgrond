#!/usr/bin/python3
import requests;
import re
import html
import html5lib
import bs4
from bs4 import BeautifulSoup;
from os import getcwd
from html import *

BingUrl = "https://www.bing.com"

response = requests.get(BingUrl)

if  not response.ok :
   print("Bing is out of reach or check Internet connection")
   exit()

page = BeautifulSoup(response.content , 'html5lib')

#  ///////////////////print(page.prettify())

tab = str(page.findAll('div' , attrs={'class' : 'img_cont'}))

print("tab = %s" %tab)

index1 = str(tab).find("url")+4

tab1 = tab[index1:]

index2 = str(tab).find("><")-2



print("index1 = %s and index2 = %s"%(index1 , index2))

print(tab[index1:index2])

image_url = BingUrl + tab[index1 : index2] ;

print(image_url)

image_response = requests.get(image_url)

import os

current_path  = os.getcwd();

imagefile = open(current_path+"/a.jpg" , "wb")

imagefile.write(image_response.content)





