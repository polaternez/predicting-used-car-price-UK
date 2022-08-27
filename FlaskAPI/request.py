import requests

url = "http://localhost:5000/predict_api"
data = {"input": [4.196867,	55.4, 1.4, 4, 1, 1]}
r = requests.post(url, json=data)

print(r.text)
