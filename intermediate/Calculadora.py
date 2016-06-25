# -*- coding: utf8 -*-
from __future__ import division # python 2.X version
import wx

class Calculadora(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(150,240),
		style=wx.DEFAULT_FRAME_STYLE & ~(wx.MAXIMIZE_BOX|wx.RESIZE_BORDER))
		self.Centre(True)
		
		# Paneles
		self.panel_pantalla = wx.Panel(self, -1)
		self.panel_onoff = wx.Panel(self, -1)
		self.panel_teclado = wx.Panel(self, -1)
		
		# Sizers
		self.mainsz=wx.FlexGridSizer(rows=3, cols=1) # Sizer principal
		self.pantallasz=wx.FlexGridSizer(rows=1, cols=1) 
		self.onoffsz=wx.BoxSizer(wx.HORIZONTAL)
		self.tecladosz=wx.FlexGridSizer(rows=4, cols=4)
		
		# Inicializar componentes
		self.crearPantalla()
		self.crearOnOff()
		self.crearTeclado()
		
		# Agregar a sizers 
		self.mainsz.Add(self.panel_pantalla, 1, wx.EXPAND|wx.ALL)
		self.mainsz.Add(self.panel_onoff, 1, wx.EXPAND|wx.ALL)
		self.mainsz.Add(self.panel_teclado, 5, wx.EXPAND|wx.ALL)
		
		self.panel_pantalla.SetSizer(self.pantallasz)
		self.panel_onoff.SetSizer(self.onoffsz)
		self.panel_teclado.SetSizer(self.tecladosz)
		self.SetSizer(self.mainsz)
		
		self.Fit()
		# Inicializa valores por defecto
		self.cadenaMostrar=""
		self.cadenaEvaluar=""
		
	def crearPantalla(self):
		""" Crea la pantalla de la calculadora """
		self.pantalla=wx.TextCtrl(self.panel_pantalla, -1, u"")
		self.pantalla.SetFont(wx.Font(16, wx.MODERN, wx.NORMAL, wx.BOLD, face="Courier New"))
		self.pantallasz.Add(self.pantalla, 1, wx.EXPAND|wx.ALL, 2)
		self.pantallasz.AddGrowableCol(0)
		
	def crearOnOff(self):
		""" Crea los botones ON y OFF """
		self.on=wx.Button(self.panel_onoff, -1, "ON")
		self.off=wx.Button(self.panel_onoff, -1, "OFF")
		self.on.SetBackgroundColour((200,10,10))
		self.on.SetForegroundColour('WHITE')
		self.off.SetBackgroundColour((10,10,200))
		self.off.SetForegroundColour('WHITE')
		
		
		# Conectando eventos
		self.Bind(wx.EVT_BUTTON, self.OnOn, self.on)
		self.Bind(wx.EVT_BUTTON, self.OnOff, self.off)
		
		self.onoffsz.Add(self.on, 1, wx.EXPAND|wx.ALL, 2)
		self.onoffsz.Add(self.off, 1, wx.EXPAND|wx.ALL, 2)
		#self.onoffsz.AddGrowableRow(0)
	
	def crearTeclado(self):
		""" Crea el teclado numérico y de operadores """
		teclas="7 8 9 / 4 5 6 * 1 2 3 - 0 . = +".split()
		for tecla in teclas:
			this=wx.Button(self.panel_teclado, -1, tecla, size=(40,-1))
			self.tecladosz.Add(this, 1, wx.EXPAND|wx.ALL, 2)
			self.Bind(wx.EVT_BUTTON, self.calcular, this)
		
	def calcular(self,event):
		tecla=wx.FindWindowById(event.GetId()).GetLabelText()
		numeros='1234567890.' # Incluyendo al punto ...
		operadores='+-*/'
		evaluador='='
		if numeros.find(tecla)!=-1:
		    self.cadenaMostrar=self.cadenaMostrar+tecla
		    self.cadenaEvaluar=self.cadenaEvaluar+tecla
		    self.pantalla.SetValue(self.cadenaMostrar)
		elif operadores.find(tecla)!=-1:
			self.cadenaEvaluar=self.cadenaEvaluar+tecla
			self.pantalla.SetValue(self.cadenaMostrar)
			self.cadenaMostrar=""
		elif tecla == evaluador:
			try:
			    resultado=eval(self.cadenaEvaluar)
			    self.pantalla.SetValue(str(resultado))
			except:
				wx.MessageBox("Algo va mal...","Calculadora")
			self.OnOn
		
	def OnOn(self,event):
		self.cadenaEvaluar=""
		self.cadenaMostrar=""
		self.pantalla.SetValue("0")
			
	def OnOff(self,event):
		self.pantalla.SetValue(wx.EmptyString)
		self.cadenaEvaluar=""
		self.cadenaMostrar=""

if __name__=='__main__':
	app=wx.App()
	frame=Calculadora(None, "Calculadora")
	frame.Show()
	app.MainLoop()
			
