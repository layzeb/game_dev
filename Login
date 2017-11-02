# -*- coding: utf8 -*-
# Desenvolvido em MAR 2017

# A simple program to create an account and log-in

new_log = ""
new_pass = ""
run = True

def menu():
	global new_log
	global new_pass
	global run
	
	while run:
		print("\n\t\tWELCOME TO LAYB'S!!!\n")
		act = input("First access? Create an account [Type 'C']:\nIf you have an account, sign-in [Type 'S']:\n")
		if act == "C" or act == 'c':
			register()
		elif act == "S" or act == 's':
			if new_log == "" and new_pass == "":
				print("Account doesn't exist! Please, create an account.\n")
				continue
			login()
		else:
			print("Invalid entry, try again!")


def register():
	global new_log
	global new_pass
	reg = True
	
	while reg:
		create_log = input("Create your Login [only letters and numbers]: \n")
		create_pass = input("Create your password [until 5 chars]: \n")
		if len(create_pass) > 5:
			print("Invalid password\n")
			continue
		else:
			new_log = create_log
			new_pass = create_pass
			
			print("Account created!\n")
			print("Your login: ", new_log)
			print("Your password: ", new_pass)
			reg = False


def login():
	global new_log
	global new_pass
	global run
	
	access = False
	
	while access == False:
		log = input("Insert your Login: \n")
		pwd = input("Insert you password: \n")
		
		if log == new_log:
			if pwd == new_pass:
				print("You are logged in!")
				access = True
				run =  False
			else:
				print("Wrong password, try again.\n")
				continue
		else:
			print("Wrong login, try again.\n")
			continue

menu()
