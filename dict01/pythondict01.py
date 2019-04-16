#!/usr/bin/env python3

## create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

## display parts of the dictionary
print( switch['hostname'])
print( switch['ip'])

## request a 'fake' key
#print( switch['lynx'])

## request a fake key with .git() method
print( "First test - .get()" )
print( switch.get('lynx'))

print( "Second test - .get()" )
print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!") )

print( "THird test - .get()" )
print( switch.get('version') )



input("Press the Enter key to exit")
