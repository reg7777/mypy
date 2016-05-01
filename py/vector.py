#!/usr/bin/python

#Will need to change input statements ('raw_input' or 'input')
#   dependent on python version
#'raw_input' for python up to 2.7
#'input' for python 3.0 on

#imports ***********************************************
import sys
import os
import math


#Begin definitions **************************************

PI = 3.14159265

# Get input function ********************************
def getinput(sprompt):
    try:
       result = raw_input(sprompt)
    except:
       result = input(sprompt)
    return result
    

# Get vector function ********************************
def getvector():
    length = getinput("Input vector length   ")
    length = float(length)
    ang = getinput("Input vector angle  ")
    ang = float(ang)
    return length, ang

def vector(inlen,inang):
    y= inlen * math.sin(inang*PI/180)
    x= inlen * math.cos(inang*PI/180)
    return x, y

def computevector():
    vlen, vang = getvector()
#    print("Vector is: " + str(vlen) + ",  " + str(vang))
    vx, vy = vector(vlen, vang)
    vx = format(vx,'0.3f')
    vy = format(vy,'0.3f')
#    print("vector x and y : " +str(vx) +" " +str(vy))
    return vx, vy

def totalvector(v1x,v1y,v2x,v2y):
    v1x = float(v1x)
    v1y = float(v1y)
    v2x = float(v2x)
    v2y = float(v2y)
    tvecx = v1x+v2x
    tvecy = v1y+v2y
    x = float(tvecy/tvecx)
#    print("************* ratio of y/x = " +str(x))
    vecang = math.atan(x)
#    svecangrad = format(vecang,'0.3f')
#    print("********* vecang = " +str(svecangrad))
    veclen = tvecy/math.sin(vecang)
    vecang = vecang*180/PI
#    sveclen = format(veclen,'0.3f')
#    print("********* veclen = " +str(sveclen))
#    print("\nToltal vector xy is = " +str(tvecx) + ",  " + str(tvecy))
    return veclen, vecang, tvecx, tvecy
    
def main():
    print("*****************************************************")
    print("python version " +sys.version)
    print("*****************************************************")
    vec1x, vec1y = computevector()
    vec2x, vec2y = computevector()
    print("\nInput vector 1 is: " + str(vec1x) + ",  " + str(vec1y))
    print("Input vector 2 is: " + str(vec2x) + ",  " + str(vec2y))
    totallen, totalang, totalx, totaly = totalvector(vec1x, vec1y, vec2x, vec2y)
    totallen = format(totallen, '0.3f')
    totalang = format(totalang, '0.3f')
    totalx = format(totalx, '0.3f')
    totaly = format(totaly, '0.3f')
    print("\nTotal vector is : " +str(totallen) +",   " +str(totalang))
    print("Total vector xy is = " +str(totalx) + ",  " + str(totaly))
    exit()
    
def exit():
  #  result = raw_input("\n Press any key to finish  ")  #use for python 2.7
    try:
       result = input("\n Press any key to finish  ")  #use for python 3.4
       print(result)
    except:
       print("\n  ********  Wrong python version  *******")

#Run main ***********************************************
if __name__ == '__main__':
    main()

