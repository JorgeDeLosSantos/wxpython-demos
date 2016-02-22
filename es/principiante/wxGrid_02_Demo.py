# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#
import wx
import wx.grid as wxgrid
from random import randint

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(280,250))
		self.sz = wx.BoxSizer(wx.VERTICAL)
		
		self.grid = wxgrid.Grid(self)
		# Creamos grilla de 10x2
		filas, columnas = 10, 3
		self.grid.CreateGrid(filas,columnas)
		# Asignamos valores a las celdas
		for i in range(filas):
			for j in range(columnas):
				val = "%s"%(randint(0,100))
				self.grid.SetCellValue(i,j,val)
		
		# Asignando colores aleatorios
		for ii in range(filas):
			for jj in range(columnas):
				clr = wx.Colour(randint(0,255),randint(0,255),randint(0,255))
				self.grid.SetCellBackgroundColour(ii,jj,clr)
		
		# Quitando las etiquetas de filas
		self.grid.SetRowLabelSize(0)
		
		# Modificando etiquetas de columna
		lbl = {0:"Tiempo", 1:"Temperatura", 2:u"Presión"}
		for col,header in lbl.items():
			self.grid.SetColLabelValue(col,header)
		
		self.sz.Add(self.grid, 1, wx.EXPAND|wx.ALL, 2)
		self.SetSizer(self.sz)
		self.Centre(True)
		self.Show()

if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None, u"Simple Grid Demo")
	app.MainLoop()
