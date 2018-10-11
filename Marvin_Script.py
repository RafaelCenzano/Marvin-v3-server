# Imports
import marvin.misc # import MarvinExit class
import marvin.commands # import all commands
from os import path # path to create paths per os type
from json import load # import json.load to format json data
from codecs import encode # function to encode data
from hashlib import sha512 # hash data
from getpass import getpass # for hiding password input like sudo commands
from marvin.admin_menu import ADMIN # import ADMIN menu
from marvin.essentials import speak, listen # import speak and listen


'''
Code in this file runs everything that is Marvin.
It does logins and command input.
'''

contact_path = path.join('marvin','json','contacts.json') # Format Paths
pass_path = path.join('marvin','json','pass.json') # Format Paths
correction_path = path.join('marvin','json','correction.json') # Format Paths

# Master Loop
while True:


# LOGIN
    try: # try to have the ability to restart loop all the way to login

        with open('Os.json', 'r') as os_data: # open Os.json to get data
            os_type_loaded = load(os_data) # format data
            os_type = os_type_loaded['Os_data']['OS'] # get os type Example(Windows, Linux, Darwin)
            speak_type = os_type_loaded['voice'] # get male or female voice type

        with open(pass_path, 'r') as login_data: # open pass.json to get all users
            new_login_data = load(login_data) # format data
            search_login = new_login_data['logins'] # get users that can be logined in to

        while True: # loop until full user correct and ready for commands
            while True: # loop until user entered correctly
                print('\n\n\n\n##### LOGIN #####\n') # login message
                print('Login in with:') # list header
                for x in search_login: # loop to prinnt all users
                    print(x) # print each user
                login_usr = input('>') # take input of which user to login with
                if login_usr not in search_login: # user doesn't exists
                    print('\n######################\nIncorrect User\n#######################\n') # no user message
                else: # user found
                    break # leave loop

            new_login = encode(login_usr, 'rot13') # encode user for salt
            print('Please Type Password') # type password prompt
            login_pass = getpass('>')
            login_pass2 = sha512(login_pass.encode('utf-8') + new_login.encode('utf-8')).hexdigest() # hash
            if login_pass2 == new_login_data['logins'][login_usr]['pass']: # if passwords match allow login
                if login_usr == 'ADMIN': # if user admin open admin menu
                    ADMIN(contact_path, pass_path, speak_type) # open admin menu
                    raise marvin.commands.MarvinRelog # restart to login to not allow admins to use commands
                break # break loop if not admin
            else: # wrong password
                print('\n#####################\nIncorrect Credentials\n#####################\n') # incorrect password message


# MAIN command loop


        while True: # input type loop
            '''
        core loop this is the part that will be looped to check user wants to keep using voice commands
        it will always ask the user the prompt below when the while loop goes back to the start
        part that will run when while loop resets
            '''
            speak('\nChoose an option', speak_type) # ask for which type of input
            print(' \nOPTIONS:\n1. voice commands\n2. typed commands\n3. standby\n4. quit\n ') # options for inputs
            beg_input = input(">").lower() # input for which option chosen

            if beg_input == '1' or 'voice' in beg_input: # voice commands
                try: # try to be able to restart loop

                    while 1: # loop to repeat listening commands
                        print('\nAwaiting commands') # prompt for command
                        data = listen() #use listen function in commands.py
                        marvin_command_data = marvin.commands.dataCommands(data.lower(), 1, pass_path, contact_path, correction_path, os_type, speak_type) # check for command and lower what was just said
                        if marvin_command_data != 'null': # when command was spelled incorrectly
                            marvin_command_run_2 = marvin.commands.dataCommands(marvin_command_data, 1, pass_path, contact_path, correction_path, os_type, speak_type) # check for command and lower what was just said and adds 0 value to show raw input and not talking commands

                except marvin.commands.MarvinCommands: # except and pass to resume stanby
                    pass # restart loop

            elif beg_input == '2' or 'type' in beg_input: # typed commands
                try: # try to be able to restart loop

                    while 1: # loop to repeat input for commands
                        print('\nAwaiting commands') # prompt for command
                        data = input('') # input of typed command
                        marvin_command_data = marvin.commands.dataCommands(data.lower(), 0, pass_path, contact_path, correction_path, os_type, speak_type) # check for command and lower what was just said and adds 0 value to show raw input and not talking commands
                        if marvin_command_data != 'null': # when command was spelled incorrectly
                            marvin_command_run_2 = marvin.commands.dataCommands(marvin_command_data, 0, pass_path, contact_path, correction_path, os_type, speak_type) # check for command and lower what was just said and adds 0 value to show raw input and not talking commands

                except marvin.commands.MarvinCommands: # except and pass to resume stanby
                    pass #restart loop

            elif beg_input == '3' or 'standby' in beg_input: # standby no recording

                while True: # loop until start or quit entered
                    print("Type start to reopen commands or quit to exit") # show options
                    y_n = input('>') # take input of standby
                    if 'start' in y_n.lower(): # if user wants to choose input type
                        break # restart loop
                    elif 'quit' in y_n.lower() or 'leave' in y_n.lower() or 'exit' in y_n.lower(): # exit
                        raise marvin.misc.MarvinExit # raise MarvinExit to exit

            elif beg_input == '4' or 'quit' in beg_input or 'exit' in beg_input: # if the user just wants to end marvin
                raise marvin.misc.MarvinExit # raise MarvinExit to exit

            else: # input not matched to any options
                print('Did you spell it wrong? try again') # error messgae

    except marvin.commands.MarvinRelog: # if marvin.commands.MarvinRelog raised will restart loop all the way to logins
        pass # skip and restart loop

    except marvin.misc.MarvinExit:
        speak('closing program', speak_type) # exit message
        exit() # exit program