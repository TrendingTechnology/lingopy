[![Active Development](https://img.shields.io/badge/Maintenance%20Level-Actively%20Developed-brightgreen.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/sveneschlbeck/lingopy)
![GitHub language count](https://img.shields.io/github/languages/count/sveneschlbeck/lingopy?color=pink)
![GitHub top language](https://img.shields.io/github/languages/top/sveneschlbeck/lingopy?color=white)
![GitHub search hit counter](https://img.shields.io/github/search/sveneschlbeck/lingopy/goto?color=brown)


# LINGOPY 

Welcome to lingopy, the quick and easy way to translate text or audio files into a foreign language. If you would like to transform a recording of a speech you gave into a different language or always wanted to translate a whole text file, then this project may help you out!

## Translator types

- terminal input -> convert texts or messages by just typing them into the terminal window
- text files -> choose a text file stored on your device to translate it
- self recorded speeches -> translate speeches recorded with your microphone into a foreign language

## Project compatibility & Expansion

If you would like to translate audio books, YouTube videos or Zoom meetings, check out my project 'A2T_converter' to first transcribe them into text files. These text files can then be translated by the software provided in this repository.  
The same approach is required if you want your translations to be read out loudly. Translate them using this project and then use the 'text_2_speech' module from the repository 'A2T_converter'.

## Languages
  
Note that the software is only applicable to supported languages. Translating unsopported languages with this API can cause wrong and unintentional translations.  

Currently supported languages include:  
- English
- French
- German
- Italian
- Afrikaans
- Albanian
- Amharic
- Arabic
- Armenian
- Azerbaijani
- Basque
- Belarusian
- Bengali
- Bosnian
- Bulgarian
- Catalan
- Cebuano
- Chichewa
- Chinese (Han Yu)
- Corsican
- Croatian
- Chinese (traditional)
- Czech
- Danish
- Dutch
- Esperanto
- Estonian
- Filipino
- Finnish
- Frisian
- Galician
- Georgian
- Greek
- Gujarati
- Hausa
- Hawaiian
- Haitian creole
- Hebrew
- Hindi
- Hmong
- Hungarian
- Icelandic
- Igbo
- Indonesian
- Irish
- Japanese
- Javanese
- Kannada
- Kazakh
- Khmer
- Korean
- Kurdish (Kurmanji)
- Kyrgyz
- Lao
- Latin
- Latvian
- Lithuanian
- Luxembourgish
- Macedonian
- Malagasy
- Malay
- Malayalam
- Maltese
- Maori
- Marathi
- Mongolian
- Myanmar (Burmese)
- Nepali
- Norwegian
- Pashto
- Persian
- Polish
- Portuguese
- Samoan
- Serbian
- Scots gaelic
- Sesotho
- Shona
- Sindhi
- Sinhala
- Slovak
- Slovenian
- Somali
- Spanish
- Sundanese
- Swahili
- Swedish
- Tajik
- Tamil
- Telugu
- Thai
- Turkish
- Ukrainian
- Urdu
- Uzbek
- Vietnamese
- Welsh
- Xhosa
- Yiddish
- Yoruba
- Zulu

Note: If your terminal output is not showing all unicode symbols (e.g. Arabic letters or Chinese signs), choose a different font for the terminal, I recommend 'SimSun-ExtB'.

## Controls

The program is very intuitive. Just follow the command line instructions and you'll be fine.  
To quit the program at any time, press <kbd>Q</kbd> whenever a question is asked or click on the red 'X' in the upper right terminal window corner.  
If asked a question, reply by either pressing <kbd>Y</kbd> for 'yes', <kbd>N</kbd> for 'no', or <kbd>Q</kbd> to quit the program.  
To confirm the given answer, press <kbd>&#9166;</kbd>.  

## Hardware & Software Requirements

This program can be run without much computing power. It can be executed on any modern device using Microsoft's Windows operating system. Other OS may work but are not specifically supported.  
lingopy is written in python and currently only available in the form of multiple python modules. Therefore, you need to download python in order to execute the program files (.py files). The required storage capacity depends on the user's behavior. It can range from a few KB when only translating short text files to multiple MB/GB when translating books or webpages.  
After downloading and storing this repository, open a python terminal window, navigate to the repository directory and type e.g. 'translator.py'. As soon as you hit <kbd>&#9166;</kbd>, the program will start.

## Software dependencies

All required libraries, packages or frameworks can be seen in the environment.yaml file. They need to be installed on your machine (Anaconda environment recommended) in order to execute all programs correctly.

## Code Documentation

The documentation for this project can be found under 'docs/build/html/index.html'. Navigate to the file on your local machine and open it in a web browser.

## Repository structure

All directories and files in this repository serve a distinct purpose, e.g. containing meta data. Deleting one or more of these directories or files in them can cause programs to throw errors and to stop working. So, don't delete meta data!  
Since most temporary data only exist for a short time and are required for few internal operations, they are overwritten in each program cycle, meaning that no additional storage space is required on your device.

## Resources & Links

https://www.python.org/ (Python)  
https://www.anaconda.com/ (Anaconda)  
https://pytube.io/en/latest/ (Pytube)  
https://github.com/jiaaro/pydub (Pydub)  
https://pypi.org/project/SpeechRecognition/ (SpeechRecognition)  
https://cloud.google.com/speech-to-text (Google Cloud Speech-to-Text API)  
https://www.sphinx-doc.org/en/master/# (Sphinx)  
https://readthedocs.org/ (Read the Docs)  
https://pypi.org/project/googletrans/ (Google Translator API)  
https://docs.python.org/3/library/time.html (Python time library)  
https://docs.python.org/3/library/pprint.html (Pprint)  

## Contribute to this repository

I am open to new ideas and inspiration. If you are interested in this project and want to contribute or cooperate, write me an e-mail with your GitHub name and the reason for your interest. Following a check, your request will be granted or rejected.

## Contact

You have questions about the project or want to report a bug or feedback in general?  
Contact me via sven.eschlbeck@t-online.de
