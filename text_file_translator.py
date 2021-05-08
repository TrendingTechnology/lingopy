"""This module translates written words from a text file into a foreign language using the Google translator API"""

from googletrans import Translator, constants
from pprint import pprint
import time


banner = r'''


	 ``````` ```` `` ```` ``````` ```` ``````` ```` ``````` ```` ``````` ```` `` ```
	 ``````` ```` `` ```` ``````` ```` ``````` ```` ``````` ```` ``````` ```` `` ```
	``````./ssyysyyyysyyyyyyysyyyysyyyyyyysyyys+.```````````````````````````````````
	```` +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy````` ``````` ```` ``````` ```` ``
	````-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/`````````````````````````````````
	 ```:MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+ ``````` ```` ``````` ```` `` ```
	````-MMMMMMMMMMMMMMMMMMMMd++sMMMMMMMMMMMMMMMMM+`````````````````````````````````
	````-MMMMMMMMMMMMMMMMMMMMy``-MMMMMMMMMMMMMMMMM+```` ```` `` ```` ``````` ```` ``
	````-MMMMMMMd```````````````````````````MMMMMM+`````````````````````````````````
	 ```:MMMMMMMm++++++++++++++++++/`` +++++MMMMMM+ ``````` ```` ``````` ```` `` ```
	````-MMMMMMMMMMMMMNhsNMMMMMMMMMo``:MMMMMMMMMMM+`````````````````````````````````
	````-MMMMMMMMMMMMM/``-dMMMMMMMy```dMMMMMMMMMMM+```` ``````` ```` ``````` ```` ``
	````-MMMMMMMMMMMMMMs```+NMMMNo```hMMMMMMMMMMMM+`````````````````````````````````
	 ```:MMMMMMMMMMMMMMMm:```oNy. `-mMMMMMMMMMMMMM+ ``````` ```` ``````` ```` `` ```
	 ```:MMMMMMMMMMMMMMMMMh:`````.yMMMMMMMMMMMMMMM+ ``````` ```` ``````` ```` `` ```
	````-MMMMMMMMMMMMMMMMms:` ```.ohNMho/:--------.```` ``````` ```` ``````` ```` ``
	````-MMMMMMMMMMMMmy+.```-ody/` ``````-----------------------------------````` ``
	````-MMMMMMMMMMy.```.:smMMMMMNh```-hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy.`````
	 ```:MMMMMMMMMMM:```/mMMMMMMMMs``-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN` ```
	````-MMMMMMMMMMh-`````oNMMMMMM+``+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-````
	````-MMMMMMMMm/```sd:``.hMMMMM+``+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-` ``
	`````NMMMMMMo```/NMMMy.``:mMMM+``+MMMMMMMMMMMMMMMMMMs...sMMMMMMMMMMMMMMMMMM-````
	 `` `.yNMMh-` -dMMMMMMN+```oNM+``+MMMMMMMMMMMMMMMMMd``` `dMMMMMMMMMMMMMMMMM- ```
	````````.-``.yMMMMMMMMMMd:``.-.``+MMMMMMMMMMMMMMMMN.``-``.NMMMMMMMMMMMMMMMM-````
	```` ``````-hdddMMMMMMmddd+``` ``+MMMMMMMMMMMMMMMM: `/N-``/MMMMMMMMMMMMMMMM-` ``
	````````````````MMMMMM+``````````/NMMMMMMMMMMMMMMo``.NMd```sMMMMMMMMMMMMMMM-````
	 ``````` ```` ``MMMMMM+`````` /-```+mMMMMMMMMMMMh```hMMMo```dMMMMMMMMMMMMMM- ```
	````````````````MMMMMM+```````yMh/```:hMMMMMMMMN.``+MMMMM-``.NMMMMMMMMMMMMM-````
	```` ``````` ```--:--:--:-:--:hMMMmo.` .sNMMMMM:````.....`` `/MMMMMMMMMMMMM-` ``
	```` ``````` ```.sNMMMMMMMMMMMMMMMMMMy:```+dMMo```/+++++++/ ``oMMMMMMMMMMMM-` ``
	 ``````` ```` `` `.sNMMMMMMMMMMMMMMMMMN+`` `sh` `+MMMMMMMMM/ ``dMMMMMMMMMMM- ```
	 ``````` ```` `` ```.sNMMMMMMMMMMMMMm+.``-sNN.` .NMMMMMMMMMN.``.NMMMMMMMMMM- ```
	``````````````````````````````yMMMh:```/hMMMNmmmNMMMMMMMMMMMNmmmNMMMMMMMMMM-````
	```` ``````` ```` ``````` ````yNs.``.omMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-` ``
	``````````````````````````````-```-yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-````
	 ``````` ```` `` ```` ``````` ```/MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM. ```
	``````````````````````````````````sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo`````
	```` ``````` ```` ``````` ```` `` `.+syyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyys/.``` ``
	````````````````````````````````````````````````````````````````````````````````
	 `` ```` ```` `` ```` ```` `` ```` ```` `` ```` `` ```` ```` `` ```` ```` `` ```
				[Sven Eschlbeck] [2021]



Hello! Welcome to the simple translator for written words...

Enter 'q' to quit.
'''


print(banner)


prompt2 = r"""
Please specify the language you wish to translate the text file to.

Press '1' for French.			Press '2' for German.			Press '3' for Italian.

Leave blank for default (English).
"""


while True:
	print("-----------------------------------------------------------------------------------------------------------------------------")
	origin_path = input("\nPlease specify the full path to the folder including the file name.\nYour entry should look like this: 'C:/User/.../example.txt' but without quotes.\n")
	# Aborting if a 'q' is given
	if origin_path == 'q':
		break
	# Loading text file
	filename = origin_path
	with open(filename, 'r') as f:
		text_input = f.read()
	
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
	translation = translator.translate(f"{text_input}", dest = final_language)

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
	question_save_trans = input("Do you want to save the translated text to a text file? [y/n]\n")
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
	question_more = input("Do you wish to translate another file? [y/n]\n")
	if question_more == 'y':
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break
