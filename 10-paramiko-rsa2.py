#!/usr/bin/python3

## standard library imports
import os
import warnings
## 3rd party import
import paramiko

## excel data or csv data
excellist = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "fry", "ip": "10.10.2.4"}, {"un": "zoidberg", "ip": "10.10.2.5"}]

warnings.filterwarnings(action="ignore", module=".*paramiko.*")

## Think! We created an empty PuTTY session
sshsession = paramiko.SSHClient()

## go grab an SSH key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## Skips the warning that says "THIS FINERPRINT LOOKS NEW" (known_hosts)
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for fc in excellist:
    ## cool windows dressing
    print("\nConnecting to ...", fc['un'], "@", fc['ip'])
    ## press the CONNECT butttto in our PuTTY session
    sshsession.connect(hostname=fc['ip'], username=fc['un'], pkey=mykey)

    ## Get teh 3 responses
    ssh_in, ssh_out, ssh_err = sshsession.exec_command('ls /var/')

    ## Display results of our command
    print(ssh_out.read().decode('utf-8'))

    ## ssh is not a barn
    sshsession.close

