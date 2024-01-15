#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the
value of the X-Request-Id variable found in the header of the
response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """Takes in a URL, sends a request to the URL, and displays
    the value of the X-Request-Id variable found in the header
    of the response using requests"""
    url = argv[1]

    try:
        # Make a GET request using the requests library
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Retrieve the value of X-Request-Id from the headers
            request_id = response.headers.get('X-Request-Id')

            if request_id:
                # Print the value of X-Request-Id
                print(request_id)
            else:
                print("X-Request-Id not found in the response headers.")
        else:
            # Display error message if the request was not successful
            print(f"Error: Unable to fetch response. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Handle any request-related exceptions
        print(f"Error: {e}")
