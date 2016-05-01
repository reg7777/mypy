#!/usr/bin/python

# Modified 2016-04-03 ***********************************
#*********************************************************
#*********************************************************

# import modules used here -- sys is a very standard one
import sys
import math


#   Define functions

#Begin definitions **************************************
#*********************************************************
#*********************************************************
# degrees = radians*180/pi
# radians = degrees*pi/180
# python trig uses radians

# sine x = opposite/hypotenuse
# cosine x = adjacent/hypotenuse
# tangent = opposite/adjacent

PI = 3.14159265
ER = 0  #**********Turn on (1) for use in error tests


# Get input function ********************************
#*********************************************************
#*********************************************************

def getinput(sprompt):
    try:
        try:
           result = raw_input(sprompt)
        except:
           result = input(sprompt)
    except:
        print("Error in getinput function")
    return result

#*********************************************************
# Header function    
def header():
    print("*****************************************************")
    print("python version " +sys.version)
    print("*****************************************************")
    return

#*********************************************************
# Print function
def fprintout(lpdata):
  print
  print( lpdata)
  print

#*********************************************************
# Print to file function
def ffile(sout):
  f= open("out.txt", "a")
  f.write(sout)
  f.close()


# Exit function ****************************************
def exit():
    
    result = getinput("\n Press any key to finish\n")
    print(result)

#********************************************************************************
#********************************************************************************
#*********************************************************
#*********************************************************

# Gather our code in a main() function
def main():
    header()
    x = getinput("Test input  ")
    exit()



#Run main ***********************************************
#*********************************************************
#*********************************************************
#********************************************************
#********************************************************
if __name__ == '__main__':
    main()
#********************************************************
#********************************************************

