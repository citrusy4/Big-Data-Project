import nltk
import sys
import json
import operator

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
data = open('natural_disaster_US.json','r',encoding = 'utf-8-sig',errors = 'ignore')
data2 = json.load(data,strict=False)
words = []
count = 0

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


wordcount = {}
for line in data2:
    for word in line['text'].split():
        if word not in wordcount:
            wordcount[word.translate(non_bmp_map)]=1
        else:
            wordcount[word.translate(non_bmp_map)]+=1
sorted_wordcount = sorted(wordcount.items(),key=operator.itemgetter(1),reverse = True)
for k,v in sorted_wordcount:
    print (k,v)
    words.append(k)
    count+=1
    if (count == 5):
        break

with open('natural_disaster_US_Filter.json','a',encoding = 'utf-8') as f:
    f.write('[')
    f.flush()
    f.close()
for line in data2:
    sentence = line['text']
    tokens = nltk.word_tokenize(sentence)
    wrote = False
    for word in words:
        if word in tokens:
            if(wrote == False):
                with open('natural_disaster_US_Filter.json','a',encoding = 'utf-8') as f2:
                    print('1')
                    result = result = '{"text":"'+line['text']+'","created_at":"'+line['created_at']+'",'+'"coordinates":"'+line['coordinates']+'"},'
                    f2.write(result)
                    f2.write('\n')
                    f2.flush()
                    f2.close()
                    wrote = True
with open('natural_disaster_US_Filter.json','a',encoding = 'utf-8') as f:
    f.write(']')
    f.flush()
    f.close()
    
