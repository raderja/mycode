#!/usr/bin/python3
import urllib.request
import json

def main():
    majortom = urllib.request.urlopen('http://api.open-notify.org/astros.json')

    #print(majortom.code)
    #print(majortom.headers)
    #print(type(majortom.read().decode('utf-8')))

    # How to get sting changed over to dictionary using json
    helmetson = majortom.read().decode('utf-8')
    groundctrl = json.loads(helmetson)
    #print(groundctrl)
    #print(type(groundctrl))
    # pull data from json and pull out only the name
    for astro in groundctrl['people']:
        print(astro['name'])

    # code, status, headers

    #print(type(majortom))

    #print(dir(majortom))

    input("Press Enter to exit")

main()
main()
