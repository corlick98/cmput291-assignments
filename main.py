import sqlite3
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
	# This is the primary control area to the questions
	# connec to the database
	connection = sqlite3.connect('a2.db')

	print('Welcome to the Paper Review Database')
	
	exit_program = False
	# loop till user says to stop
	while exit_program == False:
		printoptions()
		try: #test if the user enters an integer
			user_input = int(input('Select the option number you wish to see: '))
		except ValueError:
			print()
			print('Please enter a valid selection')
			print()
			time.sleep(0.5)
			continue
		# tests if the user enters a valid choice
		if user_input not in range(1,8):
			print()
			print('Please enter a valid selection')
			print()
			time.sleep(0.5)
			continue
		# call the corresponding function for each question/task
		if user_input == 1:
			question1(connection)
		elif user_input == 2:
			question2(connection)
		elif user_input == 3:
			question3(connection)
		elif user_input == 4:
			question4(connection)
		elif user_input == 5:
			question5(connection)
		elif user_input == 6:
			question6(connection)
		elif user_input == 7:
			exit_program = True

	return
