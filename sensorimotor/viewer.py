#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:32:34 2020

@author: nekropolis
"""
from .signal import Signal

class Viewer:
    
    signals = list()
    
    def __init__(self):
        for i in range(0, 3):
            self.signals.append(Signal())
