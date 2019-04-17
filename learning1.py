#!/usr/bin/python3

import requests

def main():
majortom = requests.git('http://api.open-notify.org/astros.json')

helmetson = majortom.json()
for astro in helmetson["people"]: 
        print(astro["name"])
        
main()
