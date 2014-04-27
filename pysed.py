#!/usr/bin/env python3
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'
__version__ = 0.2

import re

def repace(oldstr, newstr, infile, dryrun=False):
    '''
    Sed-like Replace function..
    Usage: pysed.replace(<Old string>, <Replacement String>, <Text File>)
    Example: pysed.replace('xyz', 'XYZ', '/path/to/file.txt')
    Example 'DRYRUN': pysed.replace('xyz', 'XYZ', '/path/to/file.txt', dryrun=True) #This will dump the output to STDOUT instead of changing the input file.
    '''
    linelist = []
    f = open(infile)
    while True:
        item = f.readline().splitlines()
        if len(item) == 0:
            break
        newitem = re.sub(oldstr, newstr, item[0])
        linelist.append(newitem)
    f.close()
    if dryrun == False:
        f = open(infile, "w")
        f.truncate()
        for line in linelist: f.writelines(line + "\n")
        f.close()
    elif dryrun == True:
        for line in linelist: print(line)
    else:
        exit("Unknown option specified to 'dryrun' argument, Usage: dryrun=<True|False>.")

def rmline(oldstr, infile, dryrun=False):
    '''
    Sed-like line deletion function..
    Usage: pysed.rmline(<Unwanted string>, <Text File>)
    Example: pysed.rmline('xyz', '/path/to/file.txt')
    Example 'DRYRUN': pysed.rmline('xyz', '/path/to/file.txt', dryrun=True) #This will dump the output to STDOUT instead of changing the input file.
    '''
    linelist = []
    f = open(infile)
    while True:
        item = f.readline().splitlines()
        if len(item) == 0:
            break
        newitem = item[0]
        rmitem = re.match(r'.*{}'.format(oldstr), item[0])
        if type(rmitem) == type(None): linelist.append(item[0])
    f.close()
    if dryrun == False:
        f = open(infile, "w")
        f.truncate()
        for line in linelist: f.writelines(line + "\n")
        f.close()
    elif dryrun == True:
        for line in linelist: print(line)
    else:
        exit("Unknown option specified to 'dryrun' argument, Usage: dryrun=<True|False>.")


