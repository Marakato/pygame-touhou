# -*- coding: UTF-8 -*-
import pygame
import pic.resource

from pygame.locals import *
import scene_title


import scene_game

import scene_title

import globe
import music
import cache

class GameWindow(object): #Single Object
	#screen
	#clock
	#rsmanager
	#scene
	#myfont
	#stack

	def __init__(self):
		pass

	def init(self):
		pygame.init()
		pygame.mixer.init()
		cache.cache_init()
		self.screen=pygame.display.set_mode([640,480])#,FULLSCREEN)
		self.clock=pygame.time.Clock()

		self.rsmanager=pic.resource.Resource()
		self.msmanager=music.MusicManager()
		self.goto(scene_title.Scene_Title)
		self.stack=[]

		self.myfont=pygame.font.SysFont(None,20)

		self.tst=0

		globe.hiscore=0

	def goto(self,sc):
		self.scene=sc()
		self.scene.update()


	def call(self,sc):
		self.scene.stop()
		self.stack.append(self.scene)
		self.scene=sc()
	def back(self):
		self.scene=self.stack.pop()
		self.scene.start()

	def run(self):
		while True:
#			self.screen.fill((255,255,255))
			self.scene.update()
			self.scene.draw(self.screen)

			img=self.myfont.render("fps:"+str((int)(self.clock.get_fps()*100)*1.0/100),True,(255,255,255))
			rc=img.get_rect()
			rc.bottomright=(640,480)
			self.screen.blit(img,rc)

			pygame.display.flip()
			self.clock.tick_busy_loop(60)
			self.tst+=1

if __name__ == '__main__':
	globe.mgame=GameWindow()
	globe.mgame.init()
	globe.mgame.run()
