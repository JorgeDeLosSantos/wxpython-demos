# -*- coding: utf8 -*-
import wx

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(250,200))
		self.sz = wx.BoxSizer(wx.VERTICAL)
		
		# Botón normal
		self.button = wx.Button(self, -1, u"Botón")
		# Modificando fuente del botón
		self.font1 = self.button.GetFont()
		self.font1.SetPointSize(14)
		self.button.SetFont(self.font1)
		# Botón con ícono
		self.bitbutton = wx.Button(self, -1, u"Botón con ícono")
		self.bitbutton.SetBitmap(wx.Bitmap("img/ic_button_01.png"))
		# Botón plano
		self.flatbutton = wx.Button(self, -1, u"Botón plano", 
									style=wx.BORDER_NONE)
		
		self.sz.Add(self.button, 1, wx.EXPAND|wx.ALL, 5)
		self.sz.Add(self.bitbutton, 1, wx.EXPAND|wx.ALL, 5)
		self.sz.Add(self.flatbutton, 1, wx.EXPAND|wx.ALL, 5)
		
		self.SetSizer(self.sz)
		self.Centre(True)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None, u"wxButton Demo")
	app.MainLoop()
