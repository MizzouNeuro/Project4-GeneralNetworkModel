# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:53:53 2018

@author: tjbanks
"""

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("sim_builder_main.py", base=base)]

packages = ["idna","time","re","subprocess","threading","os","random","numpy","pandas","tkinter","glob","collections"]
folders = ['ca1/']
options = {
    'build_exe': {    
        'packages':packages,
        'include_files':folders
    },    
}

setup(
    name = "SimBuilder",
    options = options,
    version = "1",
    description = 'Sim Builder Nair Lab (Tyler Banks)',
    executables = executables
)