import time
import pandas as pd
import json
import re
import csv
import seaborn as sns
import numpy as np
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType, ChartType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.datasets.coordinates import get_coordinate, search_coordinates_by_keyword
from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts
from MyQR import myqr
import os
os.environ["PROJ_LIB"] = r'C:\Users\xuzhen\env\pyecharts\Library\share\basemap';
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
%matplotlib qt

def main():
    print(df.columns)
    print(len(df))
    df.drop([ 'updated', 'url', 'detail', 'felt',
       'alert', 'status', 'tsunami', 'net', 'code', 'ids', 'sources', 'types',
       'nst', 'dmin', 'rms', 'gap', 'magType', 'type', 'title',
       'geometry_type', 'id'], axis=1, inplace=True)
    print(df.head())
    print(df)
#     ranges = df['time']
#     print(time.ctime(df['time']))
#     print(time.gmtime(df['time']))
    ranges = [0, 5, 6, 7, 8, 99]
    group_mag = df['mag'].groupby(pd.cut(df.mag, ranges, right=False)).count()
#     year_mag = df['mag'].groupby(pd.cut(df.mag, df[], right=False)).count()
    print(group_mag)
    plt.figure(figsize=(27, 12))
    sns.distplot(df['mag'], bins=100, color='g')

#     ax.plot(bins, y, '--')
#     ax.set_xlabel('Smarts')
#     ax.set_ylabel('Probability density')
#     ax.set_title(r('Histogram of IQ: $\mu=' + mu +'$, $\sigma=' + 'signam' + '$'))

    # Tweak spacing to prevent clipping of ylabel
#     fig.tight_layout()
#     plt.show()
#     plt.pause(20)
    df6=df[df['mag'] > 6]
    yearly_count = pd.to_datetime(df6['time'],  unit='ms').dt.year.value_counts().sort_index()
#     sns.barplot(x='year', y='mag6_num', data=df[''])

    print(yearly_count.index, yearly_count.values)
#     fig, ax = plt.subplots()
    plt.figure(figsize=(27, 12))
#     plt.subplot(111)
    plt.bar(yearly_count.index.tolist(), yearly_count.values.tolist())
    plt.title('Num of Earthquakes Mag 6+ 1950-2020')
    plt.show()
    plt.savefig('num_of_earthquakes6_1950_2020.jpg')
    plt.pause(20)
    print(len(df6))
    print(df6)
    plt.figure(figsize=(27, 12))
    m = Basemap()
    ax = plt.gca()

    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5)
    m.shadedrelief()
    m.readshapefile( 'C:/Users/xuzhen/usgs/gadm36_CHN_shp/gadm36_CHN_1', 'states', drawbounds=True)


    for indexs in df6.index:
        lon2,lat2 = float(df6.loc[indexs].values[5].split(',')[0].replace('[','')), float(df6.loc[indexs].values[5].split(',')[1])
#         print(lon2,lat2)
        x,y = m(lon2,lat2)
#         m.plot(x,y,'ro',markersize = 2) 
        ax.scatter(x, y,  cmap='hsv',  s=np.pi*(df6.loc[indexs].values[0]/4.5)**2, alpha=1)
    plt.title('Earthquakes Mag 6+ 1950-2020')
    plt.savefig('map_of_earthquakes6_1950_2020.jpg')
#     print(df[df['mag'] > 8][['place', 'geometry_coordinates']].to_json())
# time.ctime(1593521814.167)
# time.gmtime(1593521814.167)
if __name__ == '__main__':
    t1 = time.time()
    csv_data = []
    path_dir = r'C:\Users\xuzhen\usgs'
    if os.path.exists(path_dir):
        path_dir = os.path.abspath(path_dir)
        for f in sorted(os.listdir(path_dir)):
            path_f = os.path.join(path_dir, f)
            if os.path.isfile(path_f):
                #if re.search('.jpg$|.png$', path_i, re.IGNORECASE):
                # note: it won't do anything if the picture filename does not contain any of the following strings: pre/dep/ret/per
                # of course you can expand the search range if necessary
                if re.search('json', path_f, re.IGNORECASE):
#                     print('json filename:' + '#'*50)
#                     print(path_f, f)                                       
                    with open(path_f, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        eq_list = data['features']    
                        for i in eq_list:
                            eq_info = []
                            eq_info.append(i['properties']['mag'])  
                            eq_info.append(i['properties']['place'])  
                            eq_info.append(i['properties']['time'])  
                            eq_info.append(i['properties']['updated'])  
                            eq_info.append(i['properties']['tz'])  
                            eq_info.append(i['properties']['url']) 
                            eq_info.append(i['properties']['detail'])
                            eq_info.append(i['properties']['felt'])  
                            eq_info.append(i['properties']['cdi'])  
                            eq_info.append(i['properties']['alert']) 
                            eq_info.append(i['properties']['status'])  
                            eq_info.append(i['properties']['tsunami'])  
                            eq_info.append(i['properties']['net'])  
                            eq_info.append(i['properties']['code'])  
                            eq_info.append(i['properties']['ids'])  
                            eq_info.append(i['properties']['sources'])  
                            eq_info.append(i['properties']['types'])  
                            eq_info.append(i['properties']['nst'])  
                            eq_info.append(i['properties']['dmin'])  
                            eq_info.append(i['properties']['rms'])  
                            eq_info.append(i['properties']['gap'])  
                            eq_info.append(i['properties']['magType']) 
                            eq_info.append(i['properties']['type']) 
                            eq_info.append(i['properties']['title']) 
                            eq_info.append(i['geometry']['type'])
                            eq_info.append(i['geometry']['coordinates'])
                            eq_info.append(i['id'])  
                            csv_data.append(eq_info)
#                             print(eq_info)
#     print('csv_data:\n', csv_data)
    a = [('mag','place','time','updated','tz','url','detail', 'felt', 'cdi', 'alert', 'status', 'tsunami', 'net', 'code',
     'ids', 'sources', 'types', 'nst', 'dmin', 'rms', 'gap', 'magType', 'type', 'title', 'geometry_type', 'geometry_coordinates', 'id')]
    csvfile = open('usgs_earthquake_4.5_worldwide_v2.csv', 'w',encoding='utf-8-sig',newline='')
    writer = csv.writer(csvfile)
    writer.writerows(a)
    writer.writerows(csv_data)
    csvfile.close()
    
    df = pd.read_csv('usgs_earthquake_4.5_worldwide_v2.csv')
    main()
    t2 = time.time()
    print('Data Analysis took {} seconds!'.format(t2 - t1))
