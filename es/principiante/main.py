# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#
import wx
import glob

all_demos = glob.glob("*.py")
all_demos.remove("main.py")

def main():
	app = wx.App()
	wx.MessageBox("Cierre la ventana actual para mostrar la siguiente.")
	for demo in all_demos:
		execfile(demo)
	app.MainLoop()

if __name__=='__main__':
	main()
