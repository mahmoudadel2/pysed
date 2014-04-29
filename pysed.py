#!/usr/bin/env python3
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'
__version__ = 0.3

import re

def replace(oldstr, newstr, infile, dryrun=False):
    '''
    Sed-like Replace function..
    Usage: pysed.replace(<Old string>, <Replacement String>, <Text File>)
    Example: pysed.replace('xyz', 'XYZ', '/path/to/file.txt')
    Example 'DRYRUN': pysed.replace('xyz', 'XYZ', '/path/to/file.txt', dryrun=True) #This will dump the output to STDOUT instead of changing the input file.
    '''
    linelist = []
    with open(infile) as f:
        for item in f:
            newitem = re.sub(oldstr, newstr, item)
            linelist.append(newitem)
    if dryrun == False:
        with open(infile, "w") as f:
            f.truncate()
            for line in linelist: f.writelines(line)
    elif dryrun == True:
        for line in linelist: print(line, end='')
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
    with open(infile) as f:
        for item in f:
            rmitem = re.match(r'.*{}'.format(oldstr), item)
            if type(rmitem) == type(None): linelist.append(item)
    if dryrun == False:
        with open(infile, "w") as f:
            f.truncate()
            for line in linelist: f.writelines(line)
    elif dryrun == True:
        for line in linelist: print(line, end='')
    else:
        exit("Unknown option specified to 'dryrun' argument, Usage: dryrun=<True|False>.")