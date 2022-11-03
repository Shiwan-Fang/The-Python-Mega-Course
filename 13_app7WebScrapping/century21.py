#!/usr/bin/env python
# coding: utf-8

# In[62]:


import requests
from bs4 import BeautifulSoup

r=requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/") #srap the html code from the webpage
c=r.content

soup=BeautifulSoup(c,"html.parser") #beautify the html code

all=soup.find_all("div", {"class": "propertyRow"}) #find all the div elements with it's class called propertyRow

len(all) # which means the page has 10 div with class:propertyRow

all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
#if we use find method, we will get the tag element(just like the html code). If we use find_all method, we will get a lsit.
#all[0].find("h4",{"class":"propPrice"}).text  is a str, you can use type() method to check

page_nr=soup.find_all("a",{"class":"Page"})[-1].text #不通过观察每一页的链接如何变化，而是直接抓取html中的信息，直接告诉我们有多少页


# In[63]:


l=[]#store all tne info you scrapped in the dictionary
# base_url="https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
#不是复制全部网址，可以看看网页发现规律。这个网站的规律是每点下一页，s=后面的数字都会加10。
for page in range(0,int(page_nr)*10,10): #0到30，以10为单位迭代
    print(base_url+str(page)+".html")
    r=requests.get(base_url+str(page)+".html")#抓取这个网站每一页的html code
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div", {"class": "propertyRow"}) #find all the div elements with it's class called propertyRow
    for item in all:
        d={} 
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        d["Adress"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        try: #如果不用try，某一个没有这个属性的话这个一整条都不会加到字典中
            d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        except:
            d["Locality"]=None
        try:
            d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text #get the number of beds, if the house doesn't have beds, then pass
        except:
            d["Beds"]=None

        try:
            d["Ares"]=item.find("span",{"class":"infosqFT"}).find("b").text #get the number of FullBath, if the house doesn't have beds, then pass
        except:
            d["Ares"]=None

        try:
            d["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text #get the number of FullBath, if the house doesn't have beds, then pass
        except:
            d["Full Baths"]=None

        try:
            d["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text #get the number of HalfBath, if the house doesn't have beds, then pass
        except:
            d["Half Baths"]=None    

        for column_group in item.find_all("div", {"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}),column_group.find_all("span",{"class","featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text  #we only need the info of lot size
        l.append(d)


# In[64]:


import pandas
df=pandas.DataFrame(l) #switch the dictionary to a graph


# In[65]:


df


# In[66]:


df.to_csv("Output.csv") #put the data to a csv file

