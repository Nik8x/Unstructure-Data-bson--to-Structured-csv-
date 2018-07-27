
# coding: utf-8

# In[1]:


import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import io
import pymongo
import bson     # this is installed with the pymongo package
import matplotlib.pyplot as plt


# In[5]:


path = os.getcwd() + '/books.bson'
with open(path,'rb') as f:
 data1 = bson.decode_all(f.read())


# In[14]:


prod_to_category = dict()


# In[15]:


for c, d in enumerate(data1):
    title = d['title']
    primary_isbn = d['primary_isbn']
    asin = d['asin']
    isbns = d['isbns']
    #apple_ean = d['apple_ean']
    #google_id = d['google_id']
    publisher = d['publisher']
    #partner_title = d['partner_title']
    bisac_status = d['bisac_status']
    pub_date = d['pub_date']
    price = d['price']
    series_name = d['series_name']
    volume = d['volume']
    #legacy_slugs = d['legacy_slugs']
    book_img = d['book_img']
    description = d['description']
    retailers = d['retailers']
    #retilers= d['name'](retailer_site_links)
    #url = d['url'](retailer_site_links)

    prod_to_category[title] = title, primary_isbn,asin, isbns, publisher, bisac_status, pub_date, price, series_name, volume, book_img, description, retailers


# In[16]:


prod_to_category = pd.DataFrame.from_dict(prod_to_category, orient='index')
#prod_to_category.columns = ['title','primary_isbn13','asin','apple_ean','google_id','publisher','partner_title','bisac_status','pub_date','us_list_price','series_name','volume','legacy_slugs','image', 'description', 'retailer','product_uri']


# In[17]:


prod_to_category.rename(columns={0: 'title'}, inplace=True)
prod_to_category.rename(columns={1: 'primary_isbn13'}, inplace=True)
prod_to_category.rename(columns={2: 'asin'}, inplace=True)
prod_to_category.rename(columns={3: 'apple_ean'}, inplace=True)
prod_to_category.rename(columns={4: 'publisher'}, inplace=True)
prod_to_category.rename(columns={5: 'bisac_status'}, inplace=True)
prod_to_category.rename(columns={6: 'pub_date'}, inplace=True)
prod_to_category.rename(columns={7: 'us_list_price'}, inplace=True)
prod_to_category.rename(columns={8: 'series_name'}, inplace=True)
prod_to_category.rename(columns={9: 'volume'}, inplace=True)
prod_to_category.rename(columns={9: 'volume'}, inplace=True)
prod_to_category.rename(columns={10: 'image'}, inplace=True)
prod_to_category.rename(columns={11: 'description'}, inplace=True)
prod_to_category.rename(columns={12: 'retailer'}, inplace=True)


# In[18]:


prod_to_category.tail(250)


# In[11]:


prod_to_category.to_csv("books.csv", index = False)

