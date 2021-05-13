[![Active Development](https://img.shields.io/badge/Maintenance%20Level-Actively%20Developed-brightgreen.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/sveneschlbeck/lingopy)
![GitHub language count](https://img.shields.io/github/languages/count/sveneschlbeck/lingopy?color=pink)
![GitHub top language](https://img.shields.io/github/languages/top/sveneschlbeck/lingopy?color=white)
![GitHub search hit counter](https://img.shields.io/github/search/sveneschlbeck/lingopy/goto?color=brown)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/sveneschlbeck/lingopy?color=azure)  
![GitHub repo size](https://img.shields.io/github/repo-size/sveneschlbeck/lingopy?color=orange)
![GitHub last commit](https://img.shields.io/github/last-commit/sveneschlbeck/lingopy)

# lingopy 

Welcome to lingopy, the quick and easy way to translate text or audio files into a foreign language. If you would like to transform a recording of a speech you gave into a different language or always wanted to translate a whole text file, then this project may help you out!

## Translator types

- `translator.py` -> convert texts or messages by just typing them into the terminal window

```console
(translate_env) C:/Users/user_name/dir python translator.py
. . .
. . .
. . .
Hello! Welcome to the simple instant translator...

Enter 'q' to quit.

-----------------------------------------------------------------------------------------------------------------------------

Please type in the text/ message you would like to translate.
Your entry should look like this: 'This is an example message.' but without quotes.
I would like to translate this text.

-----------------------------------------------------------------------------------------------------------------------------

Please specify the language you wish to translate to.

Press '1' for French.                   Press '2' for German.                   Press '3' for Italian.
Press '4' for Afrikaans.                Press '5' for Albanian.                 Press '6' for Amharic.
Press '7' for Arabic.                   Press '8' for Armenian.                 Press '9' for Azerbaijani.
Press '10' for Basque.                  Press '11' for Belarusian.              Press '12' for Bengali.
Press '13' for Bosnian.                 Press '14' for Bulgarian.               Press '15' for Catalan.
Press '16' for Cebuano.                 Press '17' for Chichewa.                Press '18' for Chinese (Han Yu).
Press '19' for Corsican.                Press '20' for Croatian.                Press '21' for Chinese (traditional).
Press '22' for Czech.                   Press '23' for Danish.                  Press '24' for Dutch.
Press '25' for Esperanto.               Press '26' for Estonian.                Press '27' for Filipino.
Press '28' for Finnish.                 Press '29' for Frisian.                 Press '30' for Galician.
Press '31' for Georgian.                Press '32' for Greek.                   Press '33' for Gujarati.
Press '34' for Hausa.                   Press '35' for Hawaiian.                Press '36' for Haitian creole.
Press '37' for Hebrew.                  Press '38' for Hindi.                   Press '39' for Hmong.
Press '40' for Hungarian.               Press '41' for Icelandic.               Press '42' for Igbo.
Press '43' for Indonesian.              Press '44' for Irish.                   Press '45' for Japanese.
Press '46' for Javanese.                Press '47' for Kannada.                 Press '48' for Kazakh.
Press '49' for Khmer.                   Press '50' for Korean.                  Press '51' for Kurdish (Kurmanji).
Press '52' for Kyrgyz.                  Press '53' for Lao.                     Press '54' for Latin.
Press '55' for Latvian.                 Press '56' for Lithuanian.              Press '57' for Luxembourgish.
Press '58' for Macedonian.              Press '59' for Malagasy.                Press '60' for Malay.
Press '61' for Malayalam.               Press '62' for Maltese.                 Press '63' for Maori.
Press '64' for Marathi.                 Press '65' for Mongolian.               Press '66' for Myanmar (Burmese).
Press '67' for Nepali.                  Press '68' for Norwegian.               Press '69' for Pashto.
Press '70' for Persian.                 Press '71' for Polish.                  Press '72' for Portuguese.
Press '73' for Punjabi.                 Press '74' for Romanian.                Press '75' for Russian.
Press '76' for Samoan.                  Press '77' for Serbian.                 Press '78' for Scots gaelic.
Press '79' for Sesotho.                 Press '80' for Shona.                   Press '81' for Sindhi.
Press '82' for Sinhala.                 Press '83' for Slovak.                  Press '84' for Slovenian.
Press '85' for Somali.                  Press '86' for Spanish.                 Press '87' for Sundanese.
Press '88' for Swahili.                 Press '89' for Swedish.                 Press '90' for Tajik.
Press '91' for Tamil.                   Press '92' for Telugu.                  Press '93' for Thai.
Press '94' for Turkish.                 Press '95' for Ukrainian.               Press '96' for Urdu.
Press '97' for Uzbek.                   Press '98' for Vietnamese.              Press '99' for Welsh.
Press '100' for Xhosa.                  Press '101' for Yiddish.                Press '102' for Yoruba.
Press '103' for Zulu.

Leave blank for default (English).
2

-----------------------------------------------------------------------------------------------------------------------------

Original text:

I would like to translate this text.

Original language: en

=============================================================================================================================
Translating...
=============================================================================================================================

New text: Ich möchte diesen Text übersetzen.

New language: de
. . .
. . .
. . .
```

- `text_file_translator.py` -> choose a text file stored on your device to translate it

```console
(translate_env) C:/Users/user_name/dir python text_file_translator.py
. . .
. . .
. . .
Hello! Welcome to the simple translator for written words...

Enter 'q' to quit.

-----------------------------------------------------------------------------------------------------------------------------

Please specify the full path to the folder including the file name.
Your entry should look like this: 'C:/User/.../example.txt' but without quotes.
C:/Users/user_name/Documents/blabla.txt
. . .
. . .
. . .
```

- `spoken_word_translator.py` -> translate speeches recorded with your microphone into a foreign language

```console
(translate_env) C:/Users/user_name/dir python spoken_word_translator.py
. . .
. . .
. . .
Hello! Welcome to the simple translator for spoken words...

Enter 'q' to quit.

-----------------------------------------------------------------------------------------------------------------------------

Please specify the spoken language.

Press '1' for French.                   Press '2' for German.                   Press '3' for Italian.
Press '4' for Russian.                  Press '5' for Dutch.                    Press '6' for Mandarin (Han Yu).
Press '7' for Spanish.                  Press '8' for Turkish.                  Press '9' for Swedish.
Press '10' for Portuguese.              Press '11' for Japanese.                Press '12' for Korean.
Press '13' for Polish.                  Press '14' for Czech.                   Press '15' for Finnish.
Press '16' for Hebrew.                  Press '17' for Hungarian.               Press '18' for Indonesian.
Press '19' for Malaysian.               Press '20' for Norwegian.               Press '21' for Romanian.
Press '22' for Serbian.                 Press '23' for Slovak.                  Press '24' for Afrikaans.

Leave blank for default (English).
2

-----------------------------------------------------------------------------------------------------------------------------

How long do you plan to speak?

Define a time span.
Press '1' for 30 seconds.
Press '2' for 60 seconds.
Press '3' for 90 seconds.
Press '4' for 120 seconds.
Press '5' for 300 seconds.

Leave blank for default (10 seconds).

-----------------------------------------------------------------------------------------------------------------------------

Speak now!

-----------------------------------------------------------------------------------------------------------------------------

Recognizing voice...

/

-----------------------------------------------------------------------------------------------------------------------------

Record:

hallo dies ist ein Test ich teste ob dieses Programm funktioniert

-----------------------------------------------------------------------------------------------------------------------------

Do you want to save the original audio you just recorded to a text file? [y/n]
n
. . .
. . .
. . .
```

## Project compatibility & Expansion

If you would like to translate audio books, YouTube videos or Zoom meetings, check out my project `A2T_converter` to first transcribe them into text files. These text files can then be translated by the software provided in this repository.  
The same approach is required if you want your translations to be read out loudly. Translate them using this project and then use the `text_2_speech.py` module from the repository `A2T_converter` (https://github.com/sveneschlbeck/A2T_converter).

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

Note: If your terminal output is not showing all unicode symbols (e.g. Arabic letters or Chinese signs), choose a different font for the terminal, I recommend `SimSun-ExtB`.

## Controls

The program is very intuitive. Just follow the command line instructions and you'll be fine.  
To quit the program at any time, press <kbd>Q</kbd> whenever a question is asked or click on the red 'X' in the upper right terminal window corner.  
If asked a question, reply by either pressing <kbd>Y</kbd> for 'yes', <kbd>N</kbd> for 'no', or <kbd>Q</kbd> to quit the program.  
To confirm the given answer, press <kbd>&#9166;</kbd>.  

## Hardware & Software Requirements

This program can be run without much computing power. It can be executed on any modern device using Microsoft's Windows operating system. Other OS may work but are not specifically supported.  
lingopy is written in python and currently only available in the form of multiple python modules. Therefore, you need to download python in order to execute the program files (`.py` files). The required storage capacity depends on the user's behavior. It can range from a few KB when only translating short text files to multiple MB/GB when translating books or webpages.  
After downloading and storing this repository, open a python terminal window, navigate to the repository directory and type e.g. `translator.py`. As soon as you hit <kbd>&#9166;</kbd>, the program will start.

## Software dependencies

All required libraries, packages or frameworks can be seen in the `environment.yaml` file. They need to be installed on your machine (Anaconda environment recommended) in order to execute all programs correctly.  
If you already created a conda environment that you would like to use, you can update it anytime by first activating the environment and then running the `conda env update` command.

```python
conda activate myenv
```

```python
conda env update --name myenv --file environment.yaml
```


Note that this command will only `update` the conda environment. It will no remove already installed packages, especially if they have been installed using `pip install`.  

You can also build a conda environment from a `.yaml` file. In order to do this, type in the following command.

```python
conda env create --name myenv --f environment.yaml
```

## Code Documentation

The documentation for this project can be found under `docs/build/html/index.html`. Navigate to the file on your local machine and open it in a web browser.

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

## Contact

You have questions about the project or want to report a bug or feedback in general?  
Open a new issue or contact me directly via sven.eschlbeck@t-online.de
