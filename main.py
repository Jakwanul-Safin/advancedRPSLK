#!/usr/bin/python
# Arthor Jakwanul Safin

"""
main.py - Main entry point for game
"""

from random import *

#Start
def main(mainpath):

	game = RPSLKGame()
	display = textDisplay(game)
	game.addObserver(display)

	game.loop()

class RPSLKGame:

	def __init__(self):
		self.Observers = []
		self.turn = 0
		self.playerOne, self.playerTwo = Player("P1", self), Player("P2", self)
		self.playerOneMove = None
		self.playerTwoMove = None
		self.addObserver(self.playerOne)
		self.addObserver(self.playerTwo)

	def addObserver(self, newObserver):
		self.Observers.append(newObserver)

	def notify(self):
		for observer in self.Observers:
			observer.update()

	def loop(self):
		while True:
			self.turn += 1

			self.playerOneMove, self.playerTwoMove = self.askForMove()
			self.notify()

			if self.turn == 100:
				print("This game's gone on for long enough. Goodbye.")
				return

	def askForMove(self):
		return self.playerOne.askForMove(), self.playerTwo.askForMove()

class GameObserver:

	def __init__(self, thingToObserve):
		self.observable = thingToObserve

	def update(self):
		raise NotImplemenentedError("Update function need to be defined on every observer")

class Player(GameObserver):
	def __init__(self, name, game):
		GameObserver.__init__(self, game)
		self.name = name

	def __str__(self):
		return self.name

	def askForMove(self):
		return sample(["Rock", "Paper", "Scissor"], 1)[0]

	def update(self):
		pass

class textDisplay(GameObserver):

	def __init__(self, game):
		GameObserver.__init__(self, game)

	def update(self):
		print("Turn", self.observable.turn, ":", self.observable.playerOne, "plays", self.observable.playerOneMove, "and", self.observable.playerTwo, "plays", self.observable.playerTwoMove)

main(0)