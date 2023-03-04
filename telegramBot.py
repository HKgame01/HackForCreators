import openai
openai.api_key = "API"

import telebot

API_KEY = "API"
finalText = ""

bot = telebot.TeleBot(API_KEY)
print("Bot is up and running!")
@bot.message_handler(commands=['start'])
def greet(message):
  bot.send_message(message.chat.id, "Hello, Welcome to the creAIte.Please write /help to see the commands available.")

@bot.message_handler(commands=['help'])
def hello(message):
  bot.send_message(message.chat.id, """To start with, Tell us your idea :-
`i wanna make video on (your idea)` 
/title - Get the appropiate Title
/description - Get the appropiate Description
/tags - Get the appropiate Tags

/idea - In case you do not have any ideo on what video to make, get it from us
/communitypost - If you want to post for community in community section get it from us

/script - To get a script on the video
	"""
  
)


@bot.message_handler(commands=['about'])
def greet(message):
  bot.send_message(message.chat.id, "This bot is made for Hack For Creators")

def content_request(message):
  request = message.text.split()
  if len(request) < 6 or request[0].lower() not in "i wanna make video on":
    return False
  else:
    return True

@bot.message_handler(func=content_request)
def send_link(message):
    query = message.text.split()[5:]
    
    outputText = ""
    for i in query:
        outputText = outputText+i+" "
    outputText.strip()

    comp = openai.Completion.create(engine = "text-davinci-003", prompt=f'tell me a good youtube title, desciption, tags for "{outputText}"', max_tokens=1000)
    finalTextL = comp.choices[0]["text"]
    global finalText
    finalText = finalTextL
    finalText = finalText.split("\n")
    bot.send_message(message.chat.id, f"Okay got it\nNow you can use\n/title - Get the appropiate Title\n/description - Get the appropiate Description\n/tags - Get the appropiate Tags")


@bot.message_handler(commands=['title'])
def greet(message):
    title = ""
    for i in finalText:
        if i.startswith("Title"):
            title = i
            break
    bot.send_message(message.chat.id, f"For your idea the most appropriate title according to us is:\n{title}")

@bot.message_handler(commands=['description'])
def greet(message):
    description = ""
    for i in finalText:
        if i.startswith("Description"):
            description = i
            break
    bot.send_message(message.chat.id, f"For your idea the most appropriate description according to us is:\n{description}")

@bot.message_handler(commands=['tags'])
def greet(message):
    tags = ""
    for i in finalText:
        if i.startswith("Tags"):
            tags = i
            break
    bot.send_message(message.chat.id, f"For your idea the most appropriate tags according to us is:\n{tags}")

@bot.message_handler(commands=['idea'])
def greet(message):
    rawidea = openai.Completion.create(engine = "text-davinci-003", prompt=f'tell me a good youtube video idea"', max_tokens=1000)
    idea = rawidea.choices[0]["text"]
    bot.send_message(message.chat.id, f"The best idea for your Youtube Channel after reviewing your content is\n{idea}")

@bot.message_handler(commands=['communitypost'])
def greet(message):
    rawcomm = openai.Completion.create(engine = "text-davinci-003", prompt=f'tell me a good youtube community post for the channel"', max_tokens=1000)
    comm = rawcomm.choices[0]["text"]
    bot.send_message(message.chat.id, f"The best idea for your Youtube Channel after reviewing your content is\n`{comm}`")

def scr_request(message):
  request = message.text.split()
  if len(request) < 6 or request[0].lower() not in "i want a script on":
    return False
  else:
    return True

@bot.message_handler(func=scr_request)
def send_link(message):
    query = message.text.split()[5:]
    
    outputText = ""
    for i in query:
        outputText = outputText+i+" "
    outputText=outputText.strip()

    scr_waw = openai.Completion.create(engine = "text-davinci-003", prompt=f'write a script on "{outputText}"', max_tokens=1000)
    script = scr_waw.choices[0]["text"]

    bot.send_message(message.chat.id, f"Here you go:\n{script}")
bot.polling()
