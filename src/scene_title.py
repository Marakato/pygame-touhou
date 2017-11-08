# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
import pic.resource
import sys
import globe
import scene_game


class Title_Menu(object):
	#btrc=[]
	#index
	#frame_now
	#rs
	#teji

	def __init__(self):
		self.btrc=[]  #Rects
		self.rs=globe.mgame.rsmanager.image
		self.btrc.append([495,200])
		self.btrc.append([500,240])
		self.image=[]
		self.image.append(self.rs["startb"])
		self.image.append(self.rs["startd"])
		self.image.append(self.rs["quitb"])
		self.image.append(self.rs["quitd"])

		self.index=0

		self.choose=False

		self.flash=0
		self.teji=pygame.Surface(globe.mgame.screen.get_size())
		self.teji.fill((0,0,0))


	def evcontrol(self):

		if self.choose==False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
						pygame.quit()
						sys.exit()
					if event.key == K_UP:
						if self.index==1:
							self.index=0
							self.btrc[0][0]-=5
							self.btrc[1][0]+=5
							globe.mgame.msmanager.play_SE("select")
					if event.key == K_DOWN:
						if self.index==0:
							self.index=1
							self.btrc[0][0]+=5
							self.btrc[1][0]-=5
							globe.mgame.msmanager.play_SE("select")
					if event.key == K_z:
						self.choose=True
						globe.mgame.msmanager.play_SE("select")
		else:
			self.flash+=1
			if self.flash>=20:
				if self.index==1:
					pygame.quit()
					sys.exit()
				else:
					if self.flash>=40:
						globe.mgame.goto(scene_game.Scene_Game)


			if self.flash%2==0 and self.flash<=40:
				tmp=self.image[self.index*2]
				self.image[self.index*2]=self.image[self.index*2+1]
				self.image[self.index*2+1]=tmp

	def draw(self,screen):
		screen.blit(self.image[self.index],self.btrc[0])
		screen.blit(self.image[3-self.index],self.btrc[1])
		if self.flash>=20:
			self.teji.set_alpha((self.flash-20)*12)
			screen.blit(self.teji,(0,0))


class Scene_Title(object):
	#rs
	#menu
	def __init__(self):
		self.rs=globe.mgame.rsmanager
		self.menu=Title_Menu()



	def update(self):
		self.menu.evcontrol()


	def draw(self,screen):
		screen.blit(self.rs.image["background"],(0,0))
		self.menu.draw(screen)
