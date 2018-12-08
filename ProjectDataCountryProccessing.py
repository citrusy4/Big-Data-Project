import json
import re
import sys
import urllib
import countries
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
data = open('naturaldisaster.json','r',encoding = 'utf-8-sig',errors = 'ignore')
data2 = json.load(data,strict=False)
cc = countries.CountryChecker('TM_WORLD_BORDERS-0.3.shp')
c = 0;
with open('natural_disaster_US.json','a',encoding = 'utf-8') as f:
    f.write('[')
    f.flush()
    f.close()
for line in data2:
    lat = float(line['coordinates'].split(',')[0][1:])
    log = float(line['coordinates'].split(',')[1][:-1])
    print(c)
    if(cc.getCountry(countries.Point(log,lat)) is None):
        pass
    else:
        if(cc.getCountry(countries.Point(log,lat)).iso == 'US'):
            with open('natural_disaster_US.json','a',encoding = 'utf-8') as file:
                result = '{"text":"'+line['text']+'","created_at":"'+line['created_at']+'",'+'"coordinates":"'+line['coordinates']+'"},'
                file.write(result);
                file.write('\n')
                file.flush()
                file.close()
                c+=1
with open('natural_disaster_US.json','a',encoding = 'utf-8') as file2:
    file2.write(']')
    file2.flush()
    file2.close()

