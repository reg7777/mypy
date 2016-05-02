#!/usr/bin/python

# Modified 2016-05-01 ***********************************
# Take in a string of digits and return the average.
#*********************************************************
#*********************************************************

# import modules used here -- sys is a very standard one
import sys
import math
import os


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
    print("Average of a string of input numbers")
    print("  Press 'q' to quit")
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
    os.system('clear')
    header()
    x = ''
    fa = float(0)
    it = 1
    sdata = ""

    while( x != 'q'):
       ix = getinput("Input number   " + str(it) + ": ")
       sdata = sdata + " " + str(ix)

       x = ix
       
       if x == 'q':
           break

       fx = float(x)
       fa = fa + fx
       fsa = '{:0.2f}'.format(fa)
       sa = str(fsa)
       
       it = it + 1

       fit = float(it-1)
       favg = (fa/fit)
       favg = '{:0.2f}'.format(favg)
       savg = str(favg)

    it =it-1
    sit = str(it)
    os.system('clear')
    header()
    
    print("\nData = " + sdata)
    print("\nCount = " + sit +  "\nSum of the numbers = " + sa + "\nAverage = " + savg)
    print("\n")
#   exit()



#Run main ***********************************************
#*********************************************************
#*********************************************************
#********************************************************
#********************************************************
if __name__ == '__main__':
    main()
#********************************************************
#********************************************************

