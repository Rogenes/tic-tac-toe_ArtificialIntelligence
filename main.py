import numpy as np
import sys
import random
import time
import os

game = np.array([[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]) 
tree = None

#player1 start, computer

class node(object):
	def __init__(self,turn,matrix):
		self._node=[]
		self._prev=None
		self._matrix=matrix
		self._turn=turn
		self._children=0
		self._level=0
		self._value=None
	def next(self,child):
		return self._node[child]
	def prev(self):
		return self._prev
	def add(self,turn, matrix):
		node1=node(turn, matrix)
		self._node.append(node1)
		self._children=self._children+1
		node1._prev=self
		node1._level=self._level+1
		return node1

def result(game):
	if (game[0][0] == game[0][1] == game[0][2]):
		if(game[0][0] == game[0][1] == game[0][2] == 'x'):
			return 'player1'
		elif (game[0][0] == game[0][1] == game[0][2] == 'o'):
			return 'player2'
	elif(game[1][0] == game[1][1] == game[1][2]):
		if(game[1][0] == game[1][1] == game[1][2] == 'x'):
			return 'player1'
		elif(game[1][0] == game[1][1] == game[1][2] == 'o'):
			return 'player2'
	elif (game[2][0] == game[2][1] == game[2][2]):
		if (game[2][0] == game[2][1] == game[2][2] == 'x'):
			return 'player1'
		elif(game[2][0] == game[2][1] == game[2][2] == 'o'):
			return 'player2'
	elif (game[0][0] == game[1][0] == game[2][0]):
		if (game[0][0] == game[1][0] == game[2][0] == 'x'):
			return 'player1'
		elif (game[0][0] == game[1][0] == game[2][0] == 'o'):
			return 'player2'
	elif (game[0][1] == game[1][1] == game[2][1]):
		if (game[0][1] == game[1][1] == game[2][1] == 'x'):
			return 'player1'
		elif (game[0][1] == game[1][1] == game[2][1] == 'o'):
			return 'player2'
	elif game[0][2] == game[1][2] == game[2][2]:
		if (game[0][2] == game[1][2] == game[2][2] == 'x'):
			return 'player1'
		elif (game[0][2] == game[1][2] == game[2][2] == 'o'):
			return 'player2'
	elif (game[0][0] == game[1][1] == game[2][2]):
		if (game[0][0] == game[1][1] == game[2][2] == 'x'):
			return 'player1'
		elif (game[0][0] == game[1][1] == game[2][2] == 'o'):
			return 'player2'
	elif (game[2][0] == game[1][1] == game[0][2]):
		if (game[2][0] == game[1][1] == game[0][2] == 'x'):
			return 'player1'
		elif (game[2][0] == game[1][1] == game[0][2] == 'o'):
			return 'player2'
	else:
		for row in game:
			for element in row:
				if element == ' ':
					return 'endOfTurn'
		return 'draw'

def createChild(turn, game, tree):

	if(turn=='x'):
		turn='o' #Min's turn
	elif(turn=='o'):
		turn='x' #Max's turn
	possibilities = []

	tree=tree.add(turn,game)

	if(result(game)=='player1'):
		a = []
		a.append(1)
		tree._value=a
		tree=tree.prev()
		return a
	elif(result(game)=='player2'):
		a = []
		a.append(-1)
		tree._value=a
		tree=tree.prev()
		return a
	elif(result(game)=='draw'):
		a = []
		a.append(0)
		tree._value=a
		tree=tree.prev()
		return a

	for i in range(3):
		for j in range(3):

			if(game[i][j]==' '):
				matrix = game.copy()
				matrix[i][j] = turn
				possibilities.extend(createChild(turn,matrix,tree))

	if(turn=='x'):
		v = []
		v.append(max(possibilities))
		tree._value=v
		return v
	elif(turn=='o'):
		v = []
		v.append(min(possibilities))
		tree._value=v
		return v

def checkPosition(position, playingGame):
	if(position==1 and playingGame[0][0]==' '):
		playingGame[0][0]='o'
		return True
	elif(position==2 and playingGame[0][1]==' '):
		playingGame[0][1]='o'
		return True
	elif(position==3 and playingGame[0][2]==' '):
		playingGame[0][2]='o'
		return True
	elif(position==4 and playingGame[1][0]==' '):
		playingGame[1][0]='o'
		return True
	elif(position==5 and playingGame[1][1]==' '):
		playingGame[1][1]='o'
		return True
	elif(position==6 and playingGame[1][2]==' '):
		playingGame[1][2]='o'
		return True
	elif(position==7 and playingGame[2][0]==' '):
		playingGame[2][0]='o'
		return True
	elif(position==8 and playingGame[2][1]==' '):
		playingGame[2][1]='o'
		return True
	elif(position==9 and playingGame[2][2]==' '):
		playingGame[2][2]='o'
		return True
	return False

def play(tree, playingGame):
	round = 0
	turn = -1
	lalala = True

	while True:
		turn*=-1
		os.system('cls' if os.name == 'nt' else 'clear')
		
		if(result(playingGame)=='player1'):
			showBoard(playingGame)
			print(f'Você perdeu.')
			time.sleep(1)
			print(f'Hahahahahaha.')
			time.sleep(1)
			print(f'Que pena...')
			time.sleep(1)
			print(f'Triste, não?...')
			time.sleep(1)
			print(f'Triste...\n')
			break
		elif(result(playingGame)=='draw'):
			showBoard(playingGame)
			print(f'Você empatou.')
			time.sleep(1)
			print(f'Hahahahahaha.')
			time.sleep(1)
			print(f'Que pena...')
			time.sleep(1)
			print(f'Triste, não?...')
			time.sleep(1)
			print(f'Triste...\n')
			break

		if(lalala==False):
			showBoard(playingGame)

		if(turn==1):
			print(f'\nVez do Seu oponente, aguarde...')
			time.sleep(2)
			if(lalala==True):
				round+=1
				lalala=False
			elif(lalala==False):
				round+=1

				# print('Opcoes:')
				# for x in tree._node:
				# 	print(f'{x._matrix}')
				# 	print(f'{x._value}\n\n')
				# pause = input('pausado')

				jump=0
				for x in tree._node:
					c = []
					c.append(1)
					if( np.array_equal(x._value, c) ):
						tree=x
						playingGame=x._matrix
						jump+=1
						break
				if(jump<1):
					for x in tree._node:
						d = []
						d.append(0)
						if( np.array_equal(x._value, d) ):
							tree=x
							playingGame=x._matrix
							break

		elif(turn==-1):
			round+=1
			print(f'Sua vez')
			while True:
				position = input("Entre com a posicao que deseja jogar:")

				if(not position.isdigit() or int(position)>9 or int(position)<1 or not checkPosition(int(position),playingGame)):
					print(f'Posicao invalida, tente novamente.')
				else:
					break
			for x in tree._node:
				if( np.array_equal(x._matrix, playingGame) ):
					tree=x

def showBoard(matrix):
	print(f'Game:\n')
	
	print ('  ' + matrix[0][0] + '  |  ' +matrix[0][1]+ '  |  ' +matrix[0][2] )
	print ('-----------------')
	print ('  ' + matrix[1][0] + '  |  ' +matrix[1][1]+ '  |  ' +matrix[1][2] )
	print ('-----------------')
	print ('  ' + matrix[2][0] + '  |  ' +matrix[2][1]+ '  |  ' +matrix[2][2] )
	print('\n\n')

if __name__ == '__main__':
	print(f'\n\n|-----INICIANDO SEU JOGO-----|\n\n')
	gameCopy = game.copy()
	tree = node('x',gameCopy)
	turn  = 'x' #first step computer, x = max, o = min
	game[random.randint(0, 2)][random.randint(0,2)] = 'x'
	playingGame = game.copy()
	createChild(turn, game, tree)
	os.system('cls' if os.name == 'nt' else 'clear')
	info = np.array([['1','2','3'], ['4','5','6'], ['7','8','9']]) 
	print(f'Este é o quadro de jogo, com suas respectivas posições:\n')
	showBoard(info)
	pause = input('\nAperete enter para continuar...\n')
	showBoard(playingGame)

	

	play(tree.next(0),playingGame)
