#Imports
from os import system, path # run terminal commands and find files in path
from json import load, dump # import json load
from difflib import get_close_matches # import close matches functions
from datetime import datetime # import datetime to show date and time
from threading import Thread # import threading to run more than one job at a time
from webbrowser import open as webopen # webbrowser to open websites
from marvin.api import ApiService # classes to handle api work
from marvin.misc import openCalculator, openStopwatch # functions to open Gui
from marvin.timer import TimerService # functions to run a threaded timer
from marvin.webscrape import TomatoeScrape, YoutubeScrape, DefinitionFind # import webscrape functions
from marvin.send_email import Email, EmailService # import email classes
from marvin.essentials import speak, commandInput, splitJoin # import speak and listen
import random
import marvin.asciiart


#####################
# File for commands #
#####################


command_list = ['open reddit', 'open subreddit', 'define', 'what is the definition of','google','where is','amazon','open google docs','open google sheets',
                    'time in','rotten tomatoes','imdb','imdb rating','youtube','search youtube','standby','exit','quit','leave','close','relog','logout','ls',
                    'dir','contacts','contact list','remove contact','delete contact','add contact','new contact','send email','roll a die','shut down','shutdown'
                    'what time is it','current time','what is the date','what\'s the date','current date','date today','d6','6 sided die','set a timer for'
                    'day of the week','week number','open calculator','run calculator','calculator','open stopwatch','run stopwatch','stopwatch','roll a d6',
                    'roll a 6 sided die','dice','what dice can I roll','flip coin','flip a coin','open twitter','open facebook','open github'
                ]


#COMMANDS

class MarvinCommands(Exception): pass # class to choose different input type
class MarvinRelog(Exception): pass # class to restart main loop to login
def dataCommands(command, type_of_input, pass_path, contact_path, correction_path, os_type, speak_type):

    bob = False

    # Website Commands #

    if 'open reddit' in command or 'open subreddit' in command:
        subreddit = splitJoin(command, 2) # function to split and rejoin command
        speak('Opening subreddit ' + subreddit + ' for you', speak_type) # saying the subreddit page
        webopen('https://www.reddit.com/r/' + subreddit, new = 2) # open url in browser
        print('Done!')

    elif 'open google sheets' == command:
        speak('Opening Google Sheets for you', speak_type) # saying what it will open twitter
        webopen('https://docs.google.com/spreadsheets/u/0/', new = 2) # open url in browser
        print('Done!')
        
    elif 'open google docs' == command:
        speak('Opening Google Docs for you', speak_type) # saying what it will open twitter
        webopen('https://docs.google.com/document/u/0/', new = 2) # open url in browser
        print('Done!')
        
    elif 'google' in command:
        gsearch = splitJoin(command, 1) # function to split and rejoin command
        speak('Opening Google search for ' + gsearch, speak_type) # saying what it will open
        url = ('https://www.google.com/search?q=' + gsearch + '&rlz=1C5CHFA_enUS770US770&oq=' + gsearch + '&aqs=chrome..69i57.1173j0j8&sourceid=chrome&ie=UTF-8') # url with search
        webopen(url, new = 2) # open url in browser
        print('Done!')

    elif 'open twitter' == command:
        speak('Opening Twitter for you', speak_type) # saying what it will open twitter
        webopen('https://twitter.com/', new = 2) # open url in browser
        print('Done!')
        
    elif 'open facebook' == command:
        speak('Opening Facebook for you', speak_type) # saying what it will open twitter
        webopen('https://www.facebook.com/', new = 2) # open url in browser
        print('Done!')
        
    elif 'open github' == command:
        speak('Opening Github for you', speak_type) # saying what it will open twitter
        webopen('https://github.com/', new = 2) # open url in browser
        print('Done!')
        
    elif 'open stack overflow' == command:
        speak('Opening Stack Overflow for you', speak_type) # saying what it will open twitter
        webopen('https://stackoverflow.com/', new = 2) # open url in browser
        print('Done!')
        
    elif 'where is' in command:
        location = splitJoin(command, 2) # function to split and rejoin command
        speak('Hold on, I will show you where ' + location + ' is.', speak_type) # saying the location heard
        url = ('https://www.google.nl/maps/place/' + location + '/&amp;') # url with location
        webopen(url, new = 2) # open url in browser
        print('Done!')

    elif 'amazon' in command:
        amazon = splitJoin(command, 1) # function to split and rejoin command
        speak('Searching amazon for ' + amazon, speak_type) # saying what it will look for
        url = ('https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + amazon) # url with amazon search
        webopen(url, new = 2) # open in browser
        print('Done!')

    elif 'time in' in command:
        time_in = splitJoin(command, 1) # function to split and rejoin command
        speak('Showing time in '+ time_in, speak_type) # saying what its opening
        url = ('https://time.is/' + time_in) # url to time.is with the location
        webopen(url, new = 2) # open in browser
        print('Done!')

    # Marvin Webscrape Commands #

    elif 'rotten tomatoes' in command:
        TomatoeScrape = TomatoeScrape(speak_type, command, 1)
        TomatoeScrape.scrapeRottentomatoes()

    elif 'imdb' in command:
        if 'imdb rating' in command:
            num_type = 2
        elif 'imdb' in command:
            num_type = 1
        TomatoeScrape = TomatoeScrape(speak_type, command, num_type)
        TomatoeScrape.IMDb()

    elif 'youtube' in command:
        if 'search youtube' in command:
            num_type = 2
        elif 'play in youtube' in commands:
            num_type = 3
        elif 'youtube' in command:
            num_type = 1
        Youtube_Scrape = YoutubeScrape(speak_type, command, num_type)
        Youtube_Scrape.scrapeYoutube() # function to scrape urls

    elif 'define' in command or 'what is the definition of' in command:
        if 'what is the definition of' in command:
            num_type = 5
        elif 'define' in command:
            num_type = 1
        Definition_Find = DefinitionFind(speak_type, command, num_type)
        Definition_Find.scrapeDefinition() # function to scrape urls

    # Marvin Api Commands #

    elif 'full random taco' == command:
        Api_Service = ApiService(speak_type)
        Api_Service.tacoFullRand()
        Api_Service.dataTaco()

    elif 'random taco' == command:
        Api_Service = ApiService(speak_type)
        Api_Service.tacoFullRand()
        Api_Service.dataTaco()

    # Marvin Function Commands #

    elif 'standby' in command:
        speak('Going on standby', speak_type)
        raise MarvinCommands # raise exeption so class passes and restarts loop

    elif command == 'exit' or command == 'quit' or command == 'leave' or command == 'close' or command == 'shutdown' or command == 'shut down':
        speak('Shutting down', speak_type)
        exit() # leave program

    elif command == 'relog' or command == 'logout':
        speak('logging out', speak_type)
        raise MarvinRelog

    elif command == 'ls' or command == 'dir':
        if os_type == 'Linux':
            system('ls')
        elif os_type == 'Darwin':
            system('ls')
        elif os_type == 'Windows':
            system('dir')

    # Sending based Commands

    elif command == 'contact list' or command == 'contacts':
        ContactService = marvin.contacts.ContactShow(contact_path, 0, speak_type)
        ContactService.contactList()

    elif command == 'delete contact' or command == 'remove contact':
        try:
            ContactService = marvin.contacts.ContactShow(contact_path, 1, speak_type)
            ContactService.contactList()
            print('input cancel to cancel delete contact') # cancel message
            speak('Who would you like to delete from your contacts?', speak_type)
            delete_contact = commandInput(type_of_input).lower() # function for listen or raw_input
            if 'quit' == delete_contact.lower() or 'exit' == delete_contact.lower() or 'cancel' == delete_contact.lower(): raise ValueError # check message for cancel
            with open(contact_path, 'r') as contact_del_list:
                del_contact_data = load(contact_del_list)
            if delete_contact.lower() not in del_contact_data['contacts']: 
                print('User does not exist')
                raise ValueError
            del del_contact_data['contacts'][delete_contact]
            with open(contact_path, 'w') as outfile:
                dump(del_contact_data, outfile)
            speak(delete_contact + ' has been removed', speak_type)
        except Exception as e:
            print('Cancelling')

    elif command == 'add contact' or command == 'new contact':
        try:
            ContactService = marvin.contacts.ContactShow(contact_path, 1, speak_type)
            ContactService.contactList()
            print('input cancel to cancel add contact') # cancel message
            speak('Who would you like to add to you contacts?', speak_type)
            print('First name please')
            add_contact = commandInput(type_of_input) # function for listen or raw_input
            if 'quit' == add_contact.lower() or 'exit' == add_contact.lower() or'cancel' == add_contact.lower(): raise ValueError # check message for cancel
            print('input cancel to cancel add contact') # cancel message
            speak('What is ' + add_contact + '\'s email?', speak_type)
            new_email = commandInput(type_of_input) # function for listen or raw_input
            if 'quit' == new_email.lower() or 'exit' == new_email.lower() or 'cancel' == new_email.lower(): raise ValueError # check message for cancel
            print('input cancel to cancel add contact') # cancel message
            speak('What is ' + add_contact + '\'s phone number? If you don\'t have it or you dont want to input respond with None', speak_type)
            new_phone_number = commandInput(type_of_input) # function for listen or raw_input
            if 'quit' == new_phone_number.lower() or 'exit' == new_phone_number.lower() or 'cancel' == new_phone_number.lower(): raise ValueError # check message for cancel
            speak('Does this contact have a nickname you like to add? If they don\'t have one type none', speak_type)
            nick = commandInput(type_of_input) # function for listen or raw_input
            nick_lower = nick.lower()
            if 'quit' == nick_lower or 'exit' == nick_lower or 'cancel' == nick_lower: raise ValueError # check message for cancel
            with open(contact_path, 'r') as contact_data:
                new_contact_data = load(contact_data) # read data
            add_contact_lowered = add_contact.lower()
            if 'none' != nick_lower:
                new_contact_data['nicks'][nick_lower] = {"real_name":add_contact_lowered}
            speak('Creating contact', speak_type)
            with open(contact_path, 'w') as outfile:
                new_contact_data['contacts'][add_contact_lowered] = {"email":new_email, "number":new_phone_number} # new data to add
                dump(new_contact_data, outfile) # add data
            print('Contact Created!')
        except Exception as e:
            print('Cancelling')

    elif command == 'send email':
        try:
            ContactService = marvin.contacts.ContactShow(contact_path, 'email', speak_type)
            ContactService.contactList()
            print('input cancel to cancel send email') # cancel message
            speak('Who would you like to send this email to?', speak_type)
            email_recipient = commandInput(type_of_input).lower() # function for listen or raw_input
            if 'quit' == email_recipient.lower() or 'exit' == email_recipient.lower() or 'cancel' == email_recipient.lower(): raise ValueError # check message for cancel
            print('input cancel to cancel send email') # cancel message
            speak('What is the subject of the email?', speak_type)
            email_subject = commandInput(type_of_input) # function for listen or raw_input
            if 'quit' == email_subject.lower() or 'exit' == email_subject.lower() or 'cancel' == email_subject.lower(): raise ValueError # check message for cancel
            print('input cancel to cancel send email') # cancel message
            speak('What is the message you would like to send to ' + email_recipient, speak_type)
            email_body = commandInput(type_of_input) # function for listen or raw_input
            if 'quit' == email_body.lower() or 'exit' == email_body.lower() or 'cancel' == email_body.lower(): raise ValueError # check message for cancel
            new_send_email = Email(contact_path, pass_path, email_recipient, email_subject, email_body, speak_type)
            Email_Service = EmailService()
            thread_email = Thread(target = Email_Service.sendemail, args = (new_send_email,))
            thread_email.start()
        except Exception as e:
            print('Cancelling')

    # Misc Commands #

    elif command == 'what time is it' or command == 'current time':
        speak('The time is ' + datetime.now().strftime('%-I:%M %p'), speak_type)

    elif command == 'what is the date' or command == 'what\'s the date' or command == 'current date' or command == 'date today':
        speak('The date is ' + datetime.now().strftime('%A %B %-d %Y'), speak_type)

    elif "day of the week" in command or command == 'what day is it':
        speak(datetime.now().strftime('%A'), speak_type)

    elif command == 'week number':
        speak(datetime.now().strftime('%W'), speak_type)

    elif  'set a timer for' in command:
        time_for = splitJoin(command, 4) # function to split and rejoin command
        Timer_Service = TimerService(time_for, speak_type)
        thread_timer = Thread(target = Timer_Service.timerLogic)
        thread_timer.start()

    elif command == 'open calculator' or command == 'run calculator' or command == 'calculator':
        thread_calculator = Thread(target = openCalculator) # run calculator code from calculator.py
        print('Calculator Opened!') # open message
        thread_calculator.start() # start 2nd thread with calulator so you can run commands along with the calculator open

    elif command == 'open stopwatch' or command == 'run stopwatch' or command == 'stopwatch':
        thread_stopwatch = Thread(target = openStopwatch) # run calculator code from calculator.py
        print('Stopwatch Opened!') # open message
        thread_stopwatch.start() # start 2nd thread with calulator so you can run commands along with the calculator open
    
    # Help commands

    elif command == 'help':
        for c in command_list:
            print(c)

# Chance commands

    elif command == 'dice' or command == 'what dice can I roll':
        speak('You can roll a \nd4, d6, d8, d10, d12, d20', speak_type)

    elif command == 'roll a die' or command == 'd6' or command == '6 sided dice' or command == 'roll a d6' or command == 'roll a 6 sided die':
        rand_roll = random.randint(1, 6)
        speak('You rolled a ' + str(rand_roll), speak_type)
        marvin.asciiart.d6Roll(rand_roll)

    elif command == 'flip a coin' or command == 'flip coin':
        rand_coin = random.randint(1, 2)
        if rand_coin == 1:
            speak('You flipped head', speak_type)
            rand_face = random.randint(1, 2)
            if rand_face == 1:
                marvin.asciiart.head1Coin()
            else:
                marvin.asciiart.head2Coin()
        else:
            speak('You flipped tails', speak_type)
            marvin.asciiart.tailCoin()

# Marvin Interaction

    elif command == 'hello' or command == 'hi':
        speak('Hello!', speak_type)

    elif command == 'who are you':
        speak('I\'m Marvin a virtual assistant created by Rafael Cenzano to make everyday life better and easier', speak_type)

    else:
        with open(correction_path, 'r') as check_correction:
            correction_check = load(check_correction)
        if command in correction_check['corrections']:
            correct_term = correction_check['corrections'][command]['correct']
            return correct_term
        else:
            bob = True


    if bob == False:
        return 'null'
    elif bob == True:
        auto_corrected_list = get_close_matches(command, command_list, 1)
        if auto_corrected_list != []:
            auto_corrected = auto_corrected_list[0]
            speak('Did you mean ' + auto_corrected + '?', speak_type)
            input_auto_correct = commandInput(type_of_input) # function for listen or raw_input
            if 'y' in input_auto_correct:
                split_autocorrected = auto_corrected.split(" ") # split find how many words there are
                length_auto_corrected = len(split_autocorrected)
                length_needed = length_auto_corrected
                split_command_for_data = command.split(" ")[length_needed:]
                if split_command_for_data != []:
                    joined_command_data = (" ").join(split_command_for_data) # joining anything that was split from after any unnecessary words
                    return auto_corrected + ' ' + joined_command_data
                else:
                    correction_check['corrections'][command] = {"correct":auto_corrected} # new data to add
                    with open(correction_path, 'w') as outfile:
                        dump(correction_check, outfile)
                    return auto_corrected
            else:
                print('Command not found')
                return 'null'
        else:
            print('Command not found')
            return 'null'
    else:
        print('Error missing variable')
        raise MarvinRelog
