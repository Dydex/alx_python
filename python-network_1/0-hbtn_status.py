"""Module that fetches URL"""
import requests
"""Module that fetches URL"""
url = "https://alu-intranet.htbn.io.status"
response = requests.get(url)
"""Module that fetches URL"""
if response.status_code == 200:
    """Module that fetches URL"""
    data = response.json()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
else:
    print("Failed to fetch data. Status code: {}".format(response.status_code))
