# coding:utf-8
# Written on Jul 12 2020 by Xuzhen Chen onboard Saltire.
# The script will crawl geojson file from usgs and save it as json/csv files

import requests
import csv
import time
import json

def data(yr):
    s = requests.session()
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?starttime=' + str(yr) + '-01-01%2023:59:59&endtime=' + str(yr) + '-12-31%2023:59:59&minmagnitude=4.5&orderby=time'
    headers = {
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    }

    s.get(url, headers=headers,timeout=30)
    cookie = s.cookies
    response = s.get(url, headers=headers,cookies=cookie,timeout=30)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    eq_json = response.json()

    with open('usgs_earthquake_data_' + str(yr) + '.json', 'w', encoding='utf-8') as file:
        json.dump(eq_json, file, ensure_ascii=False, indent=4)

# {
# "type":"Feature",
# "properties":
#     {"mag":5.9,"place":"south of Panama","time":-551589788000,"updated":1431543167000,"tz":null,
#      "url":"https://earthquake.usgs.gov/earthquakes/eventpage/iscgem893127",
#      "detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=iscgem893127&format=geojson",
#      "felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":536,"net":"iscgem",
#      "code":"893127","ids":",iscgem893127,","sources":",iscgem,","types":",origin,","nst":null,"dmin":null,
#      "rms":null,"gap":null,"magType":"mw","type":"earthquake","title":"M 5.9 - south of Panama"},
# "geometry":
#     {"type":"Point","coordinates":[-82.305,7.272,20]},
# "id":
#     "iscgem893127"
# },
        
    eq_list = eq_json['features']
    csv_data = []
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
#     print(csv_data)
    csvfile = open('usgs_earthquake_4.5_worldwide.csv', 'a+',encoding='utf-8-sig',newline='')
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
    csvfile.close()
    return csv_data
if __name__ == '__main__':
    t1 = time.time()
    a = [('mag','place','time','updated','tz','url','detail', 'felt', 'cdi', 'alert', 'status', 'tsunami', 'net', 'code',
         'ids', 'sources', 'types', 'nst', 'dmin', 'rms', 'gap', 'magType', 'type', 'title', 'geometry_type', 'geometry_coordinates', 'id')]
    csvfile = open('usgs_earthquake_4.5_worldwide.csv', 'a+',encoding='utf-8-sig',newline='')
    writer = csv.writer(csvfile)
    writer.writerows(a)
    csvfile.close()
    all_years = []
    for year in range(1950, 2021):
        result = data(year)
        all_years += result
        print('Already crawled {}pages, total num of pages:{}'.format(year, len(all_years)))
        time.sleep(5)  # slow down to get faster!
    t2 = time.time()
    print('Crawling takes {} seconds!'.format(t2 - t1))
