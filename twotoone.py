#!/usr/bin/python3

# 2 files; open data, parse to machine, combine and spit out to single files

# open file1 - bunker east
bedata = open("bunkereast.txt", "r")

# open file2 - bunker west
bwdata = open("bunkerwest.txt", "r")

# read file 1 - "bunker east"
belines = bedata.readlines()

# read file 2 - "bunker west"
bwlines = bwdata.readlines()

# close file1
bedata.close()

# close file2
bwdata.close()

# create a single file of all our lines
bafile = open('bunkerall.txt', 'w')
for switch in belines:
    bafile.write('e-' + switch.rstrip('\n') + '\n')
for switch in bwlines:
    bafile.write('w-' + switch.rstrip('\n') + '\n')

bafile = open('bunkerall.txt', 'r')
balines = bafile.readlines()
bafileip = open('bunkerips.txt', 'w') # crate a new file for ips olny
for line in balines:
    bafileip.write(line.split(' ')[1])  # just write out ips
bafileip.close()
bafile.close()

# combine data sets - 2 dictionary
# lists [] and dict {key:value}

bunkerdict = {}
bedata = open('bunkereast.txt', 'r')
belist = bedata.readlines()
bedata.close() # cloase our open file
for line in belist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')
eastwest = {}
#eastwest.update({['east'] = bunkerdict

bunkerdict2 = {} 
bwdata = open('bunkerwest.txt', 'r')
bwlist = bwdata.readlines()
bwdata.close()
for line in bwlist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')
#eastwest.update({'west'] = bunkerdict2
print(eastwest)


# lists [] dictionary {key:value}

# [{"sw1": "10.0.0.1", "sw2" "10.0.0.2", ...} {"sw1": "192.168.0.1", "sw2": "192.168.0.2", ...}]

# {"east": {"sw1": "10.0.0.1", "sw2" "10.0.0.2", ...} {"west": {"sw1": "192.168.0.1", "sw2": "192.168.0.2", ...}]

# write out to single file3 - "bunker all"
