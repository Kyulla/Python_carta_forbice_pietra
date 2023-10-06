import random as scf

def keepplaying():
	choice = input("Vuoi continuare a giocare? (Si/No): ")
	choice = choice.lower()
	return choice.replace(" ","")

def bot():
	return scf.randint(1,3)
	#Sasso = 1, Carta = 2, Forbice = 3

def playerturn():
	choice = input("\nSasso\nCarta\nForbice\nScegli tra le 3 opzioni: ")
	choice = choice.lower()
	return choice.replace(" ", "")

playagain = True

while playagain:
	validchoice = False
	botchoice = bot()

	while not validchoice:
		choice = playerturn()

		if choice == "sasso" or choice == "carta" or choice == "forbice":
			validchoice = True
		else:
			print("Errore, scelta non valida.")


	match botchoice:
		case 1:
			print("\nIl bot ha scelto Sasso.")

			if choice == "sasso":
				print("Pareggio.")

			elif choice == "carta":
				print("Hai vinto.")

			else:
				print("Hai perso.")

		case 2:
			print("\nIl bot ha scelto carta.")

			if choice == "sasso":
				print("Hai perso.")

			elif choice == "carta":
				print("Pareggio.")

			else:
				print("Hai vinto.")

		case 3:
			print("\nIl bot ha scelto forbice.")

			if choice == "sasso":
				print("Hai Vinto.")

			elif choice == "carta":
				print("Hai perso.")

			else:
				print("Pareggio.")


	validchoice = False

	while not validchoice:
		playagain = keepplaying()

		if playagain == "si" or playagain == "no":
			validchoice = True

			if playagain == "no":
				playagain = False

		else:
			print("Errore, scelta non valida.")

print("Grazie per aver giocato, alla prossima...")
