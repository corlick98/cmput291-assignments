import sqlite3
import time

def main():
	# This is the primary control area to the questions
	
	print('Welcome to the Paper Review Database')
	
	exit_program = False
	
	while exit_program == False:
		printoptions()
		try:
			user_input = int(input('Select the option number you wish to see: '))
		except TypeError:
			print('Please enter a valid selection')
		
		if user_input not in range(1,8):
			print('Please enter a valid selection')
			time.sleep(1)
			continue
		if user_input == 1:
			question1()
		elif user_input == 2:
			question2()
		elif user_input == 3:
			question3()
		elif user_input == 4:
			question4()
		elif user_input == 5:
			question5()
		elif user_input == 6:
			question6()
		elif user_input == 7:
			exit_program = True



	return
