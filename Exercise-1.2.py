"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def readfunc():
    dct_file='2002FemResp.dct'
    dat_file='2002FemResp.dat.gz'
    
    dct = thinkstats2.ReadStataDct(dct_file)
    dataframe = dct.ReadFixedWidth(dat_file, compression='gzip',nrows = None)
    
    print(dataframe['pregnum'].value_counts().sort_index())
    print(len(dataframe))
def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    
    readfunc()
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
