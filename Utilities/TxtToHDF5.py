#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
**********************************************************
*
* TxtToHDF5
* Convert txt-formatted learning data into HDF5
*
* version: 20180608a
*
* By: Nicola Ferralis <feranick@hotmail.com>
*
***********************************************************
'''

import numpy as np
import h5py, sys, os.path

#************************************
''' Read Learning file '''
#************************************
def main():

    if len(sys.argv) < 2:
        print(' Usage:\n  python3 TxtToHDF5.py <Learning File prepared with RruffDataMaker>\n')
        print(' Requires python 3.x. Not compatible with python 2.x\n')
        return
    else:
        file =  sys.argv[1]

    saveLearnFile(file)

#************************************
''' Read Learning file '''
#************************************
def saveLearnFile(learnFile):
    learnFileRoot = os.path.splitext(learnFile)[0]
    try:
        if os.path.splitext(learnFile)[1] == ".npy":
            M = np.load(learnFile)
        else:
            with open(learnFile, 'r') as f:
                M = np.loadtxt(f, unpack =False)
    except:
        print('\033[1m' + ' Learning file not found \n' + '\033[0m')
        return

    En = np.delete(np.array(M[0,:]),np.s_[0:1],0)
    M = np.delete(M,np.s_[0:1],0)
    Cl = np.asarray(['{:.2f}'.format(x) for x in M[:,0]])
    A = np.delete(M,np.s_[0:1],1)

    with h5py.File(learnFileRoot+'.h5', 'w') as hf:
        hf.create_dataset("En",  data=En)
        #hf.create_dataset("M",  data=M)
        hf.create_dataset("Cl",  data=Cl.astype('|S9'))
        hf.create_dataset("A",  data=En)

    print("Learning file converted to hdf5")

#************************************
''' Main initialization routine '''
#************************************
if __name__ == "__main__":
    sys.exit(main())
