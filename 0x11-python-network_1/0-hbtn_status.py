#!/usr/bin/python3
""" using urllib to fetch https://alx-intranet.hbtn.io/status """

from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    # fetch the URL
    with request.urlopen(url) as response:
        # Read and decode the response body
        response_body = response.read()

        # Display the response body with tabulation
        print("Body response:")
        print(f"\t- type: {type(response_body)}")
        print(f"\t- content: {response_body}")
        print(f"\t- utf8 content: {response_body.decode('utf-8')}")
        
