# Imports
from os import path
from platform import system # find os type
from subprocess import Popen, PIPE # to run GUI with terminal command

###############################
# File for miscellaneous code #
###############################

class MarvinExit(Exception): pass # class to exit program

# Function to open calculator GUI with subprocess
def openCalculator():
    if system() == 'Windows':
        python_path = path.join('marvin-env','Scripts','python.exe')
    else:
        python_path = path.join('marvin-env','bin','python') # get path for any os
    calculator_path = path.join('marvin','called_files','calculator.py') # get path for any os
    calculator = Popen([python_path + ' ' + calculator_path], stdout = PIPE, stderr = PIPE, shell = True) # terminal command to run in shell
    (out, err) = calculator.communicate() # opening calculator file

# Function to open Stopwatch GUI with subprocess
def openStopwatch():
    if system() == 'Windows': # For windows os
        python_path = path.join('marvin-env','Scripts','python.exe') # executable for windows
    else: # for linux and unix
        python_path = path.join('marvin-env','bin','python') # get path for any os
    stopwatch_path = path.join('marvin','called_files','stopwatch.py') # get path for any os
    stopwatch = Popen([python_path + ' ' + stopwatch_path], stdout = PIPE, stderr = PIPE, shell = True) # terminal command to run in shell
    (out, err) = stopwatch.communicate() # opening stopwatch file