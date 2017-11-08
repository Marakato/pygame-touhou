# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *

import globe

import cache


global ziji


class TamaManager(object):
	#tmimg
	#image
	#rect[]
	#dis
	def __init__(self):
		global ziji
		self.rect=[]
		self.tmimg=globe.mgame.rsmanager.anime["ziji"][4]
		ziji=globe.scgame.player
		for i in range(4):
			self.rect.append(self.tmimg.get_rect())

	def update(self):
		global ziji
		self.image=cache.cache_rotate(self.tmimg,globe.scgame.time*2,True)
		for i in range(4):
			self.rect[i].size=self.image.get_size()
		power=ziji.power
		if ziji.keys[pygame.K_LSHIFT]:
			dis=18
		else:
			dis=28
		if power<100:
			pass
		elif power<200:
			self.rect[0].center=ziji.point
			self.rect[0].top-=dis
		elif power<300:
			self.rect[0].center=ziji.point
			self.rect[0].left-=dis
			self.rect[1].center=ziji.point
			self.rect[1].left+=dis
		elif power<400:
			self.rect[0].center=ziji.point
			self.rect[0].left-=dis
			self.rect[1].center=ziji.point
			self.rect[1].left+=dis
			self.rect[2].center=ziji.point
			self.rect[2].top-=dis
		else:
			self.rect[0].center=ziji.point
			self.rect[0].left-=dis
			self.rect[1].center=ziji.point
			self.rect[1].left+=dis
			self.rect[2].center=self.rect[0].center
			self.rect[2].left-=(dis-10)
			self.rect[3].center=self.rect[1].center
			self.rect[3].left+=(dis-10)


	def draw(self,screen):
		tp=int(ziji.power/100)
		if tp>4:
			tp=4
		for i in range(tp):
			screen.blit(self.image,self.rect[i])