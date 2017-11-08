# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *

import globe

import cache
import item

import scene_gameover

from math import *

global resource


global cstatus
global canime



class Player(object):
	#anime
	#aindex

	#frame

	#life
	#power

	#count

	#status

	#point
	#rect


	def __init__(self):
		global resource
		resource=globe.mgame.rsmanager
		self.playrc=globe.playrc
		self.point=[224.0,450.0]
		self.rect=Rect(0,0,10,10)

		global cstatus
		global canime
		cstatus={}
		cstatus["normal"]=0
		cstatus["wudi"]=1
		cstatus["crash"]=2
		cstatus["sc"]=3
		cstatus["scwudi"]=4
		cstatus["hit"]=5

		self.status=cstatus["normal"]

		globe.cstatus=cstatus


		canime={}
		canime["stay"]=resource.anime["ziji"][0]
		canime["toleft"]=resource.anime["ziji"][1]
		canime["toright"]=resource.anime["ziji"][2]
		canime["panding"]=resource.anime["ziji"][3]

		self.anime=canime["stay"]
		self.aindex=0

		self.power=200
		self.life=8

		self.frame=0
		self.tcount=0



	def fire(self):
		if globe.scgame.timestop==False:
			tm=globe.scgame.tmmanager
			bl=globe.scgame.blmanager
			bl.create_plbl(self.rect.inflate(-12,-8).topleft,0)
			bl.create_plbl(self.rect.inflate(-12,-8).topright,0)
			tp=self.power/100
			if tp>=5:
				tp=4
			for i in range(tp):
				bl.create_plbl(tm.rect[i].center,1)
				bl.create_plbl(tm.rect[i].center,2)




	def throwbomb(self):
		if self.power>=100 and self.status!=cstatus["sc"] and self.status!=cstatus["scwudi"] and globe.scgame.timestop==False:
#			
			self.power-=100
			self.status=cstatus["sc"]
			globe.mgame.msmanager.play_SE("wudi")

	def miss(self):
		if self.status==cstatus["hit"]:
			globe.scgame.anmanager.create_anime(resource.anime["bubble"],self.rect.topleft,5)
			globe.scgame.blmanager.clear_enbl()
			rc=self.rect.copy()
			rc.left-=20
			globe.scgame.itmanager.create(item.LPowerItem,rc.topleft)
			rc.left+=20
			globe.scgame.itmanager.create(item.LPowerItem,rc.midtop)
			rc.left+=20
			globe.scgame.itmanager.create(item.LPowerItem,rc.topright)

			self.status=cstatus["crash"]
			self.tmppd=[0,0]
			self.tmppd[0]=self.point[0]
			self.tmppd[1]=self.point[1]
			self.rect.midtop=self.playrc.midbottom
			self.point[0]=self.rect.centerx
			self.point[1]=self.rect.centery
			self.tcount=0
			self.life-=1
			self.power-=200
			if self.power<=0:
				self.power=0


	def move(self):
		
		keys=self.keys

		if keys[pygame.K_z]:
			self.fire()

		if keys[pygame.K_x]:
			self.throwbomb()

		if keys[pygame.K_LSHIFT]:
			self.speed=1.5
		else:
			self.speed=8

		if (keys[pygame.K_DOWN] or keys[pygame.K_UP]) and (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
			self.speed/=sqrt(2)



		if keys[pygame.K_DOWN]:
			self.point[1]+=self.speed
		if keys[pygame.K_UP]:
			self.point[1]-=self.speed


		if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
			if self.anime!=canime["stay"]:
				self.anime=canime["stay"]
				self.aindex=0



		elif keys[pygame.K_RIGHT]:
			if self.anime!=canime["toright"]:
				self.anime=canime["toright"]
				self.aindex=0
			self.point[0]+=self.speed

		elif keys[pygame.K_LEFT]:
			if self.anime!=canime["toleft"]:
				self.anime=canime["toleft"]
				self.aindex=0
			self.point[0]-=self.speed
				
		if keys[pygame.K_LEFT]==False and keys[pygame.K_RIGHT]==False:
			if self.anime!=canime["stay"]:
				self.anime=canime["stay"]
				self.aindex=0

		self.rect.size=self.anime[self.aindex].get_size()
		self.rect.center=(int(self.point[0]),int(self.point[1]))

		if self.rect.top<self.playrc.top:
			self.rect.top=self.playrc.top
			self.point[1]=self.rect.centery
		elif self.rect.bottom>self.playrc.bottom:
			self.rect.bottom=self.playrc.bottom
			self.point[1]=self.rect.centery

		if self.rect.left<self.playrc.left:
			self.rect.left=self.playrc.left
			self.point[0]=self.rect.centerx
		elif self.rect.right>self.playrc.right:
			self.rect.right=self.playrc.right
			self.point[0]=self.rect.centerx

#########
		if self.rect.top<100:
			globe.scgame.itmanager.getitem()
###########


		if self.frame%6==0:
			self.aindex+=1

		if self.aindex>= len(self.anime):
			if self.anime==canime["stay"]:
				self.aindex=0
			else:
				self.aindex-=4


	def hit(self):
		if self.status==cstatus["normal"]:
			globe.mgame.msmanager.play_SE("miss")
			self.tcount=0
			self.status=cstatus["hit"]



	def update(self):
		if self.power>500:
			self.power=500

		self.keys=pygame.key.get_pressed()

		if self.status==cstatus["hit"]:
			if self.tcount>=20:
				self.miss()
			else:
				self.tcount+=1



		if self.status!=cstatus["crash"]:
			self.move()

		else:
			self.tcount+=1

			if self.life<0 and self.tcount==20:
                                globe.hiscore=globe.scgame.hiscore
                                globe.mgame.call(scene_gameover.Scene_GameOver)
			if self.tcount<=60:
				self.point[1]-=1

			else:

				self.status=cstatus["wudi"]
				self.tcount=0

				


		if self.status==cstatus["wudi"]:
			self.tcount+=1
			if self.tcount>300:
				self.status=cstatus["normal"]
				self.tcount=0

		

		elif self.status==cstatus["sc"]:
			self.tcount+=1
			if self.tcount>360:
				self.status=cstatus["scwudi"]
				globe.scgame.blmanager.clear_enbl()
				self.tcount=0

		elif self.status==cstatus["scwudi"]:
			self.tcount+=1
			if self.tcount>180:
				self.status=cstatus["normal"]
				self.tcount=0
#数据！！！


		self.frame+=1

	def draw(self,screen):

		self.rect.centerx=int(self.point[0])
		self.rect.centery=int(self.point[1])



		if self.status!=cstatus["normal"] and self.status!=cstatus["hit"]:
			tmp=cache.cache_set_alpha(self.anime[self.aindex],(self.frame%15)*60/15+100,True)
			tmp=cache.cache_set_mask(tmp,(100,0,100,40),True)
			screen.blit(tmp,self.rect)
		else:
			screen.blit(self.anime[self.aindex],self.rect)

		tmp=cache.cache_rotate(canime["panding"],self.frame,True)
		tprc=tmp.get_rect()
		if self.keys[pygame.K_LSHIFT]:	
			if self.status!=cstatus["crash"]:
				tprc.center=self.rect.center
				screen.blit(tmp,tprc)
		if self.status==cstatus["crash"]:
			tprc.center=self.tmppd
			screen.blit(tmp,tprc)

