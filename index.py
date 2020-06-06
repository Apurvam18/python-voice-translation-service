import flask
from flask import request
import requests
import speech_recognition as spr 
from googletrans import Translator 
from gtts import gTTS 
import os 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/hello', methods=['GET'])
def home():
    return "<h1>Apurva's Hello page</h1>"

def translateText(fileContent):
	translator = Translator() 
	from_lang = 'en' 
	to_lang = 'hi'
	#file1 = open("apurva-english.txt","r+")  
	#data = file1.read()
	result = translator.translate(fileContent,src= 'en',  dest= 'hi') 
	
	speak = gTTS(text=result.text, lang=to_lang, slow= False)  
	  
	print("saving comverted text to mp3 file")
	speak.save("captured_voice.mp3")      
	print("opening the saved mp3 file")
	
	os.system("start captured_voice.mp3") 


@app.route('/translation', methods=['GET'])
def translation():
	"<h1>Translation Page</h1>"
	fileContent = request.args.get('fileContent')
	translateText(fileContent);
	return "File Content translated"


app.run()