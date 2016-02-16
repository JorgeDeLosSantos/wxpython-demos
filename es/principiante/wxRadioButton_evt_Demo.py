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
		wx.Frame.__init__(self,parent,title=title,size=(200,200))
		self.sz = wx.BoxSizer(wx.VERTICAL)
		
		self.rb1 = wx.RadioButton(self, -1, label = 'Azul')
		self.rb2 = wx.RadioButton(self, -1, label = 'Rojo')
		self.rb3 = wx.RadioButton(self, -1, label = 'Verde')
		self.rb4 = wx.RadioButton(self, -1, label = 'Blanco')
		
		self.sz.Add(self.rb1, 1, wx.EXPAND|wx.ALL, 10)
		self.sz.Add(self.rb2, 1, wx.EXPAND|wx.ALL, 10)
		self.sz.Add(self.rb3, 1, wx.EXPAND|wx.ALL, 10)
		self.sz.Add(self.rb4, 1, wx.EXPAND|wx.ALL, 10)
		
		self.Bind(wx.EVT_RADIOBUTTON, self.OnSelect)
		
		self.SetSizer(self.sz)
		# Centrando la ventana
		self.Centre(True)
		self.Show()
		
	def OnSelect(self,event):
		sel = event.GetEventObject().GetLabel()
		colores = {"Azul":"blue",
				   "Verde":"green",
				   "Rojo":"red",
				   "Blanco":"white"}
		self.SetBackgroundColour(colores[sel])
		self.Refresh()
		

if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None, u"wxRadioButtton Demo")
	app.MainLoop()
