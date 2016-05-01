#!/usr/bin/python

# File to calculate the increments for an inside caliper
# Modified 2016-04-19 ***********************************
#*********************************************************
#*********************************************************

# import modules used here -- sys is a very standard one
import sys
import math
import os
import datetime

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
    print("\n\n*****************************************************")
    print("python version " +sys.version)
    print("*****************************************************\n")

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
def fdone():
    
    result = getinput("\n Press any key to finish  ")
    sresult = result + "\n****************  End  ****************\n"
    print(sresult)
    return 1

# getk1 function **************************************
def getk1(r1,r2):
  try:
    k1=r1/r2
    return k1
  except:
   return 1

# getk2 function **************************************
def getk2(d,r2):
  try:
    k2=d/r2
    return k2
  except:
    return 1

# domath function ************************************
def domath(num, inc, rad1, rad2):
  try:
    i=1
    num = int(num)
    sprnt = ""
    n=1

    while (i <= num):

       ang1=n*inc/rad2
       ang2 =(n-1)*inc/rad2

       sin1 = math.asin(ang1)
       sin2 = math.asin(ang2)

       dsin1 = sin1*180/PI
       if dsin1 >= 90:
           break
       
       sdsin1 = str('{:1.2f}'.format(dsin1))
       
       dsin2 = sin2*180/PI

       difangle = dsin1-dsin2 #Degrees
       rdifangle = difangle*PI/180 #radians
       
       dis = rad1*rdifangle
       sdis = str('{:1.2f}'.format(dis)) 
       
       #s = r*a
       ldist = rad2*sin1
       sldist = str('{:1.2f}'.format(ldist))

       
       dist = n*inc
       sdist =str( '{:1.2f}'.format(dist))

       sdata = "Indicator " + str(n) + " = " + sdis +  \
           "  Measured distance =  " + sdist + \
	   "  Distance from 0 = " + sldist +\
           "  Angle from 0 = " + sdsin1 + "\n"

       sprnt = sprnt + sdata

#       if dsin1 >= 90:
#          break
#       else:
       n = n+1
       i = i+1

    return str(sprnt)

  except:
    print ("Error on math function")
    serror = "1"
    return (serror)

#********************************************************************************
#********************************************************************************
#*********************************************************
#*********************************************************

# Gather our code in a main() function
def main():
  try:

    mytime = datetime.datetime.now().strftime("%Y-%m-%d")
    sresults = "\n" + str(mytime)

    os.system("clear")

    rad1 = getinput("Input a minor radius  ")
    rad2 = getinput("Input a major radius  ")
    inc = getinput("Input a distance for the increment  ")
    num = getinput("Input the number of iterations ")

    frad1 = float(rad1)
    frad2 = float(rad2)
    finc = float(inc)
    inum = int(num)

    mathans  = domath(inum, finc,frad1, frad2)
    
    os.system("clear")
    
    sresults = sresults + "\n\n*****************************************************"
    sresults = sresults + "\npython version " +sys.version
    sresults = sresults + "\n*****************************************************\n"
    sresults = sresults + "\nNumber of steps = " + str(num)
    sresults = sresults + "\nIncrementsl distance = " + str(inc)
    sresults = sresults + "\nMinor radius  = " + str(frad1)
    sresults = sresults + "\nMajor radius  = " + str(frad2)
    sresults = sresults + "\n********************************************************\n"
    sresults = sresults + str(mathans)

    print(sresults)
    ffile(sresults)

  except: 
    
    print( "Error in main" )
    fdone()
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

