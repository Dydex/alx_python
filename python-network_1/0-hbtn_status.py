"""This is an import requests module"""
import requests
"""This is an import requests module"""


    url = "https://alu-intranet.htbn.io.status"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
else:
    print("Failed to fetch data. Status code: {}".format(response.status_code))
