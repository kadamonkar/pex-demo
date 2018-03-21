#!/usr/bin/python

import requests
import sys
import json

url = sys.argv[1]

def main(): 
    r = requests.get(url)
    print r.status_code

if __name__ == '__main__':
    main()
