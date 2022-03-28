# WET BULB TEMPERATURE CALCULATOR
#
# This script is written in Python.
# You need to have Python3 installed on your computer in order to use this script.
# Made by Sven Azari
# http://www.github.com/svenazari
#
# INSTRUCTIONS:
#   1.) TT - air temeperature [°C] - input without decimal point (e.g. 21.8 = 218)
#   2.) UU - relative humidity [%]
#   3.) BBB - air pressure [hPa] - input without thousand digit and decimal point (e.g 1013.3 = 133 and 995.2 = 9952)
#           - if air pressure is unknown just leave it empty - in that case, script will use mean atmospheric pressure at sea level
#   4.) HT - calcualted wet-bulb temperature [°C] - printed without decimal point - if calculated value is negative, instead of - sign, there will be W or I in front of number - W indicates there is water on wet-bulb termomether sensor and I indicates there is ice - value in [] is for wet-bulb temperature with ice on bet-bulb termomether sensor
#   5.) For exit just type "exit".
#   6.) In case of wrong input, type "back".

#moduls inport
import math 
import sys
from os import system, name

def clear ():
  if name == 'nt':
      _ = system('cls')
  else:
      _ = system('clear')
      
#main part
def script ():
  clear ()
  print (" W     W       BBB        TTTTT       CCC")
  print (" W     W       B  B         T         C C")
  print ("  W   W        B B          T         C")
  print ("  W W W        BB           T         C")
  print ("   WWW         B B          T         C")
  print ("   WWW         B  B         T         C C")
  print ("   W W         BBB          T         CCC")
  print ("                              Version 2.0")
  print (" ")
  print ("##########################################")
  print ("# WET-BULB TEMPERATURE CALCULATOR        #")
  print ("#                                        #")
  print ("# INSTRUCTIONS:                          #")
  print ("# TT - air temperature [°C]              #")
  print ("# (input without decimal point)          #")
  print ("# UU - relative humidity [%]             #")
  print ("# BBB - air pressure [hPa]               #")
  print ("# (input without thousand digit or       #")
  print ("#   decimal point                        #")
  print ("#  - if unknown just leave it empty)     #")
  print ("#                                        #")
  print ("# For exit just type exit.               #")
  print ("#                                        #")
  print ("# In case of wrong input, type back.     #")
  print ("##########################################")
  print (" ")
  #input
  TT = input ("TT = ")
  if (TT == "exit"):
    clear ()
    sys.exit (0)
  elif (TT == "back"):
    script ()
  UU = input ("UU = ")
  if (UU == "exit"):
    clear ()
    sys.exit (0)
  elif (UU == "back"):
    script ()
  bbb = input ("BBB = ")
  if (bbb == "exit"):
    clear ()
    sys.exit (0)
  elif (bbb == "back"):
    script ()
  if (bbb == ''):
    bbb = 10133
  
  TTf = float (TT)
  UUf = float (UU) 
  bbbf = float (bbb)
  
  if bbbf < 700:
    p = (bbbf + 10000) / 10
  else:
    p = bbbf / 10
  TTf1 = TTf / 10 
  for HT in range (-5000, 4000):
    HTd = HT / 100
    e = 2.718282 
    c1 = 6.10780 
    c2 = 17.08085
    c3 = 234.175
    expTT = (c2 * TTf1) / (c3 + TTf1)
    SVPTT = c1 * pow (e, expTT) 
    expHT = (c2 * HTd) / (c3 + HTd)
    SVPHT = c1 * pow (e, expHT) 
    SVPDT = SVPHT - (0.000660 * (1 + 0.0015 * HTd)) * p * (TTf1 - HTd) 
    U_test = round (SVPDT / SVPTT * 100)
    if U_test == UUf:
      break
  if HTd >= 0:
    HTa = round(HT / 10)
    HTap = str (HTa)
    print (" ")
    print ("#####")
    print (" ")
    print ("HT = " + HTap)
    print (" ")
    print ("#####")
    fuex ()
  else:
    for HTl in range (-5000, 4000):
      HTdl = HTl / 100
      e = 2.718282 
      c1 = 6.10780 
      c2 = 17.08085
      c3 = 234.175
      cl1 = 6.10714 
      cl2 = 22.44294
      cl3 = 272.440
      expTTl = (c2 * TTf1) / (c3 + TTf1)
      SVPTTl = c1 * pow (e, expTTl) 
      expHTl = (cl2 * HTdl) / (cl3 + HTdl)
      SVPHTl = cl1 * pow (e, expHTl) 
      SVPDTl = SVPHTl - 0.000582 * p * (TTf1 - HTdl) 
      U_test_led = round (SVPDTl / SVPTTl * 100)
      if U_test_led == UUf:
        break
    for HTv in range (-5000, 4000):
      HTdv = HTv / 100
      e = 2.718282 
      c1 = 6.10780 
      c2 = 17.08085
      c3 = 234.175
      cv1 = 6.10780
      cv2 = 17.84362
      cv3 = 245.425
      expTTv = (c2 * TTf1) / (c3 + TTf1)
      SVPTTv = c1 * pow (e, expTTv) 
      expHTv = (cv2 * HTdv) / (cv3 + HTdv)
      SVPHTv = cv1 * pow (e, expHTv) 
      SVPDTv = SVPHTv - (0.000660 * (1 + 0.0015 * HTd)) * p * (TTf1 - HTd) 
      U_test_voda = round (SVPDTv / SVPTTv * 100)
      if U_test_voda == UUf:
        break
    HTal = round (HTl / -10)
    HTav = round (HTv / -10)
    HTalp = str (HTal)
    HTavp = str (HTav)
    print (" ")
    print ("#####")
    print (" ")
    print ("HT = W" + HTavp + " [I" + HTalp + "]")
    print (" ")
    print ("#####")
    fuex ()

def fuex ():
  ex = input ("[1 (new calculation), 2 (exit)]: ")
  if ex == '':
    print ("Wrong input!")
    fuex ()
  else:
    ex1 = float (ex)
    if ex1 == 1:
      script ()
    elif ex1 == 2:
      clear ()
      sys.exit (0)    
    else:
      print ("Wrong input!")
      fuex ()

script ()
