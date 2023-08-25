"""
This a Module that fetches the URL using requests package
"""
import requests

url = "https://alu-intranet.htbn.io.status"
response = requests.get(url)

print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
