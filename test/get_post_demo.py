import http.client
import urllib.request
from urllib import parse

# client实现 get请求
from urllib.error import HTTPError

http_client_get = None

http_client_get = http.client.HTTPConnection('localhost', 8080, timeout=30)
http_client_get.request('GET', '/jenkins/api/json?pretty=true')

response_get = http_client_get.getresponse()
print(response_get.status)
print(response_get.read())

# urllib.request实现 get请求
response_urllib = urllib.request.urlopen('http://localhost:8080/jenkins/api/json?pretty=true/')
print(response_urllib.read())

# urllib实现 post请求

post_data = urllib.parse.urlencode({})
response_post = urllib.request.urlopen('http://localhost:8080/jenkins/job/check_python_version1/polling',
                                       post_data, timeout=30)
print(response_post.read())
print(response_post.getheaders())
