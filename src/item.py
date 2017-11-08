# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from math import *

import globe



global itstatus
itstatus={"normal":0,"fly":1}

global rsource
global player


class ItemManager(object):
	#item=set()
	#speed
	#fspeed
	#zjpoint
	def __init__(self):
		global rsource
		global player
		rsource=globe.mgame.rsmanager.image["resource"]
		player=globe.scgame.player

		self.item=set()
		self.speed=1
		self.fspeed=10

	def create(self,itype,point):
		tp=itype(point)
		if tp.rect.right>=globe.playrc.right:
			tp.rect.right=globe.playrc.right
		if tp.rect.left<=globe.playrc.left:
			tp.rect.left=globe.playrc.left
		self.item.add(tp)

	def update(self):
		tmp=[]
		for i in self.item:
			if i.status==itstatus["normal"]:
				if i.frame<=60:
					speed=self.speed*(-1)
				else:
					speed=self.speed
				i.rect.top+=speed
				if i.rect.colliderect(globe.scgame.player.rect):
					i.buffer()
					tmp.append(i)
				if i.rect.top>globe.playrc.bottom:
					tmp.append(i)
				if i.rect.left<globe.playrc.left or i.rect.right>globe.playrc.right:
					tmp.append(i)
				i.frame+=1
			else:
				dx=player.point[0]-i.rect.centerx
				dy=player.point[1]-i.rect.centery
				dis=sqrt(dx**2+dy**2)
				if dis==0:
					dis=0.0001
				i.vx=int(self.fspeed*dx/dis)
				i.vy=int(self.fspeed*dy/dis)
				i.rect.left+=i.vx
				i.rect.top+=i.vy
				if i.rect.collidepoint(player.point):
					i.buffer()
					tmp.append(i)
		for i in tmp:
			self.item.remove(i)

	def getitem(self):
		for i in self.item:
			i.status=itstatus["fly"]

	def draw(self,screen):
		for i in self.item:
			screen.blit(i.image,i.rect)



class SPowerItem(object):
	def __init__(self,point):
		self.vx=0
		self.vy=0
		self.image=rsource[0][0]
		self.rect=self.image.get_rect()
		self.rect.center=point
		self.status=itstatus["normal"]
		self.frame=0
	def buffer(self):
		if globe.scgame.player.power<495:
			player.power+=5
		else:
			player.power=500

class LPowerItem(object):
	def __init__(self,point):
		self.vx=0
		self.vy=0
		self.image=rsource[2][1]
		rc=self.image.get_rect()
		rc.width=int(rc.width*0.7)
		rc.height=int(rc.height*0.7)
		self.image=pygame.transform.scale(self.image,rc.size)
		self.rect=self.image.get_rect()
		self.rect.center=point
		self.status=itstatus["normal"]
		self.frame=0
	def buffer(self):
		if globe.scgame.player.power<400:
			player.power+=100
		else:
			player.power=500



class PointItem(object):
	def __init__(self,point):
		self.vx=0
		self.vy=0
		self.image=rsource[0][1]
		self.rect=self.image.get_rect()
		self.rect.center=point
		self.status=itstatus["normal"]
		self.frame=0

	def buffer(self):
		globe.scgame.score+=50

class LifeItem(object):
	def __init__(self,point):
		self.vx=0
		self.vy=0
		self.image=rsource[3][0]
		self.rect=self.image.get_rect()
		self.rect.center=point
		self.status=itstatus["normal"]
		self.frame=0

	def buffer(self):
		player.life+=1
		globe.mgame.msmanager.play_SE("extend")

#globe.scgame.player

class CleanBlItem(object):
	def __init__(self,point):
		self.vx=0
		self.vy=0
		self.image=rsource[3][1]
		self.rect=self.image.get_rect()
		self.rect.center=point
		self.status=itstatus["normal"]
		self.frame=0
	def buffer(self):
		globe.scgame.score+=50