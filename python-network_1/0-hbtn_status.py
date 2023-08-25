"""
This a Module that fetches the URL using requests package
"""
import requests
response = requests.get("https://alu-intranet.htbn.io.status")

print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
