import json
import sys
import os
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
with open('naturaldisaster.json','r+',encoding = 'utf-8-sig',errors = 'ignore')as f:
    content = f.read()
    f.seek(0,0)
    f.write('['+content)
    f.write(']')
