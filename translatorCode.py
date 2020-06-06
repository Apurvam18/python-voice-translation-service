import speech_recognition as spr 
from googletrans import Translator 
from gtts import gTTS 
import os 

def translateText():
	translator = Translator() 
	from_lang = 'en' 
	to_lang = 'hi'
	file1 = open("apurva-english.txt","r+")  
	data = file1.read()
	result = translator.translate(data,src= 'en',  dest= 'hi') 
	
	speak = gTTS(text=result.text, lang=to_lang, slow= False)  
	  
	print("saving comverted text to mp3 file")
	speak.save("captured_voice.mp3")      
	print("opening the saved mp3 file")
	
	os.system("start captured_voice.mp3") 