#!/usr/bin/python
"""This a Module that fetches the URL using requests package"""
import requests
"""
This imports the requests method
"""
if __name__ == "__main__":

    response = requests.get("https://alu-intranet.htbn.io.status")
    """
    saves the requests in a variable
    """
    print("Body response:")
    """
    prints body response
    """
    print("\t- type: {}".format(type(response.text)))
    """
    prints type of response text
    """
    print("\t- content: {}".format(response.text))
    """
    prints content of response text
    """
