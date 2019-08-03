# --coding:utf-8--
import requests

# get请求
print(requests.get('http://localhost:8080/jenkins/api/json?pretty=true').text)

# post请求
url = 'http://localhost:8080/jenkins/job/check_python_version/disable'
r = requests.post(url, data={}, auth=('xiaxiaochao', '037456'))
print(r.status_code)
print(r.headers)
print(r.reason)
