# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:13:25 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,3,"b","a","g","a")