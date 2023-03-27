# [참고] https://github.com/wikibook/blockchain-by-python
# [참고] https://www.blockchain.com/explorer/api/blockchain_api
# 파이썬 실습 파일: BitcoinTime.py
# 파일 실행 : D:\python>python ./BitcoinTime.py

import requests
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 금일 생성된 블록을 읽어온다.
print("금일 생성된 블록일 읽어옵니다")
t = time.time()
time_in_milliseconds = int(t * 1000)

# blockchain_api에서 Blocks for one day 읽어오는 방법, https://blockchain.info/blocks/$time_in_milliseconds?format=json
url = 'https://blockchain.info/blocks/' + str(time_in_milliseconds) + '?format=json' 
resp = requests.get(url=url)
block = resp.json()

print("height \t time \t\t\t hash")
header = []

for n in range(len(block)):
    height = block[n]['height']
    btime = block[n]['time']
    ts = time.gmtime(block[n]['time'])
    date = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    bhash = block[n]['hash']
    print("%s \t %s \t %s" % (height, date, bhash))

    header.append([height, btime, bhash])

df = pd.DataFrame(header, columns=['Height', 'Time', 'Hash'])
sdf = df.sort_values('Time')
sdf = sdf.reset_index()
print('총 %d 개 블록 헤더를 읽어왔습니다.' % len(df))

# 블록 생성 소요 시간 분포 관찰
mtime = sdf['Time'].diff().values
mtime = mtime[np.logical_not(np.isnan(mtime))]
print("평균 Mining 시간 = %d (초)" % np.mean(mtime))