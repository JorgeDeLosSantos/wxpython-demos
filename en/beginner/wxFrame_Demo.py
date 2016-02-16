# -*- coding: utf8 -*-
import wx

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(300,200))
		
		# Configurando el color de fondo
		self.SetBackgroundColour("#fe7b7b")
		# Centrando la ventana
		self.Centre(True)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None, u"wxFrame Demo")
	app.MainLoop()
