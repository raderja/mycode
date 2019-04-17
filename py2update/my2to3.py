#!/usr/bin/python3
thisround = 0
while(True):
    print('What is the IPv4 address used to broadcast on a local network? ')
    answer = raw_input()
    thisround = thisround + 1
    if (answer == '255.255.255.255'):
        print('Correct!')
        break
    elif (thisaround == 3):
        print('Sorry, the answer was 255.255.255.255')
        break
    else:
        print('Sorry. Try again!')
