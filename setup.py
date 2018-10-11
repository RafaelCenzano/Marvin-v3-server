# Imports
import os
from platform import system, release, python_version
from json import dump, load
from hashlib import sha512
import sys

# Main Code
while True:
    print('Setting Up Marvin\nADMIN acount username is ADMIN\nPlease set a password for the ADMIN acount\nMake the password longer than 5 characters')
    new_pass = input('>')
    if len(new_pass) <= 5:
        print('Make your password longer than 5 characters please')
    else:
        pass_new = sha512(new_pass.encode('utf-8') + 'NQZVA'.encode('utf-8')).hexdigest()
        break

path = os.getcwd()
def unix_linux(pass_path, python_path, os):
    os.system('pip install virtualenv==16.0.0')
    os.system('virtualenv --python=' + python_path + ' marvin-env')
    if os == 'Darwin':
        os.system('marvin-env/bin/pip install --editable git+https://github.com/nateshmbhat/pyttsx3.git@master#egg=pyttsx3')
    else:
        os.system('marvin-env/bin/pip install pyttsx3')
    os.system('marvin-env/bin/pip install -r requirements.txt')
    env = ('source ' + path + '/marvin-env/bin/activate')
    script = (path + '/marvin-env/bin/python2.7 ' + path + '/Marvin_Script.py')
    cd = ('cd ' + path)
    # marvin script start file
    out2 = open('marvin_run.sh', 'a')
    out2.write('#!/bin/bash')
    out2.write('\n')
    out2.write(env)
    out2.write('\n')
    out2.write(cd)
    out2.write('\n')
    out2.write(script)
    out2.write('\n')
    out2.write('deactivate')
    out2.close()
    os.system('chmod 755 marvin_run.sh')
    with open(pass_path, 'w') as outfile2:
        var1 = {"email_address":email_usr, "email_password":email_pass, "logins":{"ADMIN":{"pass":pass_new}}}
        dump(var1, outfile2)
    os.system(path + '/marvin-env/bin/python marvin/create_files.py')
    print('\n\nAll files and installs completed\nYou can now run Marvin with the command marvin')

check_os = system()
os_release = release()
print ('Decting Operating System')
print ('Your os type is ' + check_os)
print ('Your os version is ' + os_release)

print('Creating needed files')

pass_path = os.path.join('marvin','json','pass.json')

print('We need your email to be able to send emails')
print('\n#####\nYou will need to change an email setting that allows less secure apps\n#####\n')
print('\nIf you dont want the email function type none')
print('Please type email address')
email_usr = input('>')
print('Please type email password')
email_pass = input('>')

print('Starting installs')

if check_os == 'Linux':
    alias = 'alias marvin="' + path + '/marvin_run.sh"'
    homefolder = os.path.expanduser('~')
    bashrc = os.path.abspath('%s/.bashrc' % homefolder)
    with open(bashrc, 'r') as f:
        lines = f.readlines()
        if alias in lines:
            print('Please delete your alias command marvin in your .bashrc file')
            exit()
        else:
            out = open(bashrc, 'a')
            out.write(alias)
            out.close()
    os.system('source ' + bashrc)
    print('\nGoing to install tkinter for GUI')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install python-tk')
    if '3.7' in python_version():
        unix_linux(pass_path, '/usr/bin/python3', 'Linux')
    else:
        print('Error python3 version not found please type full absolute path to your python3')
        os.system('sudo apt-get install python3.7')
        unix_linux(pass_path, '/usr/bin/python3', 'Linux')

elif check_os == 'Darwin':
    alias = ('alias marvin="' + path + '/marvin_run.sh"')
    homefolder = os.path.expanduser('~')
    bashrc = os.path.abspath('%s/.bash_profile' % homefolder)
    with open(bashrc, 'r') as f:
        lines = f.readlines()
        if alias in lines:
            print('Please delete your alias command marvin in your ~/.bash_profile file')
        else:
            out = open(bashrc, 'a')
            out.write(alias)
            out.close()
            os.system('source ' + bashrc)
    print('We need to install Homebrew so that we can install portaudio')
    os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    print('Installing portaudio')
    os.system('brew install portaudio')
    if '3.7' in python_version():
        unix_linux(pass_path, '/usr/local/bin/python3.7', 'Darwin')
    else:
        os.system('brew install python3')
        unix_linux(pass_path, '/usr/local/bin/python3', 'Darwin')

elif check_os == 'Windows':
    python_path = os.path.join('C:','\\Users','savag','AppData','Local','Programs','Python','Python37','python.exe')
    if os.path.isfile(python_path) == False:
        print("Python3.7 not installed or is not in the default location. Please input your path to python.exe in your Python37 folder. \nExample:\nC:\\Documents\\Programming\\Python37\\python.exe\n\nIf you do not have python installed please close the program and install it here: https://www.python.org/downloads/windows/ and install it in the default location")
        python_path = input('>')
        if os.path.isfile(python_path) == False:
            print('Please install python2.7 here: https://www.python.org/downloads/windows/')
            exit()
    python_path_list = python_path.split("\\")
    python_path_list.remove('python.exe')
    fixed_python_path = ("\\").join(python_path_list)
    pip_path = (fixed_python_path + '\\Scripts\\pip.exe')
    if os.path.isfile(pip_path) == False:
        print('You need to install pip')
        exit()
    os.system(pip_path + ' install virtualenv==16.0.0')
    os.system('virtualenv --python=' + python_path + ' marvin-env')
    fixed_pip_path = (path + '\\marvin-env\\Scripts\\pip.exe')
    os.system(fixed_pip_path + ' install -r requirements.txt')
    with open(pass_path, 'w') as outfile2:
        var1 = {"email_address":email_usr, "email_password":email_pass, "logins":{"ADMIN":{"pass":pass_new}}}
        dump(var1, outfile2)
    os.system(path + '\\marvin-env\\Scripts\\python.exe marvin\\create_files.py')
    out = open('marvin.bat', 'w')
    out.write('@echo off\n')
    out.write('cd ' + path)
    out.write('\n')
    out.write(path + '\\marvin-env\\Scripts\\python.exe ' + path + '\\Marvin_Script.py')
    out.close()
    print('\n\nAll files and installs completed\nYou can now run Marvin by typing marvin in this folder or add this ' + path + ' to a new line in your path enviorment variable and type marvin')
else:
    print ('We dont have a way to set up Marvin on your Operating System.\nIf this is a mistake make sure to report it as an issue at https://github.com/SavageCoder77/MARVIN_2.0')
