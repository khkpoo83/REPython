import requests

url='https://cookbook.exemone.com/docs/%EB%A6%B4%EB%A6%AC%EC%A6%88%EB%85%B8%ED%8A%B8/%EC%A0%95%EA%B7%9C_%ED%8C%A8%ED%82%A4%EC%A7%80/ExemONE_Release_2509_%EB%A6%B4%EB%A6%AC%EC%A6%88_%EB%85%B8%ED%8A%B8'

rs=requests.get(url=url)
print(rs.text)