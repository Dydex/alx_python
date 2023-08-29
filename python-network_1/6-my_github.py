"""
This module takes your GitHub credentials 
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys


def get_github_user_id(username, token):
    try:
        url = f'https://api.github.com/Dydex'
        headers = {
            'Authorization': f'Basic {username}:{token}',
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get('id')
            print(f'GitHub User ID: {user_id}')
        else:
            print(
                f'Error: Unable to fetch user data. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <GitHubUsername> <PersonalAccessToken>")
    else:
        username = sys.argv[1]
        token = sys.argv[2]
        get_github_user_id(username, token)
