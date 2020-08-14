# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:41:35 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import random
mc=Minecraft.create()
for i in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+i
    for j in range(10):
        r=random.randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,r)
ans=random.randrange(1,16)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        block=mc.getBlockWithdata(hit.pos)
        data=block.data
        if data==ans:
            mc.postToChat('good')
            mc.setBlock(hit.pos,57)
        else:
            mc.postToChat('wrong')                           