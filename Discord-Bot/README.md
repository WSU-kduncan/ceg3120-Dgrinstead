Setup
1. First thing you want to go is go into the Discord Developer Portal and you want to hit
create application. This can be a bot for what exactly what we were doing this is a bot.
2. You have to but the key/token in a file that is called .env and you have to make sure 
thank once your key is added in the .env file you have to make sure to add this file to something called a .gitignore file because you dont want to publish this key
to the discord servers to ensure you are the only one that has access to this.
3.You need to import discord, import python, import os and a few other things also you
might have to install git, pip, python 3.8 if you are not on pyton 3.8 yet.

Usage
1. With my changes in the code instead of using token! ann you have to use is hello! and 
the bot is going to return the different quotes that I have listed there. It is going to return " Security used 
to be an inconvenience sometimes, but now its a necessity all of the time.
" Technology trust is a good thing, but control is a better one".
"If security were all that mattered, computer would never be turned on, let alone hooked into a network 
literally millions of potential intruders"

Research
1. After doing some research the way to keep your discord bot running is you have to keep
your Repl running. Repl. it will keep code running after you close the browser tab only
if you are running a web server. you have to run the Flask framework. You have to create
a new file called keep_alive.py and type this.

from flask import Flask
from threading import Thread


app = Flask('')

@app.route('/')

def home():
	return "i'm alive"

def run():
   app.run(host='0.0.0.0',port=8080)

def keep_alive(): 
    t = Thread(target=run)
    t.start()
    
    
    
    
    
    
    
    
    This is my screenshot of the code working
    
    
    
![image](https://user-images.githubusercontent.com/59849834/134444864-19edc1a1-b356-4392-afa5-283a1bba9ec7.png)
