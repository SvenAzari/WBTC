#WET-BULB TEMPERATURE CALCULATOR gui
#You need to have Python3 and PySimpleGUI installed in order to run this script.
#To run script, open CLI on your system and type python3 wbtc_gui.py

import math
import PySimpleGUI as sg

def main():
  sg.theme ('DarkBlue')
  layout = [  [sg.Text("WET-BULB TEMPERATURE CALCULATOR")],
              [sg.Text("TT =   "), sg.InputText(size=(5,1), key='input_tt')],
              [sg.Text("UU =  "), sg.InputText(size=(5,1), key='input_uu')],
              [sg.Text("BBB ="), sg.InputText(size=(5,1), key='input_bbb')],
              [sg.Text('HT =', key='-TEXT-')],
              [sg.Button("Calculate"), sg.Button("New"), sg.Button("Help"), sg.Button("Exit")],
    ]

  window = sg.Window("WBTC gui - Version 2.1", layout)

  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Calculate":
      tt = values['input_tt']
      uu = values['input_uu']
      bbb = values['input_bbb']
      #float
      TTf = float (tt)
      UUf = float (uu)
      if bbb == '':
        bbbf = 133
      else: 
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
        HTc = "HT = " + HTap
        window['-TEXT-'].update(HTc)
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
        HTc = "HT = W" + HTavp + " [I" + HTalp + "]"
        window['-TEXT-'].update(HTc)

    elif event == "Help":
      sg.Print ("TT - air temperature [°C] - input without decimal point (21.5 = 215)")
      sg.Print ("UU - air humidity [%]")
      sg.Print ("BBB - atmospheric pressure [hPa] - input without thousand digit nor decimal point (999.8 = 9998 or 1013.3 = 133) - leave empty if unknown")
      sg.Print ("HT - calcualted wet-bulb temperature [°C] - printed without decimal point - if calculated value is negative, instead of - sign, there will be W or I in front of number - W indicates there is water on wet-bulb termomether sensor and I indicates there is ice - value in [] is for wet-bulb temperature with ice on bet-bulb termomether sensor")
    
    elif event == "New":
      window['input_tt'].update('')
      window['input_uu'].update('')
      window['input_bbb'].update('')
      window['-TEXT-'].update('')
    
  window.close()

main ()
