# -*- coding: utf-8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#

import wx
import os

class MiniEditor(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,title="MiniEditor 0.1.0",size=(600,400))
		self.icono = wx.Icon('img/editor_icono.png')
		self.SetIcon(self.icono)
		self.archivo = 'untitled.txt'
		
		# Sizer
		sz = wx.BoxSizer(wx.VERTICAL)
		
		# Editor
		self.editor = wx.TextCtrl(self, -1, u"", style=wx.TE_MULTILINE)
		self.configurarEditor()
		
		# Crear barra de menu
		self.crearMenu()
		
		# Agregar al sizer
		sz.Add(self.editor, 1, wx.EXPAND|wx.ALL,)
		self.SetSizer(sz)
		
		self.Centre(True)
		self.Show()
		
		
	def configurarEditor(self):
		"""
		Configura las características iniciales del editor
		"""
		self.fuente=wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
		self.fuente.SetFaceName("Courier New")
		self.editor.SetFont(self.fuente)
		self.editor.SetBackgroundStyle(True)
	
	def crearMenu(self):		
		"""
		Crea la barra de menú
		"""
		marchivo=wx.Menu()
		abrir=marchivo.Append(-1, "Abrir\tCtrl-O")
		guardar=marchivo.Append(-1, "Guardar\tCtrl-S")
		guardarComo=marchivo.Append(-1, "Guardar como")
		
		meditar=wx.Menu()
		copiar=meditar.Append(-1, "Copiar\tCtrl-C")
		pegar=meditar.Append(-1, "Pegar\tCtrl-V")
		
		self.mtema=wx.Menu()
		classic=self.mtema.Append(-1, "Classic")
		dark=self.mtema.Append(-1, "Dark")
		retro=self.mtema.Append(-1, "Retro")
		pink=self.mtema.Append(-1, "Pink")
		
		mayuda=wx.Menu()
		ayuda=mayuda.Append(-1, "Ayuda")
		acerca=mayuda.Append(-1, "Acerca de...")
		
		barraMenu=wx.MenuBar()
		barraMenu.Append(marchivo, "Archivo")
		barraMenu.Append(meditar, "Editar")
		barraMenu.Append(self.mtema, "Seleccionar tema")
		barraMenu.Append(mayuda, "Ayuda")
		self.SetMenuBar(barraMenu)
		
		# Definición de "eventos"
		self.Bind(wx.EVT_MENU, self.abrirArchivo, abrir)
		self.Bind(wx.EVT_MENU, self.guardarArchivoComo, guardarComo)
		self.Bind(wx.EVT_MENU, self.guardarArchivo, guardar)
		
		self.Bind(wx.EVT_MENU, self.copiar, copiar)
		self.Bind(wx.EVT_MENU, self.pegar, pegar)
		
		self.Bind(wx.EVT_MENU, self.configurarTema, classic)
		self.Bind(wx.EVT_MENU, self.configurarTema, dark)
		self.Bind(wx.EVT_MENU, self.configurarTema, retro)
		self.Bind(wx.EVT_MENU, self.configurarTema, pink)
		
		self.Bind(wx.EVT_MENU, self.acerca, acerca)
		self.Bind(wx.EVT_MENU, self.ayuda, ayuda)
	
	def abrirArchivo(self, event):
		dlg=wx.FileDialog(self, "Abrir archivo", os.getcwd(), style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			try:
				fid=open(dlg.GetPath(),'r')
				texto=fid.readlines()
				self.texto="".join(texto)
				self.texto = self.texto.decode("utf8")
				fid.close()
				self.editor.SetValue(self.texto)
				self.archivo=dlg.GetPath()
				self.SetTitle("MiniEditor "+self.archivo)
			except:
				wx.MessageBox(u"Archivo no válido","Error")
		dlg.Destroy()
	
	def guardarArchivoComo(self, event):
		"""
		Guarda el archivo actual abriendo un cuadro de diálogo
		"""
		dlg=wx.FileDialog(self, "Guardar", os.getcwd(), style=wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			fid=open(dlg.GetPath(),'w')
			txt=str(self.editor.GetValue().encode('utf8'))
			fid.write(txt)
			fid.close()
			self.archivo=dlg.GetPath()
		dlg.Destroy()
		
	def guardarArchivo(self,event):
		"""
		Guarda el archivo actual 
		"""
		if hasattr(self, 'archivo'):
			fid=open(self.archivo,'w')
			txt=str(self.editor.GetValue().encode('utf8'))
			fid.write(txt)
			fid.close()
			wx.MessageBox("Hecho","MiniEditor")
		else:
			self.guardarArchivoComo(None)
	
	def copiar(self,event):
		"""
		Copia el texto seleccionado al portapapeles
		"""
		texto=wx.TextDataObject(self.editor.GetStringSelection())
		if wx.TheClipboard.Open():
			wx.TheClipboard.SetData(texto)
			wx.TheClipboard.Close()
			
	def pegar(self,event):
		"""
		Pega el texto ubicado en el portapapeles
		"""
		txt=wx.TextDataObject()
		if wx.TheClipboard.Open():
			success=wx.TheClipboard.GetData(txt)
			wx.TheClipboard.Close()
		if success:
			self.editor.SetInsertionPoint(self.editor.GetInsertionPoint())	
			self.editor.write(txt.GetText())
	
		
	def configurarTema(self,event):
		"""
		Modifica el color de fondo y fuente del editor.
		"""
		tema_sel=self.mtema.FindItemById(event.GetId()).GetText()
		temas={'Classic':((0,0,255),(255,255,255)),
		'Dark':((200,200,200),(0,0,0)),
		'Retro':((0,255,0),(0,0,0)),
		'Pink':((20,50,50),(250,180,180))}
		self.editor.SetForegroundColour(temas[tema_sel][0])
		self.editor.SetBackgroundColour(temas[tema_sel][1])
		self.editor.Refresh()
		
	def ayuda(self,event):
		wx.MessageBox("No disponible","MiniEditor")
		
	def acerca(self, event):
		"""
		Muestra un cuadro de diálogo con información 
		básica acerca de la aplicación.
		"""
		descripcion="Editor de texto sin formato desarrollado en wxPython"
		info=wx.AboutDialogInfo()
		info.SetName('MiniEditor')
		info.SetDescription(descripcion)
		info.SetVersion('0.1.0')
		info.SetLicense('MIT License')
		info.SetDevelopers(['Pedro Jorge De Los Santos'])
		info.SetWebSite(('labdls.blogspot.mx','LAB DLS'))
		info.SetCopyright('(c) 2016')
		wx.AboutBox(info)


if __name__=='__main__':
	app=wx.App()
	frame = MiniEditor(None)
	app.MainLoop()
