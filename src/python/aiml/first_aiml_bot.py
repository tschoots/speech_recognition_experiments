# url used for this
# https://www.devdungeon.com/content/ai-chat-bot-python-aiml

# more info here
# https://www.chatbots.org/chatbot/a.l.i.c.e/
# https://github.com/FunRobots/VUI/wiki/AIML--Documentation-and-Tutorials
# https://github.com/pandorabots/Free-AIML
# https://github.com/pandorabots/rosie

# documentation i could find
# https://docs.google.com/document/d/1wNT25hJRyupcG51aO89UcQEiG-HkXRXusukADpFnDs4/pub
# http://callmom.pandorabots.com/static/reference/
# https://code.google.com/archive/p/aiml-en-us-pandorabots-callmom/wikis/CallMomOOBTags.wiki

# golang datascience libraries , move this to the appropriate spot
# https://github.com/gopherdata/resources/blob/master/tooling/README.md#nlp

# conference in Switserland
# http://www.aiml2018.unibe.ch/
# http://www.aiml2018.unibe.ch/AiML2018_accepted_papers.html

import aiml
import os

sessionId = 12345

# Create the kernel and learn AIML files
kernel = aiml.Kernel()

# Get session info as dictionary.
# Contains the input and output history as well as any predicates known
sessionData = kernel.getSessionData(sessionId)

# Each session ID needs to be a unique value
# The predicate name is the name of something/someone that the bot knows
# about in your session with the bot
# The bot might know you as "Billy" and that your "dog" is named "Brandy"
kernel.setPredicate("dog", "Brandy", sessionId)
clients_dogs_name = kernel.getPredicate("dog", sessionId)

kernel.setBotPredicate("hometown", "127.0.0.1")
bot_hometown = kernel.getBotPredicate("hometown")


# use brain files to speed up learning
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
    kernel.saveBrain("bot_brain.brn")


# kernel.learn("std-startup.xml")
# kernel.respond("LOAD AIML B")

# Press CTRL-C to break this loop
while True:
    message = input("Enter your message to the bot: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message, sessionId)
        print(bot_response)


    #print (kernel.respond(input("Enter your message >> ")))
