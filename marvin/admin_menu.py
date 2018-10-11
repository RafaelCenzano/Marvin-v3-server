# Imports
from os import system, path # for getting paths for any os and system for running terminal commands
from json import load, dump # parse and add json data
from codecs import encode # to create new passwords
from hashlib import sha512 # to create new passwords
from getpass import getpass # for hiding password input like sudo commands
from marvin.network import get_ip # get ip function
from marvin.webscrape import getVersion # webscrape version
from marvin.essentials import speak # speak function


############################
# File for ADMIN Menu code #
############################


# Function to show ADMIN Menu
def ADMIN(contact_path, pass_path, speak_type): # ADMIN MENU
    bob = True
    while True: # loop for MENU so you don't have to keep reopening it
        try:
            print('\nOnly use ADMIN acount for administrative tasks') # message to remind you can't use marvins command without a real user
            print('\n######## ADMIN MENU ########\n\n1. Create New User     2. Delete a User\n3. Update Marvin       4. Marvin APPS\n5. Voice Settings      6. Leave ADMIN Menu\n7. Exit program') # show options
            ADMIN_input = input('>') # prompt for input

            if ADMIN_input == '1' or 'user' in ADMIN_input.lower(): # check if user wants to create a user
                with open(pass_path, 'r') as login_data: # open user info
                    new_user_data = load(login_data) # parse user info
                search_login = new_user_data['logins'] # put users into variable
                print('Showing all Users') # print user printing user message
                for x in search_login: # loop for all users
                    (x) # print all users

                print('You will choose a username and password for the new user\nType a User') # prompt for new usr and pass
                new_user = input('>') # type user
                if new_user in search_login: # check if user exists
                    print('This user exists already') # user exists message
                elif 'quit' == new_user.lower() or 'exit' == new_user.lower() or 'cancel' == new_user.lower(): 
                    raise ValueError # check message for cancel
                else: # user doesn't exist

                    while True: # loop until password over 5 characters
                        print('\nType a password for the new user thats over 5 characters') # message that pass have to be over 5 length
                        new_user_pass = input('>') # input for new user pass
                        if 'quit' == new_user_pass.lower() or 'exit' == new_user_pass.lower() or 'cancel' == new_user_pass.lower(): 
                            raise ValueError # check message for cancel
                        elif len(new_user_pass) <= 5: # if new password under 5 characters
                            print('Make your password over 5 characters please') # more characters message
                        else: # password over 5 characters
                            break # break loop

                    while True: # loop until correct passward
                        print('\nType your ADMIN password again to confirm this action') # ask for admin password
                        login_pass = getpass('>') # input password
                        login_pass2 = sha512(login_pass.encode('utf-8') + 'NQZVA').hexdigest() # hash password to match if in file
                        if login_pass2 == new_user_data['logins']['ADMIN']['pass']: # check if password matches
                            break # leave loop
                        elif 'quit' == login_pass2.lower() or 'exit' == login_pass2.lower() or 'cancel' == login_pass2.lower(): 
                            raise ValueError # check message for cancel
                        else: # password doesn't match
                            print('Incorect Credentials') # wrong password message
                            i = i + 1 # add tries
                            if i >= 5: # if over 5 tries
                                exit()

                    new_login = encode(new_user, 'rot13') # encode user name
                    new_user_pass_encrypted = sha512(new_user_pass.encode('utf-8') + new_login.encode('utf-8')).hexdigest() # hash password
                    print('Creating User') # print creating messsage
                    with open(pass_path, 'w') as outfile: # open file to add changes
                        new_user_data['logins'][new_user] = {"pass":new_user_pass_encrypted} # new user data
                        dump(new_user_data, outfile) # add new user data
                    print('New user created') # new user added messgae

            elif ADMIN_input == '2' or 'delete' in ADMIN_input.lower(): # check if user wants to delete a user
                with open(pass_path, 'r') as login_data: # open file to find exisiting users
                    new_user_data = load(login_data) # parse data
                search_login = new_user_data['logins'] # get all users
                print('Showing all Users') # showing users message
                for x in search_login: # loop until all users printed
                    print(x) # print all users
                print('\nWhat user do you want to delete') # ask which user to delete
                del_user = input('>') # input for user to delete
                if del_user == 'ADMIN': # if input user is ADMIN
                    print('Can\'t delete this user') # can't delete message
                elif 'quit' == del_user.lower() or 'exit' == del_user.lower() or 'cancel' == del_user.lower(): 
                    raise ValueError # check message for cancel
                elif del_user in search_login: # check if user exists
                    while True: # loop until correct passward
                        print('\nType your ADMIN password again to confirm this action') # ask for admin password
                        login_pass = getpass('>') # input password
                        login_pass2 = sha512(login_pass.encode('utf-8') + 'NQZVA').hexdigest() # hash password to match if in file
                        if login_pass2 == new_user_data['logins']['ADMIN']['pass']: # check if password matches
                            break # leave loop
                        elif 'quit' == login_pass2.lower() or 'exit' == login_pass2.lower() or 'cancel' == login_pass2.lower(): 
                            raise ValueError # check message for cancel
                        else: # password doesn't match
                            print('Incorect Credentials') # wrong password message
                            i = i + 1 # add tries
                            if i >= 5: # if over 5 tries
                                exit()
                    del new_user_data['logins'][del_user] # del user and data
                    with open(pass_path, 'w') as outfile: # open file
                        dump(new_user_data, outfile) # add updated file
                else: # no user found 
                    print('This User doesn\'t exist') # no user found message

            elif ADMIN_input == '3' or 'update' in ADMIN_input.lower(): # check if user want to update
                print('Checking for Update') # checking message
                with open('Os.json', 'r') as marvin_v: # open .Os.json to see marvin version
                    marvin_ver = load(marvin_v) # parse data
                    marvin_version = marvin_ver['Marvin_Release'] # get local marvin version
                online_marvin_version = getVersion() # get online marvin version
                if str(marvin_version) != str(online_marvin_version): # if they don't match
                    print('Update found') # found message
                    system('git pull') # pull from github
                    print('You will now have to reopen Marvin to make sure the changes went through') # restart message
                    with open('Os.json', 'w') as outfile: # open .Os.json to change marvin version
                        marvin_ver['Marvin_Release'] = online_marvin_version # change marvin version
                        dump(marvin_ver, outfile) # add new version number
                    exit()
                else: # versions match
                    print('No update found\n##############\nYou are up to date') # versions match message

            elif ADMIN_input == '4' or 'app' in ADMIN_input:
                print('\nshowing apps:\n')
                with open('Os.json', 'r') as marvin_a: # open .Os.json to see marvin version
                    marvin_apps = load(marvin_a) # parse data
                print('IOS app : ' + marvin_apps['apps']['IOS'])
                print('\nWould you like to enable any apps?')
                app_input = input('>').lower()
                if app_input == 'yes' or 'y' in app_input:
                    print('\nWhich app would you like to activate')
                    app_active = input('>').lower()
                    if app_active == 'ios' or app_active == 'apple':
                        print('Type this into app for ip ' + get_ip())
                    elif 'quit' == app_active.lower() or 'exit' == app_active.lower() or 'cancel' == app_active.lower():
                        raise ValueError # check message for cancel
                elif 'quit' == app_input.lower() or 'exit' == app_input.lower() or 'cancel' == app_input.lower(): 
                    raise ValueError # check message for cancel
                else:
                    print('Would you like to deactivate an app?')
                    deactivate_input = input('>').lower()
                    if 'quit' == deactivate_input.lower() or 'exit' == deactivate_input.lower() or 'cancel' == deactivate_input.lower(): 
                        raise ValueError # check message for cancel
                    elif deactivate_input.lower() == 'y' or deactivate_input == 'y':
                        pass

            elif ADMIN_input == '5' or 'voice' in ADMIN_input:
                with open('Os.json', 'r') as voice_settings:
                    voice_loaded = load(voice_settings)
                print('\nVoice currently set to ' + voice_loaded['voice'])
                if voice_loaded['voice'] == 'female':
                    print('\nWould you like to change to a male voice?')
                    voice = input('>')
                    if 'y' in voice:
                        print('Changing to male voice')
                        speak('This is what I sound like now', 'male')
                        print(voice_loaded['voice'])
                        with open('Os.json', 'w') as outfile:
                            var = voice_loaded['voice'] = 'male'
                            dump(voice_loaded, outfile)
                else:
                    print('\nWould you like to change to a female voice?')
                    voice = input('>')
                    if 'y' in voice:
                        print('Changing to female voice')
                        speak('This is what I sound like now', 'female')
                        with open('Os.json', 'w') as outfile:
                            var = voice_loaded['voice'] = 'female'
                            dump(voice_loaded, outfile)

            elif ADMIN_input == '6' or 'exit' in ADMIN_input.lower() or 'leave' in ADMIN_input.lower() or 'quit' in ADMIN_input.lower(): # check if user wants to leave Menu
                print('Exiting ADMIN MENU') # exit menu message
                break # break loop to leave ADMIN MENU

            elif ADMIN_input == '7': # if you want to exit
                print('Exiting program') # exit message
                bob = False # close program
                break
        except:
            pass
    if bob == False:
        exit()