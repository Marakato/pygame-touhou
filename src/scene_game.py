# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
import sys

import player
import tama
import background
import globe
import item
import animation
import bullet
import orbit
import enemy
import dialogue

from hud import *

import scene_menu

import level1




class Scene_Game(object):
	#time
	#rs = resourcemanager


	#score hiscore
	#life和bomb由Player类维护

	#pause

	def __init__(self):
		globe.scgame=self
		self.rs=globe.mgame.rsmanager


		globe.playrc=Rect(32,16,384,448)


		self.hud=Hud()
		self.time=-60

		self.player=player.Player()
		self.player.power=200
		self.bgmanager=background.BackgroundManager()
		self.itmanager=item.ItemManager()
		self.tmmanager=tama.TamaManager()
		self.blmanager=bullet.BulletManager()
		self.anmanager=animation.AnimeManager()
		self.enmanager=enemy.EnemyManager()

		self.txplayer=dialogue.TextPlayer()

		level1.init()


		self.score=0
		self.hiscore=globe.hiscore
		print(globe.hiscore)

		self.pause=False
		self.timestop=False

		globe.BOSSING=False

		#globe.mgame.msmanager.play_BGM("abc.mp3")

	def stop(self):
		self.pause=True
	def start(self):
		self.pause=False

	def tstop(self):
		self.timestop=True
	def tstart(self):
		self.timestop=False


	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
					pygame.quit()
					sys.exit()
				elif event.key == pygame.K_ESCAPE:
					globe.mgame.msmanager.play_SE("pause")
					globe.mgame.call(scene_menu.Scene_Menu)

				elif event.key == K_z and self.timestop==True:
					self.txplayer.command("next")


		if self.pause!=True:
			self.bgmanager.update()
			self.player.update()
			self.itmanager.update()
			self.tmmanager.update()
			self.blmanager.update()
			self.anmanager.update()
			self.enmanager.update()
			level1.update(self.time)
			if self.timestop!=True:
				self.time+=1
			else:
				self.txplayer.update()
			




	def draw(self,screen):
		screen.fill((255,255,255))
		self.bgmanager.draw(screen)
		self.itmanager.draw(screen)
		self.enmanager.draw(screen)
		self.player.draw(screen)
		self.tmmanager.draw(screen)
		self.anmanager.draw(screen)
		self.blmanager.draw(screen)
		self.hud.draw(screen)

		if self.timestop==True:
			self.txplayer.draw(screen)
