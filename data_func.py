#!/usr/local/bin/python3
# _*_ coding:utf8 _*_

import requests
import time
from bs4 import BeautifulSoup

# ======================= crawler ============================
def html():
    # === inicialization ===

    # url init
    main_url = ['http://ipsmold.wicp.io:81/' ,'http://103.244.103.154/']
    login_url =['http://ipsmold.wicp.io:81/login/x', 'http://103.244.103.154/login/x']
    url = ['http://ipsmold.wicp.io:81/Network/ac_user',"http://103.244.103.154/Network/ac_user"]

    # username and password to be pass into the http POST method
    payload = {'user':'temp','pass':'4&4+?rpw%akU!AKG'}

    # open a session to maintain the cookie and other information
    s = requests.Session()

    # number array init
    number = []

    # === get the data from url ===
    # loop for the two different AP
    for i in range(len(url)):

        # access the main url
        s.get(main_url[i])

        # post uername and password to login
        s.post(login_url[i],data=payload)

        # get the return content
        r = s.get(url[i])

        # parse html to extract necessary data
        html_markup = BeautifulSoup(r.text,'html.parser')
        number.append(len(html_markup.find_all('dd')) - 1)

    # === create database ===
    # file init
    with open('database','r+') as f:

        # read the content
        old = f.read()

        # go to the 1st byte in the file
        f.seek(0)

        # timestamp for keeping track
        new_data = time.strftime("%m-%d,%H:%M:%S",time.localtime())+','

        # loop to detemine where to insert , or newline
        for i in range(len(number)):
            if i == 0:
                new_data = new_data + str(number[i]) + ','
            elif i == 1:
                new_data = new_data + str(number[i]) + '\n'

        # add new data to the database
        f.write(new_data + old)

    return number

# ========== function to extract data from database ==========
def extract(n):
    # === initialization ===
    # return array init
    line = []

    # counter init
    count = n

    # file init
    data = open('database','r')

    # === extraction ===
    for i in data:

        # exit information
        if n < 1 :
            break

        # get one number
        tmp = i.replace('\n','').split(',')

        # add it to line[]
        line.append(tmp)

        # counter updating
        n-=1
    return line

# ======== function to estimate the nubmer of people =========
# estimate by calculating the weighed average over a previous time period
# data near the request time have larger weights

# data set A
def ma_A(periods):

    # get a data array with length periods from the database
    data = extract(periods)

    # weight & average init
    weight,avg=periods,0

    # loop to sum up the weighed data
    for i in data:
        avg+=(int(i[3])*weight)
        weight-=1
        if weight == 0:
            break

    # weighed average = (weighed sum) / (sum of weights)
    # sum of weights = 1 + 2 +3 + ... + periods = (periods * (periods +1) / 2)
    avg= 2 * avg / (periods*(periods+1))
    return int(avg)


# data set B (same calculation)
def ma_B(periods):
    data = extract(periods)
    weight,avg=periods,0
    for i in data:
        avg+=(int(i[2])*weight)
        weight-=1
        if weight == 0:
            break
    avg= 2 * avg / (periods*(periods+1))
    return int(avg)
