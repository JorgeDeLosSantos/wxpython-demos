# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#
import wx

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(300,200))
		# Configurando el color de fondo
		self.SetBackgroundColour("#77ee77")
		# Centrando la ventana
		self.Centre(True)
		# Descomentar la siguiente línea para ventana maximizada.
		#self.Maximize(True)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None, u"wxFrame Demo")
	app.MainLoop()
