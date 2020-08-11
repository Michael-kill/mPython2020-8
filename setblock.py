# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:06:28 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x-1,y,z,18)
mc.setBlock(x+1,y,z,18) 
mc.setBlock(x,y,z+1,18) 
mc.setBlock(x,y,z-1,18)                    