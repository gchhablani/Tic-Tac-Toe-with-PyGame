import pygame as pg
import sys
from Game import *

def beginscreen():
	global game
	global turn
	turn={'Player':0,'Computer':0}
	game=Game()
	game.createboard()
	game.displaystr("Do you want to start first?",(game.windowsize/2-game.box_size*1.25,game.windowsize/2-game.windowsize/10),(0,255,100))
	game.displaystr("Press 'Y' for Yes.",(game.windowsize/2-game.box_size*1.25,game.windowsize/2),(0,255,100))
	pg.display.update()
	while True:
		for event in pg.event.get():
			if event.type==pg.QUIT:
				pg.quit()
				sys.exit()

			if event.type==pg.KEYDOWN:
				pg.display.update()
				if event.key==pg.K_y:
					turn['Player']=1
					gameplay()
					return
				else:
					turn['Computer']=1
					gameplay()
					return

def gameplay():

	game.screen.fill((0,0,0))
	game.lines()
	pg.display.update()
	status=-1
	while True:
		for event in pg.event.get():
			if event.type==pg.QUIT:
				pg.quit()
				sys.exit()

			if(turn['Computer']==1):
				game.AI()
				turn['Computer']=0
				turn['Player']=1
				pg.display.update()

			elif event.type==pg.MOUSEBUTTONDOWN:
				if (turn['Player']==1):
					x,y=event.pos
					done=game.human(x,y)
					pg.display.update()
					if done:
						turn['Computer']=1
						turn['Player']=0

			status=game.eval()
			if (status!=-1):
				break

		pg.display.update()
		if (status!=-1):
			break

	status=game.eval()
	pg.time.delay(200)
	game.screen.fill((0,0,0))
	if (status>0):
		game.displaystr("YOU WIN",(game.windowsize/2-game.box_size*1.25,game.windowsize/2-game.windowsize/10),(0,255,100))
	elif (status<0):
		game.displaystr("COMPUTER WINS",(game.windowsize/2-game.box_size*1.25,game.windowsize/2-game.windowsize/10),(0,255,100))
	else:
		game.displaystr("TIE!",(game.windowsize/2-game.box_size*1.25,game.windowsize/2-game.windowsize/10),(0,255,100))
	pg.display.update()
	pg.time.delay(500)
	gameoverscreen()

def gameoverscreen():

	game.screen.fill((0,0,0))
	game.displaystr("GAME OVER",(game.windowsize/2-game.box_size*1.25,game.windowsize/2-game.windowsize/10),(0,255,100))
	game.displaystr("RESTART(R) OR QUIT(Q)",(game.windowsize/2-game.box_size*1.25,game.windowsize/2),(0,255,100))
	pg.display.update()
	while True:
		for event in pg.event.get():
			if event.type==pg.QUIT:
				pg.quit()
				sys.exit()
			elif event.type==pg.KEYDOWN :
				if event.key==pg.K_r:
					game.screen.fill((0,0,0))
					pg.display.update()
					beginscreen()
					return None
				elif event.key==pg.K_q:
					pg.quit()
					quit()
					return None

pg.init()
beginscreen()
