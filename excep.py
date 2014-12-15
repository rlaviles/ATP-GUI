#! /usr/bin/env python
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
from class2 import *
from class3 import *
from Tkconstants import LEFT

class App(Tkinter.Frame):
  def __init__(self, root):

    Tkinter.Frame.__init__(self, root)
    button_opt = {'fill': Tkconstants.BOTH, 'padx': 10, 'pady': 10, 'side': LEFT}
    self.file_opt = options = {}
    options['defaultextension'] = '' # couldn't figure out how this works
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    options['initialdir'] = 'C:\\'
    options['initialfile'] = 'myfile.txt'
    options['parent'] = root
    options['title'] = 'This is a title'

    Tkinter.Button(self, text='Pick_acuRepFile', bg="yellow", fg="black", command=self.acuRep_File).pack(**button_opt)
    Tkinter.Button(self, text='XTAZ', bg="yellow", fg="black", command=self.xTilt).pack(**button_opt)
    Tkinter.Button(self, text='Disp0', bg="yellow", fg="black", command=self.LinDisp0).pack(**button_opt)
    Tkinter.Button(self, text='Disp1', bg="yellow", fg="black", command=self.LinDisp1).pack(**button_opt)
    Tkinter.Button(self, text='Disp2', bg="yellow", fg="black", command=self.LinDisp2).pack(**button_opt)
    Tkinter.Button(self, text='Disp3', bg="yellow", fg="black", command=self.LinDisp3).pack(**button_opt)
    Tkinter.Button(self, text='Tilt0Time', bg="yellow", fg="black", command=self.Tilt0Time).pack(**button_opt)
    Tkinter.Button(self, text='Disp0Time', bg="yellow", fg="black", command=self.LinDisp0Time).pack(**button_opt)
    Tkinter.Button(self, text='Pick_PSC_File', bg="black", fg="yellow", command=self.psc_File).pack(**button_opt)
    Tkinter.Button(self, text='AZ_ONvsComm', bg="black", fg="yellow", command=self.azONvsCO).pack(**button_opt)
    Tkinter.Button(self, text='EL_ONvsComm', bg="black", fg="yellow", command=self.elONvsCO).pack(**button_opt)
    Tkinter.Button(self, text='AZEL_ONvsComm', bg="black", fg="yellow", command=self.both).pack(**button_opt)
    Tkinter.Button(self, text='AZ_Diff', bg="black", fg="yellow", command=self.az_diff).pack(**button_opt)
    Tkinter.Button(self, text='EL_Diff', bg="black", fg="yellow", command=self.el_diff).pack(**button_opt)
    Tkinter.Button(self, text='Help',  bg="yellow", fg="black", command=self.help).pack(**button_opt)
    Tkinter.Button(self, text='salir', bg="green", fg="black", command='exit').pack(**button_opt)

  def acuRep_File(self):
    try:
       Separator()
       return
    except Exception:
       print('You had chosen a wrong kind of file: pick an acuReport file!!\n')
       tkMessageBox.showwarning(
            "Open an acuReport file",
            "You had chosen a wrong file. Please pick an acuReport file!\n")
       return

  def psc_File(self):
  #try:
    Creator()
  # return
  #except Exception:
  # print('You had chosen a wrong file: pick a Position Stream Client file!!\n')
  # tkMessageBox.showwarning(
  # "Open a PositionStreamClient file",
  # "You had chosen a wrong file. Please pick a PositionStreamClient file!\n")
  # return

  def xTilt(self):
    xtaz(Separator)
    return

  def LinDisp0(self):
    disp0(Separator)
    return

  def LinDisp1(self):
    disp1(Separator)
    return

  def LinDisp2(self):
    disp2(Separator)
    return

  def LinDisp3(self):
    disp3(Separator)
    return

  def Tilt0Time(self):
    x0time(Separator)
    return

  def LinDisp0Time(self):
    d0time(Separator)
    return

  def help(self):
    tkMessageBox.showinfo("HELP on GraphTool",
"Pick either an acuReport or a Position Stream Client file, then choose the appropiate graph you want to see!\n" 
" Options for acuReport files:\n"
" XTAZ - graphs the xtilt0 data as function of the movement in Azimuth\n"
" Disp0- graphs the Linear Displacement Sensor 0 data as function of Azimuth\n"
" Disp1- graphs the Linear Displacement Sensor 0 data as function of Azimuth\n"
" Disp2- graphs the Linear Displacement Sensor 0 data as function of Azimuth\n"
" Disp3- graphs the Linear Displacement Sensor 0 data as function of Azimuth\n"
" TiltoTime - graphs the behaviour of the xTilt0 sensor as function of the time\n"
" Disp0Time - graphs the behaviour of the Lin. Disp. Sensor 0 as function of time\n\n"
" Options for Position Stream Client files:\n"
" AZ_ONvsComm - graphs the ON_TE and Commanded Azimuth positions\n"
" EL_ONvsComm - graphs the ON_TE and Commanded Elevation positions\n"
" AZEL_ONvsComm - graphs the ON_TE and Commanded Az and El positions (double plot)\n"
" AZ_Diff - graphs the difference between AZ ON_TE and AZ Commanded position\n"
" EL_Diff - graphs the difference between EL ON_TE and EL Commanded position\n\n"  
" (c) Roberto Aviles A. - December 8, 2008.")
    return

  def azONvsCO(self):
    az_onvsco(Creator)
    return

  def elONvsCO(self):
    el_onvsco(Creator)
    return

  def both(self):
    azel_onvsco(Creator)
    return

  def az_diff(self):
    az_diff_onvsco(Creator)
    return

  def el_diff(self):
    el_diff_onvsco(Creator)
    return

if __name__=='__main__':
  root = Tkinter.Tk()
  root.title("Graph Tool")
  root.minsize()
  App(root).pack()
  root.mainloop()
