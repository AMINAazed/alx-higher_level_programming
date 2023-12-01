#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
    """
    url = argv[1]

    try:
        # Make a GET request using the requests library
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Decode and print the response content
            print(response.text)
        else:
            # Display error message if the request was not successful
            print(f"Error: Unable to fetch response. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Handle any request-related exceptions
        print(f"Error: {e}")

