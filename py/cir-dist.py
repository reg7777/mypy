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
  fo = getinput("Input the name of the file to output")
  f= open(fo, "a")
  f.write(sout)
  f.close()


# Exit function ****************************************
def exit():
    
    result = getinput("\n Press any key to finish  ")
    print(result)


# Calculate function *****************************************
def docal(fr1,fr2,fx):
    ratio = fr2/fr1
    fmindist = ratio*fx
    fver = .9 * fmindist
    fang = 2*math.asin(fx/(2*fr1))
    fang = fang*180/PI
    return(fmindist, fang,fver )
	
	
#********************************************************************************
#********************************************************************************
#*********************************************************
#*********************************************************

# Gather our code in a main() function
def main():
    header()
    x = getinput("Input a value for x ")
    fx = float(x)
    x = getinput("Input a value for the maximum radius ")
    fr1 = float(x)
    x = getinput("Input a value for the minium radius ")
    fr2 = float(x)
#    sout = "x = " + str(fx) + " Maxrad = " + str(fr1) + "Minrad = " + str(fr2)  
#    fprintout(sout) 
    fmindist, fang,fver =docal(fr1,fr2,fx)
    
    sout = "The minium distance is " + str(fmindist)
    fprintout(sout)
#   sout = "The incremental distance is " + str(finc)
#    fprintout(sout)
    sout = "The angle is " + str(fang)
    fprintout(sout)
    
    sout = "\n\n   Increment \t  Distance \t Angle \t Vernier"
    fprintout(sout)

    spout =sout + "\n"
    for m in range(10,220,10):
      fm = float(m)
      v,a,ver = docal(fr1,fr2,fm)
      v= "{:10.2f}".format(v)
      a= "{:10.2f}".format(a)
      ver = "{:10.2f}".format(ver)
      sout = "   " + str(m) + "\t   " +str(v) + "\t" + str(a) + "\t" + str(ver)
      fprintout(sout)
      spout = spout + sout + "\n"
      
    ffile(spout)
      
       
       
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

