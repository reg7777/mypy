
import math




#   Define functions

def fdo_ring(smulti):
#   Get inputs
  print
  if smulti=="n":
    sring = "0"
  else:
    sring = raw_input("Input the ring number")
  nseg = raw_input("Imput the number of segments  ")
  sdia = raw_input("Input the outside diameter  ")
  sir = raw_input("Input the inside diameter  ")
  sheigth = raw_input("Input the ring heigth ")

  return sring, nseg, sdia, sheigth, sir

def fgetang(nseg ):
  #   Get the angles
  iang = 360/int(nseg)
  ihalfang = iang/2
  shalfang = str(ihalfang)
  irad =math.radians(ihalfang)
  return shalfang, ihalfang, iang, irad

def fcaloseg(irad, foradius):
  #  Calculate the outside segment
  ftan=math.tan(irad)
  fseg =2*foradius*ftan
  fsi = ("%.2f" %fseg)
  ssi = str(fsi)
  return ssi

def fcalirad(irad, firadius):
  #   Calculate the inside segment measure
  fcos = math.cos(irad)
  finsideSeg = firadius*fcos
  sinsideSeg = str(finsideSeg)
  return finsideSeg

def fcalthk(foradius, finsideSeg):
  #   Calculate the thickness
  fthick = foradius-finsideSeg
  sthick = str("%.2f" %fthick)
  return sthick

def fcir(fdia):
  #   Calculate the thickness
  fcirlen= fdia * 3.14159
  scir = str("%.2f" %fcirlen)
  return scir

def fstock(segs, ssi):
  #   Calculate the thickness
  fstk= ssi * segs
  sstk = str("%.2f" %fstk)
  return sstk

def fprintout(lpdata):
  print
  print lpdata
  print

def ffile(sout):
  f= open("rings.txt", "a")
  f.write(sout)
  f.close()

def getin(message):
  result = raw_input(message)
  result = result.lower()
  return result

#********************************************************************************
#********************************************************************************
def Main(): 
# Get user input
  txt1 = "Multiple rings? (y or n)"
  ans1 = getin(txt1)
  if ans1 == "n":
   iwhile = 1
  else:
   iwhile = 0

  while iwhile < 2:
#  Get inputs
    sring, nseg, sdia, sheigth, sir  = fdo_ring(ans1)
#  Do conversions
#   Convert inputs
    fring = float(sring)
    fdia = float(sdia)
    foradius = fdia/2
    soradius = str(foradius)
    fidia = float(sir)
    firadius = fidia/2
    siradius = str(firadius)
    sheigth = str(sheigth)
    fnseg = float(nseg)
#  Get angle  
    shalfang, ihalfang, iang, irad = fgetang(nseg )
#  Do calculations
    ssi = fcaloseg(irad, foradius)
    finsiderad = fcalirad(irad, firadius)
    sthick = fcalthk(foradius, finsiderad)
    scir = fcir(fdia)
    fsi = float(ssi)
    stock = fstock(fnseg, fsi)
  #finsideSeg = fcalculations(irad, foradius, firadius)

#  Build output string for file
    sout = "\n******************\nRing " + sring + "\n" +\
    " Num of seg " + nseg + "\n" +\
    " Radius = "+ soradius + "\n" +\
    " Dia = " + sdia + "\n" + \
    " Inside dia = " + sir + "\n" +\
    " Circumference = " + scir + "\n" +\
    " Seg angle = " + str(iang) + "\n" +\
    "  Cut angle = " + shalfang + "\n" +\
    " Seg length = " + ssi + "\n" +\
    " Thickness = " + sthick + "\n" +\
    " Height = " + sheigth + "\n" +\
    " Stock (LWH) = ( " + stock + " X " + " X " + sthick + " X " + sheigth + " )" + "\n"
 

#  Print results to file
    ffile(sout)


#  Build output file for display
    sdisp = "***********************************\n" +\
    "Ring " + sring + "\n" +\
    "Number of segments " + nseg + "\n" +\
    "Outsid radius = " + soradius + "\n" +\
    "Outside diameter = " + sdia + "\n" +\
    "Inside diameter = " + sir + "\n" +\
    "Circumference = " + scir + "\n" +\
    "Segment angle  = " +  str(iang) + "\n" +\
    "Cut angle = " +  str(ihalfang) + "\n" +\
    "Segment length is " +  ssi + "\n" +\
    "Segment thickness = " +  sthick + "\n" +\
    "Segment height is = " +  sheigth + "\n" +\
    "Stock (LWH) = ( " + stock + " X " + " X " + sthick + " X " + sheigth + " )" + "\n" +\
    "***********************************\n"

#  Display the results
    fprintout(sdisp)
# If one ring
    if ans1 == "n":
#      iwhile =2
       break

# Check for more rings
    txt1 = "Another ring? (y or n)"
    ans = getin(txt1)
    if ans == "n":
      iwhile = 2
#********************************************************************************
#********************************************************************************


Main()


