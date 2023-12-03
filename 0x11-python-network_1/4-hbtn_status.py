#!/usr/bin/python3
"""This python module holds a script  that fetches
https://alx-intranet.hbtn.io/status"""
from requests import get


if __name__ == "__main__":
    result = get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print(f"\t- type: {type(result)}")
    print(f"\t- content: {result}")
    
