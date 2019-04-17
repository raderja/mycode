#!/usr/bin/python3

import csv

def main():
    with open('futurama.csv', 'r') as futurama:
        futuramalist = csv.reader(futurama, delimiter=',')
        for character in futuramalist:
            print(character[0],character[2])

main()

input("Press Enter to continue")
