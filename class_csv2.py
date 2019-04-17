#!/usr/bin/python3

import csv

def main():
    with open('futurama2.csv', 'r') as futurama:
        futuramadict = csv.DictReader(futurama, delimiter=',')
        for line in futuramadict:
            print(line["hosts"], line["ip"])

main()

input("Press Enter to continue")
