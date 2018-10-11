# Imports
from os import path, remove # import os
from gtts import gTTS # gtts for text to speech
from platform import system # find os type
from playsound import playsound # play sounds for windows gtts
from subprocess import Popen, PIPE, call # subprocess for playing audio
from marvin.network import checkConnection # check internet
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError # speech_recognition to turn speech to string


################################
# File for essential functions #
################################


def speak(spokenString, voice):
    python_path = path.join('marvin-env','bin','python3') # Format Paths
    speak_path = path.join('marvin','called_files','pyttsx3_speak.py') # Format Paths
    print(spokenString) # string to speak
    if voice == 'female' and checkConnection() == True:
        if path.isfile("Speak.mp3"):
            remove("Speak.mp3")
        tts = gTTS(text = spokenString, lang = 'en-uk') # create string into mp3 file using gtts
        tts.save('Speak.mp3') # save gtts audio as Speak.mp3
        if system() == 'Windows':
            playsound('Speak.mp3')
        else:
            proc = Popen(['mpg321 Speak.mp3'], stdout = PIPE, stderr = PIPE, shell = True) # Popen command with terminal command arguments
            (out, err) = proc.communicate() # opening speak file
    elif voice == 'male':
        call([python_path, speak_path, spokenString])
    else:
        print('No internet connection using offline speak')
        call([python_path, speak_path, spokenString])

def listen():
    r = Recognizer() # less writing
    with Microphone() as source: # using microphone to detect audio
        r.adjust_for_ambient_noise(source, duration = 0.5) #adjust for ambiet sounds for 1 second
        audio = r.listen(source) # listen for audio
    data = '' # set data ad nothing
    try: # in case of errors
        data = r.recognize_google(audio) # recognize with google's speech recognition
        print('You said: ' + data) # write what was heard
    except UnknownValueError: # unknown audio
        print('I didn\'t get that') # when google api didn't understand audio
        data = 'None' # return none
    except RequestError as e: # request error
        print('Api or connection is not working.\n The error is {0}'.format(e)) # when connection or Api offline
        data = 'Broken' # return broken
    return data # return recognized audio as string

def commandInput(type_of_input):
    if type_of_input == 1: # 1 for listening
        input_to_return = listen() # listen
        return input_to_return # return recognized audio as string
    if type_of_input == 0: # 0 for type input
        input_to_return = input('') # get input
        return input_to_return # return text input

def splitJoin(command, how_many):
    split_command = command.split(" ")[how_many:] # split for anything after any unnecessary words
    joined_command = (" ").join(split_command) # joining anything that was split from after any unnecessary words
    return joined_command # return rejoined command