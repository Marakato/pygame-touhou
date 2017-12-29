A Touhou-like Game Demo Written in Python
===

## 1. What's this

Just a demo of stg game written in python2.7 with pygame.

## 2. About Pictures and Music and SE

All of these come from Touhou Project.

## 3. Why the codes are so bad?

Because all codes are mainly written in less than a week, in order to hand in before deadline :( .

## 4. About all modules

* main.py

	Create the game window and the game loop.
	
* animation.py

	Animation Manager. Store all animation and can create it onto the screen.
	
* background.py

	Blit pictures onto the screen as background.
	
* bullet.py

	Store all bullets and remove the bullets out of screen. Have functions for colliding judgement. All bullets are treated as either circles or rectangles.

* cache.py

	After rotating sprites or changing the color and hue, this will store them.
	
* dialogue.py

	A dialogue window. Play before the boss.
	
* enemy.py

	Enemy or boss store the data and status of sprites. Manager can create enemy or boss onto the screen. 

* globe.py
	
	Just store global variable.
	
* hud.py

	Blit life and power and score onto the screen. Head Up Display.
	
* item.py

	Different item override the buffer ( buf, but mistakenly use 'buffer') function. Item manager creates and remove items, and call buffer to change the player's status.
	
* level1.py

	Instantiation all enemies and bullets.
	
* music.py

	Music manager. Play bgm and se.
	
* orbit.py

	Store the moving orbit for enemies and bullets.
	
* player.py

	Maintain all information about players. Deal with key events. Deal with fire and miss and invincible status.
	
* scene_xxx.py

	Store the data structure needed and blit them.
	
* tama.py

	tama means bowlder in Japanese. This file maintains the number of sub-gun according to power.
	
* pic/resource.py

	Read all pictures and bgm and se. Splitting all pictures into appropiate format for animation or background or hud manager. Put bgm and se into music manager.