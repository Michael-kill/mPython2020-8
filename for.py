# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:41:18 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
for j in range(3):
    for i in range(100):
        mc.setBlock(x+1,y-1,z+i+j,57)