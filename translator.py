"""This module translates written words typed into the terminal window into a foreign language using the Google translator API"""

from googletrans import Translator, constants
from pprint import pprint
import time


banner = r'''


		MMMMMMMMMMMMMMMMMMMMMMMMMMMNdyso+/::::::::::://+oshdNMMMMMMMMMMMMMMMMMMMMMMMMMMM
		MMMMMMMMMMMMMMMMMMMMMMmho/::::::::::::::::::::::::::::+sdNMMMMMMMMMMMMMMMMMMMMMM
		MMMMMMMMMMMMMMMMMMNho:::::::::::::::::::::::::::::::::::::+sdMMMMMMMMMMMMMMMMMMM
		MMMMMMMMMMMMMMMNh+::::::::::::::::::::::::::::::::::::::::::::odMMMMMMMMMMMMMMMM
		MMMMMMMMMMMMMdo:::::::::::::::::::::::::::::::::::::::::::::::::/yNMMMMMMMMMMMMM
		MMMMMMMMMMMd+::::::::::::::::::::::::::::::::::::::::::::::::::::::omMMMMMMMMMMM
		MMMMMMMMMd+::::::::::::::::::::::::::::::::::::::::::::::::::::::::::sNMMMMMMMMM
		MMMMMMMNo::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::hMMMMMMMM
		MMMMMMd:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::+NMMMMMM
		MMMMMy:::::::::::::::::::-------------------:::::::::::::::::::::::::::::/dMMMMM
		MMMMo::::::::::::::::--..````````````````````.--:::::::::::::::::::::::::::dMMMM
		MMMo:::::::::::::::-.```````````````````````````.-::::::::::::::::::::::::::dMMM
		MMy:::::::::::::::-```````````````````````````````--:::::::::::::::::::::::::mMM
		Mm:::::::::::::::-`````````````````````````````````.:::::::::::::::::::::::::/MM
		M/::::::::::::::-````````....................```````-:::::::::::::::::::::::::yM
		d:::::::::::::::.````````....................```````.::::::::::::::::::::::::::N
		o:::::::::::::::.````````````````````````````````````-:::::::::::::::::::::::::h
		::::::::::::::::.`````````..........````````````````.::oo+:::::::::::::::::::::o
		::::::::::::::::-```````.------------```````````````-:/sssso/::::::::::::::::::/
		:::::::::::::::::.`````````````````````````````````.::osssssso::::::::::::::::::
		::::::::::::::::::.```````````````````````````````.-:ossssssss+:::::::::::::::::
		:::::::::::::::::::-.````````````````````````````-::ossssssssss::::::::::::::::/
		:::::::::::::::::::::-..``````````````````````.-::+ssssssssssss/:::::::::::::::o
		o:::::::::::::::::::::::--.`````````......---::/ossssssssssssss::::::::::::::::h
		d:::::::::::::::::::::::::-```````.-://///++osssssssssssssssss/::::::::::::::::N
		M+::::::::::::::::::::::::-`````.-::::ossssssssssssssssssssso/::::::::::::::::yM
		Mm::::::::::::::::::::::::-```.-:::::::/ossssssssssssssssso/:::::::::::::::::/MM
		MMy::::::::::::::::::::::::---::::::::::::://+++osssssso:::::::::::::::::::::mMM
		MMMs:::::::::::::::::::::::::::::::::::::::::::::/ossss+::::::::::::::::::::dMMM
		MMMMy::::::::::::::::::::::::::::::::::::::::::::::/oss/:::::::::::::::::::dMMMM
		MMMMMy:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::/mMMMMM
		MMMMMMm/::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::oNMMMMMM
		MMMMMMMMs:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::/dMMMMMMMM
		MMMMMMMMMmo::::::::::::::::::::::::::::::::::::::::::::::::::::::::::yNMMMMMMMMM
		MMMMMMMMMMMdo::::::::::::::::::::::::::::::::::::::::::::::::::::::yNMMMMMMMMMMM
		MMMMMMMMMMMMMms:::::::::::::::::::::::::::::::::::::::::::::::::/yNMMMMMMMMMMMMM
		MMMMMMMMMMMMMMMMdo:::::::::::::::::::::::::::::::::::::::::::/smMMMMMMMMMMMMMMMM
		MMMMMMMMMMMMMMMMMMMds/::::::::::::::::::::::::::::::::::::+ymMMMMMMMMMMMMMMMMMMM
		MMMMMMMMMMMMMMMMMMMMMMNds+:::::::::::::::::::::::::::/oydMMMMMMMMMMMMMMMMMMMMMMM
		MMMMMMMMMMMMMMMMMMMMMMMMMMMNdhys+//::::::::://+osyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMM

					[Sven Eschlbeck] [2021]



Hello! Welcome to the simple instant translator...

Enter 'q' to quit.
'''


print(banner)


prompt2 = r"""
Please specify the language you wish to translate to.

Press '1' for French.			Press '2' for German.			Press '3' for Italian.

Leave blank for default (English).
"""


while True:
	print("-----------------------------------------------------------------------------------------------------------------------------")
	user_text = input("\nPlease type in the text/ message you would like to translate.\nYour entry should look like this: 'This is an example message.' but without quotes.\n")
	# Aborting if a 'q' is given
	if user_text == 'q':
		break

	print("\n-----------------------------------------------------------------------------------------------------------------------------")
	translation_language = input(prompt2)

	if translation_language == '1':
		final_language = 'fr'
	if translation_language == '2':
		final_language = 'de'
	if translation_language == '3':
		final_language = 'it'
	if translation_language == 'q':
		break

	# Initializing the Google translator API
	translator = Translator()

	print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
	# Translate the audi recording to the specified language
	translation = translator.translate(f"{user_text}", dest = final_language)

	print(f"Original text:\n\n{translation.origin}\n\nOriginal language: {translation.src}\n")

	
	# Printing info statement
	print("=============================================================================================================================")
	print("Translating...")
	animation = "|/-\\|/-\\"
	idx = 0
	while idx < 11:
	    print(animation[idx % len(animation)], end="\r")
	    idx += 1
	    time.sleep(0.3)
	print("=============================================================================================================================\n")

	print(f"New text: {translation.text}\n\nNew language: {translation.dest}")

	print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
	question_save_trans = input("Do you want to save the translated text/ message to a text file? [y/n]\n")
	
	if question_save_trans == 'y':
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		# Ask for the destination folder where the text should be stored
		destination_folder = input("Please specify the full path to the desired destination folder.\nYour entry should look like this: 'C:/User/...' but without quotes.\n")
		# Aborting if a 'q' is given
		if destination_folder == 'q':
			break

		# Ask for the file name
		file_name = input("\nPlease specify the desired file name.\nYour entry should look like this: 'example_file.txt' but without quotes.\n")
		# Aborting if a 'q' is given
		if file_name == 'q':
			break

		# Creating individual user path from destination folder and file name
		user_path = f"{destination_folder}/{file_name}"
		with open(user_path, 'w') as f:
			# Write the text into the file
			f.write(f"{translation.text}")

		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		print("Your translation text file is created...\nGo to the folder you specified to access it.")

	if question_save_trans == 'n':
		pass
	if question_save_trans == 'q':
		break

	print("\n-------------------------------------------------------------------------------------------------------------------------------\n")
	question_more = input("Do you wish to translate another text/ message? [y/n]\n")
	if question_more == 'y':
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break
