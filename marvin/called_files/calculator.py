from tkinter import * # import everything from tkinter module
import math # import square root and pi


###############################
# File to open GUI calculator #
###############################


expression = "" # globally declare the expression variable
show_expression = "" # globally declare show expression variable

# Function to update expression
# in the text entry box
def press(num):
    global expression # point out the global expression variable
    global show_expression # point out the global expression variable
    expression = expression + str(num)# concatenation of string
    show_expression = show_expression + str(num)# concatenation of string
    equation.set(show_expression)# update the expression by using set method

def equalpress(): # Function to evaluate the final expression
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
        global expression # point out the global expression variable
        global show_expression # point out the global expression variable
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression)) # set showing equation as answer

        if (float(total)).is_integer(): # remove .0 if number is integer
            fixed_answer = int(float(total))
        else: # leave number as float if its a float
            fixed_answer = total

        equation.set(str(fixed_answer)) # show answer
        # initialze the expression variable
        # by empty string
        expression = total
        show_expression = total
    # if error is generate then handle
    # by the except block
    except Exception as e:
        print(e)
        equation.set(" error ") # error message
        expression = "" # reset all text
        show_expression = "" # reset all text

def cuberoot():
    try:
        global expression # point out the global expression variable
        global show_expression # point out the global expression variable
        total = str(eval(expression)) # set showing equation as answer
        answer = float(total) ** (1. / 3)
        if (answer).is_integer(): # remove .0 if number is integer
            fixed_answer = int(answer)
        else: # leave number as float if its a float
            fixed_answer = answer
        equation.set(str(fixed_answer)) # set showing equation as answer
        expression = str(fixed_answer) # set showing equation as answer
        show_expression = str(fixed_answer) # set showing equation as answer
    # if error is generate then handle
    # by the except block
    except:
        equation.set(" error ") # error message
        expression = "" # reset all text
        show_expression = "" # reset all text

def percent():
    try:
        global expression # point out the global expression variable
        global show_expression # point out the global expression variable
        total = str(eval(expression)) # set showing equation as answer
        answer = (float(total) / 100)
        if (answer).is_integer(): # remove .0 if number is integer
            fixed_answer = int(answer)
        else: # leave number as float if its a float
            fixed_answer = answer
        equation.set(str(fixed_answer)) # set showing equation as answer
        expression = str(fixed_answer) # set showing equation as answer
        show_expression = str(fixed_answer) # set showing equation as answer
    # if error is generate then handle
    # by the except block
    except:
        equation.set(" error ") # error message
        expression = "" # reset all text
        show_expression = "" # reset all text

def addpi(): # add pi to equation
    try:
        global expression # point out the global expression variable
        global show_expression # point out the global expression variable
        if expression == "": # if no numbers have been input
            expression = str(math.pi) # set showing equation as answer
            show_expression = 'π' # set showing equation as answer
            equation.set('π') # set showing equation as answer
        else: # if numbers have been input
            expression = expression + str(math.pi) # set showing equation as answer
            show_expression = show_expression + 'π' # set showing equation as answer
            equation.set(show_expression) # set showing equation as answer
    # if error is generate then handle
    # by the except block
    except:
        equation.set(" error ") # error message
        expression = "" # reset all text
        show_expression = "" # reset all text

def squareroot_number2():
    try:
        global expression # point out the global expression variable
        global show_expression # point out the global expression variable
        total = str(eval(expression)) # set showing equation as answer
        answer = math.sqrt(float(total))
        if (answer).is_integer(): # remove .0 if number is integer
            fixed_answer = int(answer)
        else: # leave number as float if its a float
            fixed_answer = answer
        equation.set(str(fixed_answer)) # set showing equation as answer
        expression = str(fixed_answer) # set showing equation as answer
        show_expression = str(fixed_answer) # set showing equation as answer
    # if error is generate then handle
    # by the except block
    except:
        equation.set(" error ") # error message
        expression = "" # reset all text
        show_expression = "" # reset all text

def square():
    try:
        global expression # point out the global expression variable
        global show_expression # point out the global expression variable
        total = str(eval(expression)) # set showing equation as answer
        answer = math.pow(float(total), 2.0)
        if (answer).is_integer(): # remove .0 if number is integer
            fixed_answer = int(answer)
        else: # leave number as float if its a float
            fixed_answer = answer
        equation.set(str(fixed_answer)) # set showing equation as answer
        expression = str(fixed_answer) # set showing equation as answer
        show_expression = str(fixed_answer) # set showing equation as answer
    # if error is generate then handle
    # by the except block
    except:
        equation.set(" error ") # error message
        expression = "" # reset all text
        show_expression = "" # reset all text

def cube():
    try:
        global expression # point out the global expression variable
        global show_expression # point out the global expression variable
        total = str(eval(expression)) # set showing equation as answer
        answer = math.pow(float(total), 3.0)
        if (answer).is_integer(): # remove .0 if number is integer
            fixed_answer = int(answer)
        else: # leave number as float if its a float
            fixed_answer = answer
        equation.set(str(fixed_answer)) # set showing equation as answer
        expression = str(fixed_answer) # set hidden equation as answer
        show_expression = str(fixed_answer) # set showing equation as answer
    # if error is generate then handle
    # by the except block
    except:
        equation.set(" error ") # error message
        expression = "" # reset all text
        show_expression = "" # reset all text

# Function to clear the contents
# of text entry box
def clear():
    global expression # point out the global expression variable
    global show_expression # point out the global expression variable
    expression = "" # reset all text
    show_expression = "" # reset all text
    equation.set('enter your expression') # reset all text in equation box

# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
    gui.configure(background="light green") # set the background colour of GUI window
    gui.resizable(width=False, height=False) # stop resizing of window
    gui.title("Marvin Calculator") # set the title of GUI window
    gui.geometry("252x340") # set the configuration of GUI window

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)
    gui.focus_set() # Sets focus on the input text area

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=5, ipadx=0)
    equation.set('enter your expression')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',command=lambda: press(1), height=3, width=5, highlightbackground="light green")
    button1.grid(row=4, column=0)
    button2 = Button(gui, text=' 2 ', fg='black', bg='red',command=lambda: press(2), height=3, width=5, highlightbackground="light green")
    button2.grid(row=4, column=1)
    button3 = Button(gui, text=' 3 ', fg='black', bg='red',command=lambda: press(3), height=3, width=5, highlightbackground="light green")
    button3.grid(row=4, column=2)
    button4 = Button(gui, text=' 4 ', fg='black', bg='red',command=lambda: press(4), height=3, width=5, highlightbackground="light green")
    button4.grid(row=3, column=0)
    button5 = Button(gui, text=' 5 ', fg='black', bg='red',command=lambda: press(5), height=3, width=5, highlightbackground="light green")
    button5.grid(row=3, column=1)
    button6 = Button(gui, text=' 6 ', fg='black', bg='red',command=lambda: press(6), height=3, width=5, highlightbackground="light green")
    button6.grid(row=3, column=2)
    button7 = Button(gui, text=' 7 ', fg='black', bg='red',command=lambda: press(7), height=3, width=5, highlightbackground="light green")
    button7.grid(row=2, column=0)
    button8 = Button(gui, text=' 8 ', fg='black', bg='red',command=lambda: press(8), height=3, width=5, highlightbackground="light green")
    button8.grid(row=2, column=1)
    button9 = Button(gui, text=' 9 ', fg='black', bg='red',command=lambda: press(9), height=3, width=5, highlightbackground="light green")
    button9.grid(row=2, column=2)
    button0 = Button(gui, text=' 0 ', fg='black', bg='red',command=lambda: press(0), height=3, width=11, highlightbackground="light green")
    button0.grid(row=5, column=0, columnspan=2)
    plus = Button(gui, text=' + ', fg='black', bg='red',command=lambda: press("+"), height=3, width=5, highlightbackground="light green")
    plus.grid(row=1, column=3)
    minus = Button(gui, text=' - ', fg='black', bg='red',command=lambda: press("-"), height=3, width=5, highlightbackground="light green")
    minus.grid(row=2, column=3)
    multiply = Button(gui, text=' X ', fg='black', bg='red',command=lambda: press("*"), height=3, width=5, highlightbackground="light green")
    multiply.grid(row=3, column=3)
    divide = Button(gui, text=' / ', fg='black', bg='red',command=lambda: press("/"), height=3, width=5, highlightbackground="light green")
    divide.grid(row=4, column=3)
    equal = Button(gui, text=' = ', fg='black', bg='red',command=equalpress, height=3, width=5, highlightbackground="light green")
    equal.grid(row=5, column=3)
    clear = Button(gui, text='Clear', fg='black', bg='red',command=clear, height=3, width=11, highlightbackground="light green")
    clear.grid(row=1, column=0, columnspan=2)
    percent = Button(gui, text=' % ', fg='black', bg='red',command=percent, height=3, width=5, highlightbackground="light green")
    percent.grid(row=1, column=2)
    quit = Button(gui, text='Quit', fg='black', bg='red',command=gui.quit, height=3, width=22, highlightbackground="light green")
    quit.grid(row=6, column=0, columnspan=4)
    squareroot = Button(gui, text=' √ ', fg='black', bg='red',command=squareroot_number2, height=3, width=5, highlightbackground="light green")
    squareroot.grid(row=1, column=4)
    cuberoot = Button(gui, text=' ∛ ', fg='black', bg='red',command=cuberoot, height=3, width=5, highlightbackground="light green")
    cuberoot.grid(row=2, column=4)
    pi = Button(gui, text=' π ', fg='black', bg='red',command=addpi, height=3, width=5, highlightbackground="light green")
    pi.grid(row=3, column=4)
    dot = Button(gui, text=' . ', fg='black', bg='red',command=lambda: press('.'), height=3, width=5, highlightbackground="light green")
    dot.grid(row=5, column=2)
    square = Button(gui, text=' a² ', fg='black', bg='red',command=square, height=3, width=5, highlightbackground="light green")
    square.grid(row=4, column=4)
    cubed = Button(gui, text=' a³ ', fg='black', bg='red',command=cube, height=3, width=5, highlightbackground="light green")
    cubed.grid(row=5, column=4)

    # start the GUI
    gui.mainloop()