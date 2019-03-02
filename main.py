import sqlite3
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
	# This is the primary control area to the questions
	
	connection = sqlite3.connect('a2.db')

	print('Welcome to the Paper Review Database')
	
	exit_program = False
	
	while exit_program == False:
		printoptions()
		try:
			user_input = int(input('Select the option number you wish to see: '))
		except ValueError:
			print()
			print('Please enter a valid selection')
			print()
			time.sleep(1)
			continue
		
		if user_input not in range(1,8):
			print()
			print('Please enter a valid selection')
			print()
			time.sleep(1)
			continue
			
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
