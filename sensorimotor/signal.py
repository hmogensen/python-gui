#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:25:17 2020

@author: nekropolis
"""
import matplotlib.pyplot as plt
import numpy as np

## Data containers
class Signal:
    
    def __init__(self):
        pass
    
    def get_v(self, trigger_time, pretrigger, posttrigger):
        return np.array([1., 1., 2., 1.]), np.array([-.1, 0, .1, .2])

## GUI Managers
class SignalManager:
    
    def __init__(self, parent, axes, signal=None):
        self.axes   = axes
        self.signal = signal
        self.parent = parent

    def update_plot(self):
        if self.signal is None:
            return
        v, t = self.signal.get_v(self.parent.triggertime, \
                                   self.parent.pretrigger, \
                                       self.parent.posttrigger)
        
        plt.plot(self.axes, t, v)
        plt.ylabel('some numbers')
        plt.show()

class FigureManager:
    
    def __init__(self):
        self.figure = plt.Figure()
    
class GuiManager:
    
    nbr_of_signals = 3
    pretrigger = -.5
    posttrigger = .5
    triggertime = 1
    
    def __init__(self, viewer):
        self.viewer          = viewer
        self.signal_managers = list()
        self.nbr_of_signals = min(self.nbr_of_signals, \
                                  len(viewer.signals))
            
        fig, axs = plt.subplots(self.nbr_of_signals)
        for i in range(0, self.nbr_of_signals):
            signal_manager = SignalManager(self, axs[i], viewer.signals[i])
            self.signal_managers.append(signal_manager)
        
            
        
    def update_signals(self):
        for signal_manager in self.signal_managers:
            signal_manager.update_plot()

