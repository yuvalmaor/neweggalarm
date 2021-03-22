import sys
import random
from selenium import webdriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import re
import time
import json
from datetime import datetime


def main():
    items=66#change to amount of items in page if dont work
    a=0
    v=items
    vt=items
    while(v==vt and v==items):
        time.sleep( random.randint(50, 55))
        link="https://www.newegg.com/global/il-en/p/pl?N=101613484%20600358543%20600494828%20601357261%20601294831%20600499109%20601110192%20601326002%208000%20601357247%20601359415%20601303641%20601303642%20600029797%20601357250%20601359427%20601341487&Order=1&PageSize=96"
        #link="https://www.newegg.com/p/pl?N=101613484%20600358543%20600494828%20601357261%20601294831%20600499109%20601110192%20601326002%208000%20601357247%20601359415%20601303641%20601303642%20600029797%20601357250%20601362404%20601359427%20601341487&Order=1&PageSize=96"
        #link="https://www.newegg.com/global/il-en/p/pl?N=101613484%20600358543%20600494828%20601357261%20601294831%20600499109%20601110192%20601326002%208000%20601357247%20601359415%20601303641%20601303642%20600029797%20601359427%20601341679%20601357250%20601361654&Order=1&PageSize=96"
        #link="https://www.newegg.com/global/il-en/p/pl?N=101613499%20601359163"
        #link="https://www.newegg.com/global/il-en/p/pl?N=101613484%20600358543%20600494828%20601357261%20601294831%20600499109%20601110192%20601326002%208000%20601357247%20601359415%20601303641%20601303642%20600029797%20601359427%20601341679%20601357250&Order=1&PageSize=96"
        #link="https://www.newegg.com/global/il-en/p/pl?N=101613484%208000%20601321572%20601341679%20601359427%20601303641%20601303642%20601183677%20601361654%20601359415%20601357250%20601357247&Order=3&PageSize=96"
        #link="https://www.newegg.com/global/il-en/p/pl?N=101613499%20601359163&d=CPU&isdeptsrh=1"
        #link="https://www.newegg.com/global/il-en/p/pl?N=101613484%208000%20601321572%20601341679%20601359427%20601303641%20601303642%20601183677%20601359415%20601357250%20601357247&Order=3&PageSize=96"
        #link="https://www.newegg.com/global/il-en/p/pl?N=101613484%20600358543%20600494828%20601357261%20601294831%20600499109%20601110192%20601326002%208000%20601357247%20601359415%20601303641%20601303642%20600029797&Order=1"
        r = requests.get(link)
        a=r.text
        d=a.find("item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
        a=a[d:]
        d=a.find("monetate-content-1")
        a=a[:d]
        #print(func(a))
        #printlisttwo(func(a))
        s=sinun(func(a))
        #print("num of links is"+str((s)))
        #printlist(sinun(func(a)))
        stocklist=stock(a)
        #print(makedic(s,stocklist))
        #print(json.loads(r.json()))
        print("num of links is"+str(len(s)))
        v=len(s)
        vt=len(stocklist)
        print("num of links is"+str(len(stocklist)))
        #printlisttwo(sinun(func(a)))
        #printlisttwo(func(a))
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        
        #print(a)
        #os.system('cls')
    openbrowser(s[0],link)

def func(a):
    ret = re.findall(r"href=\"[^\"\>]*\"", a)
    return ret

def printlist(a):
    for i in a:
        print(i)

def printlisttwo(a):
    for j in range(200):
        for i in a:
            if(len(i)==j):
                print(i)

def sinun(a):
    b=[]
    for i in a:
        #print(i[0:42])
        if(i[0:42]=='href="https://www.newegg.com/global/il-en/' and (i not in b) and i.find("FeedbackTab")==-1 and i.find("Item")!=-1):
            b.append(i)

    return b

def makedic( a,b):
    ret={}
    for i in range(len(a)):
        ret[a[i]]=b[i]
    return ret
def stock(a):
    c=0
    ret=[]
    #print(a.find('class="item-promo-icon"')) 
    d= a.find('class="item-promo-icon"')
    while(d!=-1):
        #print(a[d:d+40])
        ret.append(a[d+27:d+40])
        c=c+1
        a=a[d+40:]
        d= a.find('class="item-promo-icon"')

    
    print("num of links is:"+str(c))
    return ret

def openbrowser(a,link):
    print(a[6:-1])
    print("")

    #a='https://www.newegg.com/global/il-en/p/pl?N=101613484%208000%20601321572%20601341679%20601359427%20601303641%20601303642%20601183677%20601361654%20601359415%20601357250%20601357247&Order=3&PageSize=96'
    #b='https://www.newegg.com/global/il-en/p/pl?N=101613484%208000%20601321572%20601341679%20601359427%20601303641%20601303642%20601183677%20601361654%20601359415%20601357250%20601357247&Order=3&PageSize=96'
    browser  = webdriver.Chrome(ChromeDriverManager().install())
    #browser.get(b)#run
    browsera  = webdriver.Chrome(ChromeDriverManager().install())
    browsera.get(a[6:-1])
    time.sleep(8)
    #element = browsera.find_element_by_css_selector('button.btn btn-primary btn-wide')
    element = browsera.find_elements_by_css_selector('button.btn.btn-primary.btn-wide')
    #element = browsera.
    #find_element_by_class("btn btn-primary btn-wide")Add to cart 
    #class="btn btn-primary btn-wide"
    browser.get(link)
    try:
        element[0].click()
    except:

        browser.get(link)
    browser.get(link)
    print(len(element))
    #element[0].submit()
    print(a[6:-1])

    while(1):
        i=0
main()