import requests
from hust_auth import HustAuth

session = requests.Session()
hust_auth = HustAuth('U2022XXXXX','XXXXXXXX')

resp = session.get('http://m.hust.edu.cn/wechat/apps_center.jsp',auth=hust_auth)
print(resp.text)
