#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:33:41 2020
@author: nekropolis
"""
from sensorimotor import *
from scipy.io import loadmat
import scipy

#from mat4py import loadmat

"""
v = Viewer()
h = GuiManager(v)
h.update_signals
"""

def sc(filename):
    #annots = loadmat(filename, squeeze_me=True, struct_as_record=False)
    #return annots
    data = loadmat(filename, squeeze_me=True)
    return data

#filename = '/home/nekropolis/neuro-code/python-gui/BENR_sc.mat'
filename = 'example.mat'
data = sc(filename)

properties = [key for key in data.keys() if not key.startswith('__')]

for p in properties:
    print(p)
    value = data[p]
    names = value.dtype.names
    for name in names:
        it = value[name]
        val = it.all()
        
        
        if type(val) is str:
            print("str:", val)
        elif type(val) is int:
            print("int", val)
        elif type(val) is np.ndarray:
            print("nd-array:", val)
            dtypes = val.dtype
            if val.dtype.names is not None:
                print(val.dtype.names)
                names2 = val.dtype.names
                for j in names2:
                    print("___***___", val[j].all())
        elif type(val) is scipy.io.matlab.mio5_params.MatlabOpaque:
            print("matlab opaque:", val)
        else:
            print("Errorrr!", type(val))
                
