"""
This module sends a request to the URL 
and displays the value of the variable X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":

    def get_x_request_id(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                x_request_id = response.headers.get('X-Request-Id')
                if x_request_id:
                    print(f'X-Request-Id: {x_request_id}')
                else:
                    print('X-Request-Id not found in the response headers.')
            else:
                print(
                    f'Request failed with status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'An error occurred: {e}')

    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        get_x_request_id(url)
