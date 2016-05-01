#!/usr/bin/python

# Modified 2016-03-17 ***********************************
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
    
    result = getinput("\nPress any key to finish\n")
    print(result)

# function runit ***************************************
def runit(g, w, v):
      #g = glass area
      #w = wall area
      #v = volume
      #stb = sqft to btu
      #btw =btu to watts

#      g = 3*2*2
#      w = 7*12
#      v = 7*12*12
      stb =240
      btw = .239
      wpf =300.00
      heat =((g/2) + (w/20) + (v/200))
      bheat = heat*stb
      wheat = bheat*btw 
      sheat =str( "{:4.2f}".format(heat))
      sbheat =str( "{:4.2f}".format(bheat))
      swheat =str( "{:4.2f}".format(wheat))
      
      feh = wheat/wpf
      sfeh =str( "{:4.2f}".format(feh))
      


      print("\nThe number of BTU's required = ", sbheat)
      print("  at 240 BTU per SQ FT.")
      print("\nThe number of watts is equal to :",  swheat)
      print("  at 0.239 watts per BTU")
      print("\nFeet of electric heat = ", sfeh )
      print("  at 300 watts per foot.")
      print("\nDone")


#********************************************************************************
#********************************************************************************
#*********************************************************
#*********************************************************

# Gather our code in a main() function
def main():
    header()
    g1 = getinput("Input the total glass width ")
    g2 = getinput("Input the glass height ")
    fg1 = float(g1)
    fg2 = float(g2)
    g= fg1*fg2

    w1 = getinput("Input the outside wall width ")
    w2 = getinput("Input the outside wall height ")
    fw1 = float(w1)
    fw2 = float(w2)
    w = fw1*fw2

    v1 = getinput("Input the space width ")
    v2 = getinput("Input the space length ")
    v3 = getinput("Input the space heigth ")
    fv1 = float(v1)
    fv2 = float(v2)
    fv3 = float(v3)
    v = fv1 * fv2 * fv3

    runit(g, w, v)

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

