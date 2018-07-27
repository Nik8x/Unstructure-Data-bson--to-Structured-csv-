

```python
import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import io
import pymongo
import bson     # this is installed with the pymongo package
import matplotlib.pyplot as plt
```


```python
path = os.getcwd() + '/books.bson'
with open(path,'rb') as f:
 data1 = bson.decode_all(f.read())
```


```python
prod_to_category = dict()
```


```python
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

```


```python
prod_to_category = pd.DataFrame.from_dict(prod_to_category, orient='index')
#prod_to_category.columns = ['title','primary_isbn13','asin','apple_ean','google_id','publisher','partner_title','bisac_status','pub_date','us_list_price','series_name','volume','legacy_slugs','image', 'description', 'retailer','product_uri']
```


```python
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
```


```python
prod_to_category.tail(250)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>primary_isbn13</th>
      <th>asin</th>
      <th>apple_ean</th>
      <th>publisher</th>
      <th>bisac_status</th>
      <th>pub_date</th>
      <th>us_list_price</th>
      <th>series_name</th>
      <th>volume</th>
      <th>image</th>
      <th>description</th>
      <th>retailer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>How I Became a Writer and Oggie Learned to Drive</th>
      <td>How I Became a Writer and Oggie Learned to Drive</td>
      <td>9781480441545</td>
      <td>B00EOIB1MK</td>
      <td>[9781480441545, 9781480441569]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-09-10 00:00:00</td>
      <td>6.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;Winner of Italy&amp;rsquo;s 2006 Premio An...</td>
      <td></td>
    </tr>
    <tr>
      <th>Typical</th>
      <td>Typical</td>
      <td>9781480441583</td>
      <td>B00EOIB0UI</td>
      <td>[9781480441583, 9781480441675]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-09-10 00:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;Twenty-three surreal fictions&amp;mdash;st...</td>
      <td></td>
    </tr>
    <tr>
      <th>Aliens of Affection</th>
      <td>Aliens of Affection</td>
      <td>9781480441606</td>
      <td>B00EOIB008</td>
      <td>[9781480441606]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-09-10 04:00:00</td>
      <td>9.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;The idiosyncratic genius of Padgett Po...</td>
      <td></td>
    </tr>
    <tr>
      <th>A Man</th>
      <td>A Man</td>
      <td>9781480442016</td>
      <td></td>
      <td>[9781480442016, 9781480442023]</td>
      <td>RCS Libri</td>
      <td>withdrawn from sale</td>
      <td>2013-09-24 00:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;Translated and sold in nineteen countr...</td>
      <td></td>
    </tr>
    <tr>
      <th>Auschwitz Belongs to Us All</th>
      <td>Auschwitz Belongs to Us All</td>
      <td>9781480442047</td>
      <td></td>
      <td>[9781480442047, 9781480442054]</td>
      <td>RCS Libri</td>
      <td>withdrawn from sale</td>
      <td>2013-11-05 00:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;Trieste, 1944. &lt;BR&gt;&lt;BR&gt;Marta is seventeen...</td>
      <td></td>
    </tr>
    <tr>
      <th>Voices</th>
      <td>Voices</td>
      <td>9781480442078</td>
      <td></td>
      <td>[9781480442078, 9781480442085]</td>
      <td>RCS Libri</td>
      <td>withdrawn from sale</td>
      <td>2013-09-24 00:00:00</td>
      <td>9.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;An open door, a pair of blue tennis shoes...</td>
      <td></td>
    </tr>
    <tr>
      <th>Of Fever and Blood</th>
      <td>Of Fever and Blood</td>
      <td>9781480442221</td>
      <td></td>
      <td>[9781480442221]</td>
      <td>Place des editeurs</td>
      <td>withdrawn from sale</td>
      <td>2013-10-15 00:00:00</td>
      <td>9.99</td>
      <td>The Inspector Svärta Thrillers</td>
      <td>1</td>
      <td></td>
      <td>&lt;div&gt;This fast-paced supernatural thriller is ...</td>
      <td></td>
    </tr>
    <tr>
      <th>Unforgettable</th>
      <td>Unforgettable</td>
      <td>9781480442627</td>
      <td>B00FP9IQ52</td>
      <td>[9781480442627]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-10-29 00:00:00</td>
      <td>6.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A Boston teenager finds a dangerous ne...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Soul of the World</th>
      <td>The Soul of the World</td>
      <td>9781480442689</td>
      <td></td>
      <td>[9781480442689, 9781480471122]</td>
      <td>Éditions Robert Laffont</td>
      <td>withdrawn from sale</td>
      <td>2014-04-15 00:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;What mysterious force impelled seven sage...</td>
      <td></td>
    </tr>
    <tr>
      <th>Scent of Sicily</th>
      <td>Scent of Sicily</td>
      <td>9781480442696</td>
      <td></td>
      <td>[9781480442696, 9781480452541]</td>
      <td>RCS Libri</td>
      <td>withdrawn from sale</td>
      <td>2013-11-05 00:00:00</td>
      <td>9.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;An impossible love, a noble, expansive Si...</td>
      <td></td>
    </tr>
    <tr>
      <th>In the Country of the Young</th>
      <td>In the Country of the Young</td>
      <td>9781480444140</td>
      <td>B00EZEX6EO</td>
      <td>[9781480444140]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-09-24 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;&amp;ldquo;An important and rewarding coll...</td>
      <td></td>
    </tr>
    <tr>
      <th>Twice Told Tales</th>
      <td>Twice Told Tales</td>
      <td>9781480444225</td>
      <td>B00EZEX95A</td>
      <td>[9781480444225]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-09-24 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;Daniel Stern&amp;rsquo;s sparkling reinven...</td>
      <td></td>
    </tr>
    <tr>
      <th>Twice Upon a Time</th>
      <td>Twice Upon a Time</td>
      <td>9781480444249</td>
      <td>B00EZEX7XY</td>
      <td>[9781480444249]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-09-24 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;More sly and imaginative tributes to s...</td>
      <td></td>
    </tr>
    <tr>
      <th>One Day's Perfect Weather</th>
      <td>One Day's Perfect Weather</td>
      <td>9781480444256</td>
      <td>B00EZEX7LQ</td>
      <td>[9781480444256]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-09-24 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;More of Daniel Stern&amp;rsquo;s celebrate...</td>
      <td></td>
    </tr>
    <tr>
      <th>Women and Children First</th>
      <td>Women and Children First</td>
      <td>9781480445079</td>
      <td>B00EZEXA9K</td>
      <td>[9781480445079]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-09-24 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;Revelations of the mysterious, contrad...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Peaceable Kingdom</th>
      <td>The Peaceable Kingdom</td>
      <td>9781480445109</td>
      <td>B00EZEXAKE</td>
      <td>[9781480445109]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2013-09-24 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;b&gt;Stories of innocence lost, from a mast...</td>
      <td></td>
    </tr>
    <tr>
      <th>A Darkness Descending</th>
      <td>A Darkness Descending</td>
      <td>9781480447301</td>
      <td>B00EJ3FBV2</td>
      <td>[9781480447301]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2013-09-03 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;When the driven, charismatic leader of a ...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Windsor Faction</th>
      <td>The Windsor Faction</td>
      <td>9781480447349</td>
      <td>B00E88GLT4</td>
      <td>[9781480447349]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2013-09-03 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;If Wallis Simpson had not died on the ope...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Preservationist</th>
      <td>The Preservationist</td>
      <td>9781480447394</td>
      <td>B00EP6PBFE</td>
      <td>[9781480447394]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2013-10-01 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A love triangle takes a sinister turn ...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Sleep Room</th>
      <td>The Sleep Room</td>
      <td>9781480447462</td>
      <td>B00F12QUKG</td>
      <td>[9781480447462]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2013-10-01 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A novel about medicine, mental illness...</td>
      <td></td>
    </tr>
    <tr>
      <th>Byron Easy</th>
      <td>Byron Easy</td>
      <td>9781480447585</td>
      <td>B00HE2JKEE</td>
      <td>[9781480447585]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2014-01-07 05:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;It&amp;rsquo;s December 24th, 1999. Byron Eas...</td>
      <td></td>
    </tr>
    <tr>
      <th>Piero's Light</th>
      <td>Piero's Light</td>
      <td>9781480447660</td>
      <td>B00HE2JKGW</td>
      <td>[9781480447660]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2014-01-07 05:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;An innovative painter in the early genera...</td>
      <td></td>
    </tr>
    <tr>
      <th>Seven Elements That Changed the World</th>
      <td>Seven Elements That Changed the World</td>
      <td>9781480447783</td>
      <td>B00HVPI18A</td>
      <td>[9781480447783]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2014-02-04 00:00:00</td>
      <td>15.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;From iron to uranium, titanium to sili...</td>
      <td></td>
    </tr>
    <tr>
      <th>Earthquake Storms</th>
      <td>Earthquake Storms</td>
      <td>9781480447868</td>
      <td>B00HVPI16M</td>
      <td>[9781480447868]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2014-02-04 05:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A geologist explores the fault line th...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Seeker</th>
      <td>The Seeker</td>
      <td>9781480447905</td>
      <td>B00IDTAEA6</td>
      <td>[9781480447905]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2014-03-04 05:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;When graduate student Aine Cahill uncover...</td>
      <td></td>
    </tr>
    <tr>
      <th>Death in Sardinia</th>
      <td>Death in Sardinia</td>
      <td>9781480447943</td>
      <td>B00IDTADZC</td>
      <td>[9781480447943]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2014-03-04 05:00:00</td>
      <td>17.99</td>
      <td>The Inspector Bordelli Mysteries</td>
      <td>3</td>
      <td></td>
      <td>&lt;div&gt;Florence, 1965. A man is found murdered, ...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Winter Warrior</th>
      <td>The Winter Warrior</td>
      <td>9781480448100</td>
      <td>B00FS0MVU4</td>
      <td>[9781480448100]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2013-11-05 05:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;1067. Following the devastating loss of t...</td>
      <td></td>
    </tr>
    <tr>
      <th>The First of July</th>
      <td>The First of July</td>
      <td>9781480448186</td>
      <td>B00FJNMB6Y</td>
      <td>[9781480448186]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2013-11-05 05:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;During World War I, four Allied soldie...</td>
      <td></td>
    </tr>
    <tr>
      <th>Running with the Pack</th>
      <td>Running with the Pack</td>
      <td>9781480448193</td>
      <td>B00EQMX3KC</td>
      <td>[9781480448193]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2013-11-05 05:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&amp;ldquo;Most of the serious thinking I hav...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Collector of Lost Things</th>
      <td>The Collector of Lost Things</td>
      <td>9781480448261</td>
      <td>B00GI6H2CO</td>
      <td>[9781480448261]</td>
      <td>Pegasus Books</td>
      <td>active</td>
      <td>2013-12-03 05:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;The year is 1845 and young researcher Eli...</td>
      <td></td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>The Social Lives of Dogs</th>
      <td>The Social Lives of Dogs</td>
      <td>9781504015561</td>
      <td>B00YBF2D4Q</td>
      <td>[9781504015561]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>11.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;From the bestselling author of &lt;I&gt;The ...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Tribe of Tiger</th>
      <td>The Tribe of Tiger</td>
      <td>9781504015578</td>
      <td>B00YBF2D6Y</td>
      <td>[9781504015578]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;From the majestic Bengal tiger to the ...</td>
      <td></td>
    </tr>
    <tr>
      <th>Woman in Red</th>
      <td>Woman in Red</td>
      <td>9781504015615</td>
      <td>B00YBF2H0Q</td>
      <td>[9781504015615]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A novel of a shattering loss, an act o...</td>
      <td></td>
    </tr>
    <tr>
      <th>Woman in Black</th>
      <td>Woman in Black</td>
      <td>9781504015622</td>
      <td>B00YBF2GXE</td>
      <td>[9781504015622]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A housekeeper&amp;rsquo;s daughter and a d...</td>
      <td></td>
    </tr>
    <tr>
      <th>Woman in Blue</th>
      <td>Woman in Blue</td>
      <td>9781504015639</td>
      <td>B00YBF2GPC</td>
      <td>[9781504015639]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;Sisters separated as children are reun...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Diary</th>
      <td>The Diary</td>
      <td>9781504015646</td>
      <td>B00YBF2GNE</td>
      <td>[9781504015646]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>9.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;Two sisters discover startling secrets...</td>
      <td></td>
    </tr>
    <tr>
      <th>Jack and Rochelle</th>
      <td>Jack and Rochelle</td>
      <td>9781504015684</td>
      <td>B00YBF2GQ6</td>
      <td>[9781504015684]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;The memoir of a man and woman who esca...</td>
      <td></td>
    </tr>
    <tr>
      <th>Sissinghurst: An Unfinished History</th>
      <td>Sissinghurst: An Unfinished History</td>
      <td>9781504015691</td>
      <td>B00YBF2D7I</td>
      <td>[9781504015691]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;&amp;ldquo;A charming portrait of an ancie...</td>
      <td></td>
    </tr>
    <tr>
      <th>H. M. Pulham, Esquire</th>
      <td>H. M. Pulham, Esquire</td>
      <td>9781504015707</td>
      <td>B00YBF2GM0</td>
      <td>[9781504015707]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>11.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A Harvard reunion prompts a Boston Bra...</td>
      <td></td>
    </tr>
    <tr>
      <th>So Little Time</th>
      <td>So Little Time</td>
      <td>9781504015714</td>
      <td>B00YBF2GJ8</td>
      <td>[9781504015714]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>11.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A father frets over his son&amp;rsquo;s fu...</td>
      <td></td>
    </tr>
    <tr>
      <th>Point of No Return</th>
      <td>Point of No Return</td>
      <td>9781504015721</td>
      <td>B00YBF2GAC</td>
      <td>[9781504015721]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>11.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A #1 &lt;I&gt;New York Times&lt;/I&gt; bestseller ...</td>
      <td></td>
    </tr>
    <tr>
      <th>Warning Hill</th>
      <td>Warning Hill</td>
      <td>9781504015738</td>
      <td>B00YBF2G48</td>
      <td>[9781504015738]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A poor boy falls in love with a privil...</td>
      <td></td>
    </tr>
    <tr>
      <th>Women and Thomas Harrow</th>
      <td>Women and Thomas Harrow</td>
      <td>9781504015745</td>
      <td>B00YBF2G4I</td>
      <td>[9781504015745]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;&amp;ldquo;&lt;I&gt;Women and Thomas Harrow &lt;/I&gt;...</td>
      <td></td>
    </tr>
    <tr>
      <th>Melville Goodwin, USA</th>
      <td>Melville Goodwin, USA</td>
      <td>9781504015752</td>
      <td>B00YBF2FZS</td>
      <td>[9781504015752]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>11.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;Finalist for the National Book Award: ...</td>
      <td></td>
    </tr>
    <tr>
      <th>Sincerely, Willis Wayde</th>
      <td>Sincerely, Willis Wayde</td>
      <td>9781504015769</td>
      <td>B00YBF2G7U</td>
      <td>[9781504015769]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>11.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;The unforgettable journey of an Americ...</td>
      <td></td>
    </tr>
    <tr>
      <th>B.F.'s Daughter</th>
      <td>B.F.'s Daughter</td>
      <td>9781504015776</td>
      <td>B00YBF2FYE</td>
      <td>[9781504015776]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-14 04:00:00</td>
      <td>17.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;The daughter of a powerful industriali...</td>
      <td></td>
    </tr>
    <tr>
      <th>Snoopy the Sportsman</th>
      <td>Snoopy the Sportsman</td>
      <td>9781504000666</td>
      <td>B00YO78SC2</td>
      <td>[9781504000666]</td>
      <td>Peanuts Worldwide</td>
      <td>active</td>
      <td>2015-07-21 04:00:00</td>
      <td>6.99</td>
      <td>Snoopy</td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;Who&amp;rsquo;s the best athlete of all time?...</td>
      <td></td>
    </tr>
    <tr>
      <th>Snoopy the Winter Wonder Dog</th>
      <td>Snoopy the Winter Wonder Dog</td>
      <td>9781504002066</td>
      <td>B00YO78SBS</td>
      <td>[9781504002066, 9781504002103]</td>
      <td>Peanuts Worldwide</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>6.99</td>
      <td>Snoopy</td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;Double axels, acrobatic jumps, and flying...</td>
      <td></td>
    </tr>
    <tr>
      <th>Snoopy the Great Entertainer</th>
      <td>Snoopy the Great Entertainer</td>
      <td>9781504002110</td>
      <td>B00YO78S9U</td>
      <td>[9781504002110, 9781504002165]</td>
      <td>Peanuts Worldwide</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>6.99</td>
      <td>Snoopy</td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;Snoopy keeps us laughing with &amp;ldquo;pawp...</td>
      <td></td>
    </tr>
    <tr>
      <th>Snoopy the Tennis Ace</th>
      <td>Snoopy the Tennis Ace</td>
      <td>9781504005401</td>
      <td>B00YO78RQE</td>
      <td>[9781504005401, 9781504005456]</td>
      <td>Peanuts Worldwide</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>6.99</td>
      <td>Snoopy</td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;Who knew that a beagle could play tennis ...</td>
      <td></td>
    </tr>
    <tr>
      <th>City</th>
      <td>City</td>
      <td>9781504012942</td>
      <td>B00YO78T1M</td>
      <td>[9781504012942]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-21 04:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;This award-winning science fiction cla...</td>
      <td></td>
    </tr>
    <tr>
      <th>Way Station</th>
      <td>Way Station</td>
      <td>9781504013185</td>
      <td>B00YO78RRS</td>
      <td>[9781504013185]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>14.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;An ageless hermit runs a secret way st...</td>
      <td></td>
    </tr>
    <tr>
      <th>The Werewolf Principle</th>
      <td>The Werewolf Principle</td>
      <td>9781504013222</td>
      <td>B00YTFT9ZE</td>
      <td>[9781504013222]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>6.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;His body hosting a pair of strange ali...</td>
      <td></td>
    </tr>
    <tr>
      <th>A Heritage of Stars</th>
      <td>A Heritage of Stars</td>
      <td>9781504013239</td>
      <td>B00YTFTA0S</td>
      <td>[9781504013239]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A man hunts for lost knowledge in a fu...</td>
      <td></td>
    </tr>
    <tr>
      <th>All Flesh Is Grass</th>
      <td>All Flesh Is Grass</td>
      <td>9781504013246</td>
      <td>B00YTFT9CM</td>
      <td>[9781504013246]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-21 04:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;Long before &lt;I&gt;Under the Dome&lt;/I&gt;, thi...</td>
      <td></td>
    </tr>
    <tr>
      <th>Time Is the Simplest Thing</th>
      <td>Time Is the Simplest Thing</td>
      <td>9781504013253</td>
      <td>B00YTFT9BI</td>
      <td>[9781504013253]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-21 04:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A telepath acquires a powerful alien c...</td>
      <td></td>
    </tr>
    <tr>
      <th>Out of Their Minds</th>
      <td>Out of Their Minds</td>
      <td>9781504013260</td>
      <td>B00YTFT9KY</td>
      <td>[9781504013260]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>6.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A writer finds himself trapped in an i...</td>
      <td></td>
    </tr>
    <tr>
      <th>Shakespeare's Planet</th>
      <td>Shakespeare's Planet</td>
      <td>9781504013284</td>
      <td>B00YTFT9AY</td>
      <td>[9781504013284]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>6.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A human space traveler trapped on a re...</td>
      <td></td>
    </tr>
    <tr>
      <th>Enchanted Pilgrimage</th>
      <td>Enchanted Pilgrimage</td>
      <td>9781504013277</td>
      <td>B00YTFT9F4</td>
      <td>[9781504013277]</td>
      <td>Open Road Media</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>7.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;&lt;B&gt;A scholar, a goblin, and a gnome, amon...</td>
      <td></td>
    </tr>
    <tr>
      <th>Princess for a Week</th>
      <td>Princess for a Week</td>
      <td>9781504013291</td>
      <td>B00YO78RS2</td>
      <td>[9781504013291]</td>
      <td>Holiday House</td>
      <td>active</td>
      <td>2015-07-21 00:00:00</td>
      <td>5.99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>&lt;div&gt;Roddy Hall overhears his mother saying &amp;l...</td>
      <td></td>
    </tr>
  </tbody>
</table>
<p>250 rows × 13 columns</p>
</div>




```python
prod_to_category.to_csv("books.csv", index = False)
```
