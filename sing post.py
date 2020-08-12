# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:09:07 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
line1=[]
line2=[]
line3=[]
for i in range (1,4):
    line1.append(1*i)
for i in range(1,4):
    line2.append(2*1)
for i in range(1,4):
    line3.append(3*i)
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,3,str(line1),str(line2),str(line3))    