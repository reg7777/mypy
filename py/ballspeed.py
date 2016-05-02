#!/usr/bin/python

#*******************************************************
#2016-05-01 nodified header
#Calculate the ball speed parameters from mph and distance
#*******************************************************
#*******************************************************

#imports ***********************************************
import sys
import os
import math


#Begin definitions **************************************
# degrees = radians*180/pi
# radians = degrees*pi/180
# python trig uses radians

PI = math.pi
ER = 0  #**********Turn on (1) for use in error tests
FM = 88/60   #88ft/sec = 60 mph
# Get input function ********************************
def getinput(sprompt):
    try:
        try:
           result = raw_input(sprompt)
           if(ER == 1):
               print("\n***************")
               ty = result.type
               print("result = " + str(result) +"  type " +ty)
        except:
           result = input(sprompt)
           if(ER == 1):
               print("\n***************")
               ty = type(result)
               print("result = " + str(result) +"  type " +str(ty))

    except:
        print("Error in getinput function")
    return result

# Header function    
def header():
    print("*****************************************************")
    print("python version " +sys.version)
    print("*****************************************************")
    return

# Ball speed calculations
def ballcal(mph, dist):
# 88fps/60mph = fps/mph
    ratio = 88.0/60.0
    fps = (ratio*float(mph))
    foottime = (1/fps)*1000
    disttime = float(dist) * foottime
    if(ER == 1):
        print("fps = " +str(fps))
        print("foottime = " +str(foottime))    
    return fps, foottime, disttime
    
# Metric conversion function
def metriccal(fpers):
    fpers = float(fpers)
    mpers =12*.0245*fpers/100
    sperm = 1/mpers
    return mpers, sperm

# Main function  ************************************
def main():
    os.system('clear')
    header()
    x = getinput("What is ball speed in mph?  ")
    x1 = getinput("What is distance in feet? (Default home to pitcher 60.5 ft)?  ")
    if(x1 == ''):
        x1 = float(60.5)
    ftpersec, timeperft, distms = ballcal(x, x1)
    ftpersec = format(ftpersec, '0.2f')
    timeperft = format(timeperft, '0.2f')
    distms = format(distms, '0.2f')
    print("\n" +x +" miles per hour is " +str(ftpersec) +" feet per sec")
    print("Time for 1 foot is = " +str(timeperft) +"ms")
    print("Time for total distance is = " +str(distms) +"ms")
    
    meterpersec, secpermeter = metriccal(ftpersec)
    meterpersec = format(meterpersec, '0.2f')
    secpermeter = format(secpermeter, '0.4f')
    print("\n" +x +"mph is = " +str(meterpersec) + " meters/sec")
    print("Time for 1 meter is = " +str(secpermeter) +"ms")    
    print("\n")

#   exit()

# Exit function ****************************************
def exit():
    
    result = getinput("\n Press any key to finish  ")
    print(result)
        
#Run main ***********************************************
#********************************************************
#********************************************************
if __name__ == '__main__':
    main()
#********************************************************
#********************************************************
