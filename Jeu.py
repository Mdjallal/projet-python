from random import randrange
import pickle

def afficher(board):
	# affiche l'état du jeu a chauqe itération
	j = max(board)
	for n, i in enumerate(board) :
		print( n+1, '|', '*'*(i),' '*(j-i) ,' |', i )

def maj_score(loss, coups, players, score):
	# enregistre les nouveaux score et met a jour les meilleurs score

	s = sum( i*10**i for i in range(1, coups+1)  )
	perd  = players[ loss ]
	gagne = players[ (loss+1)%2 ]

	if perd in score.keys() :
		score[perd][1] = float('inf')
	else :
		score[perd] = [ float('inf'), float('inf') ] # inf au lieu de zero pour garder une consistance dans la logique des score

	if gagne in score.keys() :
		score[gagne][1] = s

		if score[gagne][0] > s :
			score[gagne][0] = s
	else :
		score[gagne] = [ s, s ]

	with open('score', 'wb') as f :
		pickle.dump(score, f)
	return score
	

def lire_score():
	# ouvre le fichier score a l'aide de pickle
	try :
		with open('score', 'rb') as f:
			return pickle.load(f)
		
	except :
		return {}

def afficher_top10(A):
	# affiche les 10 (si disposible) meilleurs score
	a, b = list(A.keys()), A.values()
	best, last = zip(*b)
	best = list(best)
	
	print('Nom : Meilleur Score')
	for i in range(10):
		j = best.index(min(best))
		print( a[j],':', min(best) )
		
		del a[j]
		del best[j]

		if len(best) == 0 :
			break

def Jeu():
	# le jeu lui meme
	score = lire_score()
	players = [0, 0]

	# initialisation de la partie
	players[0] = input('Joueur 1, entrez votre nom :')
	players[1] = input('Joueur 2, entrez votre nom :')

	board = [ randrange(5, 24) for _ in range(randrange(3,8)) ]
	turn  = randrange(0, 2)
	coups = 0
	afficher(board)

	# loop tour a tour entre les 2 joueurs
	while sum(board) > 0 :
		rang, pierre = input(f"Joueur {turn+1}, entrez votre coups :").split('-')
		rang, pierre = eval(rang), eval(pierre)

		board[ rang-1 ] -= pierre
		afficher(board)
		turn = ( turn+1 )%2
		coups += 1

	# fin de la partie
	score = maj_score(turn, coups, players, score)
	afficher_top10(score)

	# option de rejouer
	if input("Pour rejouer, taper 'oui' :") == 'oui' :
		Jeu()
Jeu()