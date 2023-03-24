# [참고] https://github.com/wikibook/blockchain-by-python
# [참고] https://bitnodes.io/api/#list-snapshots
# 파이썬 실습 파일: BitcoinNodes.py
# 파일 실행 : D:\python>python ./BitcoinNodes.py
import requests                 # pip install requests
import time
import matplotlib.pyplot as plt # pip install matplotlib

# 100 page까지만 조회한다. 이 사이트는 최근 10일까지 데이터를 제공함.
nPage = 17

t = []
n = []
for page in range(1, nPage):
    # 페이지 당 100개 씩 요청한다. (Max = 100)
    url = 'https://bitnodes.io/api/v1/snapshots/?limit=100&page=' + str(page)
    resp = requests.get(url=url)
    data = resp.json()
    print("page %d loaded." % page)

    for i in range(len(data['results'])):
        ts = time.gmtime(data['results'][i]['timestamp'])
        t.append(time.strftime("%Y-%m-%d %H:%M:%S", ts))
        n.append(data['results'][i]['total_nodes'])

t = t[::-1]
n = n[::-1]

# 최근 노드수의 변화를 확인한다
plt.figure(figsize=(8,6))
plt.plot(n, color='red', linewidth=0.7)
plt.xlabel('timestamp')
plt.ylabel('total nodes')
plt.title('Bitcoin Nodes\n' + t[0] + ' ~ ' + t[-1])
plt.grid(color='green', alpha=0.2)
plt.show()
