"""This module translates spoken words into a foreign language using the Google translator API"""

# Importing required modules
from googletrans import Translator, constants
from pprint import pprint
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import time

# Defining banner (to be shown when starting the program)
banner = r'''
                                                                                                                                                      
     :++++++++++++++++++++++++++++++++oo-                                                   
     /+++++++++++++++++++++++++++++++++o+`                                                  
     /++++++++++++++++++++++++++++++++ooo/                                                  
     /+++++++++++++++++++++++++++++++ooooo-                                                 
     /+++++++++++++++++++++++++++++++ooooo+.```````````````````````````````                 
     /++++++++++++++++++++++++++++++ooooooo+-..```````````````````````````````              
     /+++++++++++++++++++++++++++++ooooooooo/-..```````````````````````````````             
     /+++++++++++++++/:--....--:/+oooooooooo+:--.``````````````````````````````             
     /+++++++++++++:.````````````./oooooooooo+--...````````````````````````````             
     /+++++++++++:.`````.-::-.``.:+ooooooooooo:--....``````````````````````````             
     /++++++++++:````.:++++++o+/+ooooooooooooo+:--.....````````````````````````             
     /+++++++++/````.+++o+++++++++++++ooooooooo/--.......`...``````````````````             
     /+++++++++-````++o+oo+.``````````+ooooooooo:--......-ooo.`````````````````             
     /++++++o++-````+ooooo+```````````+ooooooooo+:----...-sss-...........``````             
     /+++++++oo/````-+oooo+//////`````+ooooooooooossssssssssssooooooooooo``````             
     /oooooooooo-````-++ooooooo+-````:ooooooooooooo+++++++++++++oooo/////`.````             
     /oooooooooo+-`````.::///:-`````:ooooooooooooo+---.........-oso:``````.````             
     /oooooooooooo/-``````````````-/ooooooooooooooo//+++-.....-oss+..``````````             
     /oooooooooooooo+/-..````..-:+oooooooooooooooooo:+sso:...-oss+.....````````             
     /ooooooooooooooooo++++++++ooooooooooooooooooooo+:+sso/./oss/........``````             
     /ooooooooooooooooooooooooooooooooooooooooooooooo/-:ossosso:...........``.`             
     /oooooooooooooooooooooooooooooooooooooooooooooooo:-/sssss:...............`             
     /oooooooooooooooooooooooooooooooooooooooooooooooo+osso+oso+:.............`             
     /oooooooooooooooooooooooooooooooooooooooooooooooooss+-.-/oso+:...........`             
     /oooooooooooooooooooooooooooooooooooooooooooooooooo/--...-/oso+:.........`             
     /oooooooooooooooooooooooooooooooooooooooooooooooooo+---....-+oso+........`             
     -ooooooooooooooooooooooooooooooooooooooooooooooooooo/--......-++:........`             
      :+oooooooooooooooooooooooooooooooooooooooooooooooooo:--.................`             
       `.--------------------------------sssssssssssssssss/--.................`             
                                         :yyyyyyyyyyyyys+:---.................`             
                                          +yyyyyyyyyys+:---...................`             
                                          `syyyyyyys+:----....................`             
             [Sven Eschlbeck] [2021]       :yyyyyso:----......................`             
           

			

Hello! Welcome to the simple translator for spoken words...

Enter 'q' to quit.
'''

# Printing the banner
print(banner)

# Listing the languages that can be detected
prompt = r"""
Please specify the spoken language.

Press '1' for French.			Press '2' for German.			Press '3' for Italian.
Press '4' for Russian.			Press '5' for Dutch.			Press '6' for Mandarin (Han Yu).
Press '7' for Spanish.  		Press '8' for Turkish.  		Press '9' for Swedish.
Press '10' for Portuguese.		Press '11' for Japanese.  		Press '12' for Korean.
Press '13' for Polish. 			Press '14' for Czech.  			Press '15' for Finnish.
Press '16' for Hebrew. 			Press '17' for Hungarian.		Press '18' for Indonesian.
Press '19' for Malaysian.		Press '20' for Norwegian.		Press '21' for Romanian.
Press '22' for Serbian.   		Press '23' for Slovak.   		Press '24' for Afrikaans.

Leave blank for default (English).
"""

# Listing the languages that are supported
prompt2 = r"""
Please specify the language you wish to translate to.

Press '1' for French.			Press '2' for German.			Press '3' for Italian.
Press '4' for Afrikaans.		Press '5' for Albanian.			Press '6' for Amharic.
Press '7' for Arabic.			Press '8' for Armenian.			Press '9' for Azerbaijani.
Press '10' for Basque.			Press '11' for Belarusian.		Press '12' for Bengali.
Press '13' for Bosnian.			Press '14' for Bulgarian.		Press '15' for Catalan.
Press '16' for Cebuano.			Press '17' for Chichewa.		Press '18' for Chinese (Han Yu).
Press '19' for Corsican.		Press '20' for Croatian.		Press '21' for Chinese (traditional).
Press '22' for Czech.			Press '23' for Danish.			Press '24' for Dutch.
Press '25' for Esperanto.		Press '26' for Estonian.		Press '27' for Filipino.
Press '28' for Finnish.			Press '29' for Frisian.			Press '30' for Galician.
Press '31' for Georgian.		Press '32' for Greek.			Press '33' for Gujarati.
Press '34' for Hausa.			Press '35' for Hawaiian.		Press '36' for Haitian creole.
Press '37' for Hebrew.			Press '38' for Hindi.			Press '39' for Hmong.
Press '40' for Hungarian.		Press '41' for Icelandic.		Press '42' for Igbo.
Press '43' for Indonesian.		Press '44' for Irish.			Press '45' for Japanese.
Press '46' for Javanese.		Press '47' for Kannada.			Press '48' for Kazakh.
Press '49' for Khmer.			Press '50' for Korean.			Press '51' for Kurdish (Kurmanji).
Press '52' for Kyrgyz.			Press '53' for Lao.		        Press '54' for Latin.
Press '55' for Latvian.			Press '56' for Lithuanian.		Press '57' for Luxembourgish.
Press '58' for Macedonian.		Press '59' for Malagasy.		Press '60' for Malay.
Press '61' for Malayalam.		Press '62' for Maltese.			Press '63' for Maori.
Press '64' for Marathi.			Press '65' for Mongolian.		Press '66' for Myanmar (Burmese).
Press '67' for Nepali.			Press '68' for Norwegian.		Press '69' for Pashto.
Press '70' for Persian.			Press '71' for Polish.			Press '72' for Portuguese.
Press '73' for Punjabi.			Press '74' for Romanian.		Press '75' for Russian.
Press '76' for Samoan.			Press '77' for Serbian.			Press '78' for Scots gaelic.
Press '79' for Sesotho.			Press '80' for Shona.			Press '81' for Sindhi.
Press '82' for Sinhala.			Press '83' for Slovak.			Press '84' for Slovenian.
Press '85' for Somali.			Press '86' for Spanish.			Press '87' for Sundanese.
Press '88' for Swahili.			Press '89' for Swedish.			Press '90' for Tajik.
Press '91' for Tamil.			Press '92' for Telugu.			Press '93' for Thai.
Press '94' for Turkish.			Press '95' for Ukrainian.		Press '96' for Urdu.
Press '97' for Uzbek.			Press '98' for Vietnamese.		Press '99' for Welsh.
Press '100' for Xhosa.			Press '101' for Yiddish.		Press '102' for Yoruba.
Press '103' for Zulu.

Leave blank for default (English).
"""

# Starting main while loop
while True:

	print("-----------------------------------------------------------------------------------------------------------------------------")
	lang = input(prompt)

	if lang == '1':
		language = 'fr-FR'
	if lang == '2':
		language = 'de-DE'
	if lang == '3':
		language = 'it-IT'
	if lang == '4':
		language == 'ru-RU'
	if lang == '5':
		language = 'nl-NL'
	if lang == '6':
		language = 'zh-CN'
	if lang == '7':
		language = 'es-ES'
	if lang == '8':
		language = 'tr'
	if lang == '9':
		language = 'sv-SE'
	if lang == '10':
		language = 'pt-PT'
	if lang == '11':
		language = 'ja'
	if lang == '12':
		language = 'ko'
	if lang == '13':
		language = 'pl'
	if lang == '14':
		language = 'cz'
	if lang == '15':
		language = 'fi'
	if lang == '16':
		language = 'he'
	if lang == '17':
		language = 'hu'
	if lang == '18':
		language = 'id'
	if lang == '19':
		language = 'ms-MY'
	if lang == '20':
		language = 'no-NO'
	if lang == '21':
		language = 'ro-RO'
	if lang == '22':
		language = 'sr-SP'
	if lang == '23':
		language = 'sk'
	if lang == '24':
		language = 'af'
	if lang == '':
		language = 'en-US'
	if lang == 'q':
		break


	print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

	# Asking for the duration of the planned recording
	length = input("How long do you plan to speak?\n\nDefine a time span.\nPress '1' for 30 seconds.\nPress '2' for 60 seconds.\nPress '3' for 90 seconds.\nPress '4' for 120 seconds.\nPress '5' for 300 seconds.\n\nLeave blank for default (10 seconds).\n")
	if length == '1':
		duration = 30
	if length == '2':
		duration = 60
	if length == '3':
		duration = 90
	if length == '4':
		duration = 120
	if length == '5':
		duration = 300
	if length == '':
		duration = 10
	if length == 'q':
		break


	# Initializing the recognizer
	r = sr.Recognizer()

	# Defining microphone as input source
	with sr.Microphone() as source:
		# Users starts speaking
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		print("Speak now!")
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		# Read the audio data from the default microphone
		audio_data = r.record(source, duration = duration)

		# Printing wait statement
		print("Recognizing voice...\n")
		animation = "|/-\\"
		idx = 0
		while idx < 6:
		    print(animation[idx % len(animation)], end="\r")
		    idx += 1
		    time.sleep(0.2)
		print("")

		# Convert speech to text
		text = r.recognize_google(audio_data, language = language)
		# Print text
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		print(f"Record:\n\n{text}")
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

	question_save = input("Do you want to save the original audio you just recorded to a text file? [y/n]\n")
	if question_save == 'y':
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
			f.write(f"{text}")

		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		print("Your original text file is created...\nGo to the folder you specified to access it.")
		print("\n-----------------------------------------------------------------------------------------------------------------------------")

	if question_save == 'n':
		pass
	if question_save == 'q':
		break

	print("\n-----------------------------------------------------------------------------------------------------------------------------")
	translation_language = input(prompt2)

	if translation_language == '':
		final_language = 'en'
	if translation_language == '1':
		final_language = 'fr'
	if translation_language == '2':
		final_language = 'de'
	if translation_language == '3':
		final_language = 'it'
	if translation_language == '4':
		final_language = 'af'
	if translation_language == '5':
		final_language = 'sq'
	if translation_language == '6':
		final_language = 'am'
	if translation_language == '7':
		final_language = 'ar'
	if translation_language == '8':
		final_language = 'hy'
	if translation_language == '9':
		final_language = 'az'
	if translation_language == '10':
		final_language = 'eu'
	if translation_language == '11':
		final_language = 'be'
	if translation_language == '12':
		final_language = 'bn'
	if translation_language == '13':
		final_language = 'bs'
	if translation_language == '14':
		final_language = 'bg'
	if translation_language == '15':
		final_language =  'ca'
	if translation_language == '16':
		final_language =  'ceb'
	if translation_language == '17':
		final_language =  'ny'
	if translation_language == '18':
		final_language =  'zh-cn'
	if translation_language == '19':
		final_language =  'co'
	if translation_language == '20':
		final_language =  'hr'
	if translation_language == '21':
		final_language =  'zh-tw'
	if translation_language == '22':
		final_language =  'cs'
	if translation_language == '23':
		final_language =  'da'
	if translation_language == '24':
		final_language =  'nl'
	if translation_language == '25':
		final_language =  'eo'
	if translation_language == '26':
		final_language =  'et'
	if translation_language == '27':
		final_language =  'tl'
	if translation_language == '28':
		final_language =  'fi'
	if translation_language == '29':
		final_language =  'fy'
	if translation_language == '30':
		final_language =  'gl'
	if translation_language == '31':
		final_language =  'ka'
	if translation_language == '32':
		final_language =  'el'
	if translation_language == '33':
		final_language =  'gu'
	if translation_language == '34':
		final_language =  'ha'
	if translation_language == '35':
		final_language =  'haw'
	if translation_language == '36':
		final_language =  'ht'
	if translation_language == '37':
		final_language =  'iw'
	if translation_language == '38':
		final_language =  'hi'
	if translation_language == '39':
		final_language =  'hmn'
	if translation_language == '40':
		final_language =  'hu'
	if translation_language == '41':
		final_language =  'is'
	if translation_language == '42':
		final_language =  'ig'
	if translation_language == '43':
		final_language =  'id'
	if translation_language == '44':
		final_language =  'ga'
	if translation_language == '45':
		final_language =  'ja'
	if translation_language == '46':
		final_language =  'jw'
	if translation_language == '47':
		final_language =  'kn'
	if translation_language == '48':
		final_language =  'kk'
	if translation_language == '49':
		final_language =  'km'
	if translation_language == '50':
		final_language =  'ko'
	if translation_language == '51':
		final_language =  'ku'
	if translation_language == '52':
		final_language =  'ky'
	if translation_language == '53':
		final_language =  'lo'
	if translation_language == '54':
		final_language =  'la'
	if translation_language == '55':
		final_language =  'lv'
	if translation_language == '56':
		final_language =  'lt'
	if translation_language == '57':
		final_language =  'lb'
	if translation_language == '58':
		final_language =  'mk'
	if translation_language == '59':
		final_language =  'mg'
	if translation_language == '60':
		final_language =  'ms'
	if translation_language == '61':
		final_language =  'ml'
	if translation_language == '62':
		final_language =  'mt'
	if translation_language == '63':
		final_language =  'mi'
	if translation_language == '64':
		final_language =  'mr'
	if translation_language == '65':
		final_language =  'mn'
	if translation_language == '66':
		final_language =  'my'
	if translation_language == '67':
		final_language =  'ne'
	if translation_language == '68':
		final_language =  'no'
	if translation_language == '69':
		final_language =  'ps'
	if translation_language == '70':
		final_language =  'fa'
	if translation_language == '71':
		final_language =  'pl'
	if translation_language == '72':
		final_language =  'pt'
	if translation_language == '73':
		final_language =  'pa'
	if translation_language == '74':
		final_language =  'ro'
	if translation_language == '75':
		final_language =  'ru'
	if translation_language == '76':
		final_language =  'sm'
	if translation_language == '77':
		final_language =  'sr'
	if translation_language == '78':
		final_language =  'gd'
	if translation_language == '79':
		final_language =  'st'
	if translation_language == '80':
		final_language =  'sn'
	if translation_language == '81':
		final_language =  'sd'
	if translation_language == '82':
		final_language =  'si'
	if translation_language == '83':
		final_language =  'sk'
	if translation_language == '84':
		final_language =  'sl'
	if translation_language == '85':
		final_language =  'so'
	if translation_language == '86':
		final_language =  'es'
	if translation_language == '87':
		final_language =  'su'
	if translation_language == '88':
		final_language =  'sw'
	if translation_language == '89':
		final_language =  'sv'
	if translation_language == '90':
		final_language =  'tg'
	if translation_language == '91':
		final_language =  'ta'
	if translation_language == '92':
		final_language =  'te'
	if translation_language == '93':
		final_language =  'th'
	if translation_language == '94':
		final_language =  'tr'
	if translation_language == '95':
		final_language =  'uk'
	if translation_language == '96':
		final_language =  'ur'
	if translation_language == '97':
		final_language =  'uz'
	if translation_language == '98':
		final_language =  'vi'
	if translation_language == '99':
		final_language =  'cy'
	if translation_language == '100':
		final_language =  'xh'
	if translation_language == '101':
		final_language =  'yi'
	if translation_language == '102':
		final_language =  'yo'
	if translation_language == '103':
		final_language =  'zu'
	if translation_language == 'q':
		break

	# Initializing the Google translator API
	translator = Translator()

	print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
	# Translate the audi recording to the specified language
	translation = translator.translate(f"{text}", dest = final_language)

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
	question_more = input("Do you wish to translate another recording? [y/n]\n")
	if question_more == 'y':
		print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break
