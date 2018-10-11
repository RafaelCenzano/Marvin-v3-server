import sys # system to get input variable/data form other script
import pyttsx3 # run pyttsx3

##############################################################
# File to speak with pyttsx3 and have no errors in threading #
##############################################################

def init_engine(): # initialize engine function
    engine = pyttsx3.init() # initialize engine
    return engine  # return initialized engine

def say(s): # function to speak with engine
    engine.say(s) # que tts data
    engine.runAndWait() # speak text

engine = init_engine() # create engine
say(str(sys.argv[1])) # speak