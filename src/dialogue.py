# -*- encoding: UTF-8 -*-
import pygame
from pygame.locals import *
import scene_menu
import globe


global globaltext

global globaltext

globaltext=[
	[u'大家好，就不自我介绍了。'],
	[u'美工死绝、编剧死绝。',u'就不要指望这个游戏有多好。'],
	[u'所以并无和神主一样的剧本,',u'取而代之的是...'],
	"showright",
	[u'你好啊⑨，1+1等于多少？'],
	"showleft",
	[u'⑨！！！'],
	"showright",
	[u'那好，开打吧。']
]





class TextPlayer(object):
	def __init__(self):
		self.texts=globaltext
		self.index=0
		self.lpic=globe.mgame.rsmanager.image["cirno"]
		self.rpic=globe.mgame.rsmanager.image["reimu"]
		self.lpic_av=False
		self.rpic_av=False

		self.font=pygame.font.SysFont('msyh.ttc',20)

		self.rc=pygame.Rect(globe.playrc.left,globe.playrc.bottom-100,globe.playrc.width-128,100)


	def command(self,cm=None):
		if cm=="next":
			self.index+=1
		else:
			cm=self.texts[self.index]
			if cm=="showleft":
				self.lpic_av=True
				self.rpic_av=False
				self.index+=1
			elif cm=="showright":
				self.rpic_av=True
				self.lpic_av=False
				self.index+=1

	def update(self):
		if self.index<len(self.texts):
			self.command()
		else:
			globe.scgame.time+=1
			globe.scgame.tstart()
			return
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_z:
					self.command("next")
				elif event.key == pygame.K_ESCAPE:
					globe.mgame.msmanager.play_SE("pause")
					globe.mgame.call(scene_menu.Scene_Menu)

	def draw(self,screen):
		if globe.scgame.timestop==True:
			if self.lpic_av==False:
				screen.fill((200,200,200),self.rc,BLEND_RGB_ADD)
				if type(self.texts[self.index])==str:
					txtimg=self.font.render(self.texts[self.index],True,(255,0,0))
					screen.blit(txtimg,self.rc.topleft)
				elif type(self.texts[self.index])==list:
					for i in range(len(self.texts[self.index])):
						txtimg=self.font.render(self.texts[self.index][i],True,(255,0,0))
						screen.blit(txtimg,(self.rc.left,self.rc.top+i*40))
				if self.rpic_av==True:
					tprc=self.rpic.get_rect()
					tprc.bottomleft=self.rc.bottomright
					screen.blit(self.rpic,tprc)
				elif self.lpic_av==True:
					tprc=self.lpic.get_rect()
					tprc.bottomright=self.rc.bottomleft
					screen.blit(self.lpic,tprc)

			else:
				tp=self.rc.copy()
				tp.left+=128
				screen.fill((200,200,200),tp,BLEND_RGB_ADD)

				if type(self.texts[self.index])==str:
					txtimg=self.font.render(self.texts[self.index],True,(255,0,0))
					screen.blit(txtimg,tp.topleft)
				elif type(self.texts[self.index])==list:
					for i in range(len(self.texts[self.index])):
						txtimg=self.font.render(self.texts[self.index][i],True,(255,0,0))
						screen.blit(txtimg,(tp.left,tp.top+i*40))
				if self.rpic_av==True:
					tprc=self.rpic.get_rect()
					tprc.bottomleft=tp.bottomright
					screen.blit(self.rpic,tprc)
				elif self.lpic_av==True:
					tprc=self.lpic.get_rect()
					tprc.bottomright=tp.bottomleft
					screen.blit(self.lpic,tprc)
